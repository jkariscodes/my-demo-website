from django.contrib import admin

from .models import EmailMessage, BlogPost, BlogCategory


@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
    )


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
