from rest_framework import serializers

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = BlogPost
        fields = (
            "title",
            "id",
            "body",
            "category",
            "status",
            "author",
        )
