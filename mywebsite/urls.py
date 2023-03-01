from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from website.sitemaps import BlogPostSitemap

sitemaps = {"blogposts": BlogPostSitemap}

urlpatterns = [
    path("tajiri/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("website.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("my-api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

if settings.PROJECT_ENV == "development":
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
