from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BlogSearchView,
    EmailSuccess,
    BlogPostListAPIView,
    BlogPostDetailAPIView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("contact/success/", EmailSuccess.as_view(), name="email_success"),
    path("blog/", BlogListView.as_view(), name="blog_posts"),
    path("blog/post/<uuid:pk>/", BlogDetailView.as_view(), name="blog_article"),
    path("blog/post/create/", BlogCreateView.as_view(), name="blog_article_create"),
    path(
        "blog/post/<uuid:pk>/update/",
        BlogUpdateView.as_view(),
        name="blog_article_update",
    ),
    path(
        "blog/post/<uuid:pk>/delete/",
        BlogDeleteView.as_view(),
        name="blog_article_delete",
    ),
    path("blog/search/", BlogSearchView.as_view(), name="blog_posts_search"),
    path("blog-api/v1/", BlogPostListAPIView.as_view(), name="blog_list_api"),
    path(
        "blog-api/v1/<uuid:pk>/",
        BlogPostDetailAPIView.as_view(),
        name="blog_detail_api",
    ),
]
