from django.contrib import admin
from .models import UserDescription, BlogPost, BlogCategory, Comment


@admin.register(UserDescription)
class UserDescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
