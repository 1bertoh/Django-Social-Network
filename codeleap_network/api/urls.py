from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views import CommentViewSet, PostViewSet, UserCreateView
# from .views import UserCreateView, PostViewSet, CommentViewSet # Já importado acima

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment') # Mudou para 'comments' e basename 'comment'

urlpatterns = [
    path('', include(router.urls)),
    path('users/register/', UserCreateView.as_view(), name='register_user'), # name em inglês
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]