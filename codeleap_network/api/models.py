from django.db import models
from django.contrib.auth.models import User # Django's default User model
from django.conf import settings # To reference the User model flexibly

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE, verbose_name="Author")
    title = models.CharField(max_length=255, verbose_name="Title") # Novo campo Title
    content = models.TextField(verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    # For likes: a ManyToMany relationship with User.
    # Each user can like multiple posts, and each post can be liked by multiple users.
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True, verbose_name="Likes")

    def __str__(self):
        return f"Post {self.id} by {self.author.username}: {self.title}"

    @property
    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-created_at'] # Most recent posts first by default
        verbose_name = "Post"
        verbose_name_plural = "Posts"

class Comment(models.Model): # Renomeado de Comentario para Comment
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, verbose_name="Post") # related_name comments
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='made_comments', on_delete=models.CASCADE, verbose_name="Author") # related_name made_comments
    content = models.TextField(verbose_name="Comment Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"Comment by {self.author.username} on '{self.post.title}'"

    class Meta:
        ordering = ['created_at'] # Oldest comments first by default
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
