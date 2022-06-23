from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    BlogListView,
    BlogDetailView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('blog/', BlogListView.as_view(), name='blog_posts'),
    path('blog/post/<uuid:pk>/', BlogDetailView.as_view(), name='blog_article'),
]
