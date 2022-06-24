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
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('blog/', BlogListView.as_view(), name='blog_posts'),
    path('blog/post/<uuid:pk>/', BlogDetailView.as_view(), name='blog_article'),
    path('blog/post/create/', BlogCreateView.as_view(), name='blog_article_create'),
    path('blog/post/<uuid:pk>/update/', BlogUpdateView.as_view(), name='blog_article_update'),
    path('blog/post/<uuid:pk>/delete/', BlogDeleteView.as_view(), name='blog_article_delete'),
]
