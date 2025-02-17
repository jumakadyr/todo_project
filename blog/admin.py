from django.contrib import admin
from blog.models import Post, Category, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner")
    list_display_links = ("id", "title")
    list_filter = ("category",)
    search_fields = ("title", "content")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "post")
    list_display_links = ("id", "owner")
