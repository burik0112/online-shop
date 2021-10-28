from django.contrib import admin

from posts.models import PostModel, AuthorModel, PostTagModel, CommentModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['title']


@admin.register(PostTagModel)
class PostTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', ]
    list_filter = ['created_at', 'author', 'tags']
    autocomplete_fields = ['author', 'tags']


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['phone', 'created_at', 'name', 'email','comment']
    list_filter = ['created_at','phone']
    search_fields = ['name']