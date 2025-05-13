from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Post, Comment # Mudou para Comment

class UserSerializer(serializers.ModelSerializer): # Renomeado de UsuarioSerializer
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm password") # Label em inglês

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'password2')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'email': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."}) # Mensagem em inglês
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class AuthorSerializer(serializers.ModelSerializer): # Renomeado de AutorPostSerializer
    """ Simplified serializer for the author within Post/Comment """
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')

class CommentSerializer(serializers.ModelSerializer): # Renomeado de ComentarioSerializer
    author = AuthorSerializer(read_only=True) # Usa AuthorSerializer

    class Meta:
        model = Comment # Mudou para Comment
        fields = ('id', 'post', 'author', 'content', 'created_at', 'updated_at') # Campos em inglês
        read_only_fields = ('created_at', 'updated_at', 'author') # author is set in the view

    def create(self, validated_data):
        # The author will be the logged-in user, set in the view
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True) # Usa AuthorSerializer
    total_likes = serializers.IntegerField(read_only=True) # Model property

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'created_at', 'updated_at', 'total_likes', 'likes') # Adicionado title, campos em inglês
        read_only_fields = ('created_at', 'updated_at', 'author', 'likes') # author is set in the view

    def create(self, validated_data):
        # The author will be the logged-in user, set in the view
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)