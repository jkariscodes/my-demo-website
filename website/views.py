from django.conf import settings
from rest_framework import generics, permissions
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .serializers import BlogPostSerializer
from .permissions import IsOwnerOrReadOnly
from .models import EmailMessage, BlogPost
from .forms import ContactForm


class HomePageView(TemplateView):
    """
    Landing page view.
    """

    template_name = "website/home.html"


class AboutPageView(TemplateView):
    """
    About page template view.
    """

    template_name = "website/about.html"


class BlogListView(ListView):
    """
    Blog posts/articles view.
    """

    model = BlogPost
    context_object_name = "blog_posts"
    template_name = "website/blog_posts.html"
    paginate_by = 4


class BlogDetailView(DetailView):
    """
    Single blog post/article view.
    """

    model = BlogPost
    context_object_name = "blog_article"
    template_name = "website/blog_article.html"


class BlogCreateView(LoginRequiredMixin, CreateView):
    """
    Create blog post/article view.
    """

    model = BlogPost
    context_object_name = "blog_article_create"
    template_name = "website/blog_article_create.html"
    fields = ["title", "body", "category", "status"]
    success_url = reverse_lazy("blog_posts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Blog post edit/update view.
    """

    model = BlogPost
    context_object_name = "blog_article_update"
    template_name = "website/blog_article_update.html"
    fields = ["title", "body", "category", "status"]
    success_url = reverse_lazy("blog_posts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        my_obj = self.get_object()
        return my_obj.author == self.request.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Blog post delete confirm view.
    """

    model = BlogPost
    context_object_name = "blog_article_delete"
    template_name = "website/blog_article_delete.html"
    success_url = reverse_lazy("blog_posts")

    def test_func(self):
        my_obj = self.get_object()
        return my_obj.author == self.request.user


class ContactPageView(FormView):
    """
    Email contact form view.
    """

    template_name = "website/contact.html"
    form_class = ContactForm
    success_url = "/contact/success/"

    def form_valid(self, form):
        name = form.cleaned_data.get("name")
        from_email = form.cleaned_data.get("from_email")
        subj = form.cleaned_data.get("subject")
        msg = form.cleaned_data.get("message")
        send_mail(subj, msg, from_email, [settings.DEFAULT_FROM_EMAIL])
        form.save()
        form = ContactForm
        return super().form_valid(form)


class EmailSuccess(TemplateView):
    """
    Email success template view.
    """

    template_name = "website/email_success.html"


class BlogSearchView(ListView):
    """
    Blog posts search list view.
    """

    model = BlogPost
    context_object_name = "blog_search_list"
    template_name = "website/blog_posts_search.html"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        return BlogPost.objects.filter(
            Q(title__icontains=query) | Q(category__title__icontains=query)
        )


class BlogPostListAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = BlogPost.objects.all().filter(status="published")
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):  # new
        serializer.save(author=self.request.user)


class BlogPostDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = BlogPost.objects.all().filter(status="published")
    serializer_class = BlogPostSerializer
