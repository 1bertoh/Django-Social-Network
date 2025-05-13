from django.contrib import admin
from .models import Post, Comment # Mudou para Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'short_content', 'total_likes', 'created_at', 'updated_at') # Adicionado title, campos em inglês
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content', 'author__username') # Adicionado title
    readonly_fields = ('total_likes',)

    def short_content(self, obj): # Renomeado de conteudo_resumido
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    short_content.short_description = "Content" # Descrição em inglês


@admin.register(Comment) # Mudou para Comment
class CommentAdmin(admin.ModelAdmin): # Mudou para CommentAdmin
    list_display = ('id', 'short_post_title', 'author', 'short_content', 'created_at') # Campos em inglês
    list_filter = ('created_at', 'author', 'post')
    search_fields = ('content', 'author__username', 'post__title', 'post__content') # Adicionado post__title

    def short_content(self, obj): # Renomeado de conteudo_resumido
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    short_content.short_description = "Content"

    def short_post_title(self, obj): # Renomeado de post_resumido
        return obj.post.title[:30] + "..." if len(obj.post.title) > 30 else obj.post.title
    short_post_title.short_description = "Post Title"