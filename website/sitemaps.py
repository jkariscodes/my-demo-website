from django.contrib.sitemaps import Sitemap
from .models import BlogPost


class BlogPostSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return BlogPost.objects.all().filter(status="published")

    def lastmod(self, obj):
        return obj.updated
