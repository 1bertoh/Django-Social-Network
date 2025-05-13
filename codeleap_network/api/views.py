from rest_framework import generics, viewsets, status, permissions as drf_permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.models import User

from .models import Post, Comment # Mudou para Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer # Mudou nomes dos serializers
from .permissions import IsOwnerOrReadOnly
from api import serializers

class UserCreateView(generics.CreateAPIView): # Renomeado de CriarUsuarioView
    queryset = User.objects.all()
    permission_classes = (drf_permissions.AllowAny,)
    serializer_class = UserSerializer # Mudou para UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [drf_permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author__username', 'likes__username'] # Campos em inglês
    search_fields = ['title', 'content', 'author__username'] # Adicionado title, campos em inglês
    ordering_fields = ['title', 'created_at', 'total_likes', 'updated_at'] # Adicionado title, campos em inglês

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) # Mudou para author

    @action(detail=True, methods=['post'], permission_classes=[drf_permissions.IsAuthenticated], url_path='like-unlike') # url_path em inglês
    def like_unlike(self, request, pk=None): # Renomeado de curtir_descurtir
        """
        Action to like or unlike a post.
        If the user has already liked it, remove the like. Otherwise, add it.
        """
        post = self.get_object()
        user = request.user

        if user in post.likes.all(): # Mudou para post.likes
            post.likes.remove(user)
            liked = False
        else:
            post.likes.add(user)
            liked = True
        
        post.save()
        serializer = self.get_serializer(post)
        return Response({'liked': liked, 'total_likes': post.total_likes, 'post': serializer.data}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='who-liked') # url_path em inglês
    def who_liked(self, request, pk=None): # Renomeado de quem_curtiu
        """ Returns the list of users who liked the post. """
        post = self.get_object()
        likers = post.likes.all() # Mudou para post.likes
        serializer = AuthorSerializer(likers, many=True, context={'request': request}) # Usa AuthorSerializer
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet): # Renomeado de ComentarioViewSet
    queryset = Comment.objects.all() # Mudou para Comment
    serializer_class = CommentSerializer # Mudou para CommentSerializer
    permission_classes = [drf_permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['post', 'author__username'] # Mudou para author__username
    ordering_fields = ['created_at'] # Mudou para created_at

    def get_queryset(self):
        queryset = super().get_queryset()
        post_pk = self.kwargs.get('post_pk')
        if post_pk:
            queryset = queryset.filter(post_id=post_pk)
        return queryset
    
    def perform_create(self, serializer):
        post_pk = self.kwargs.get('post_pk')
        if post_pk:
            try:
                post_obj = Post.objects.get(pk=post_pk)
                serializer.save(author=self.request.user, post=post_obj) # Mudou para author
            except Post.DoesNotExist:
                raise serializers.ValidationError("Post not found.") # Mensagem em inglês
        else:
            serializer.save(author=self.request.user) # Mudou para author