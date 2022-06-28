from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import EmailMessage, BlogPost
from .forms import ContactForm


class HomePageView(TemplateView):
    """
    Landing page view.
    """
    template_name = 'website/home.html'


class AboutPageView(TemplateView):
    """
    About page template view.
    """
    template_name = 'website/about.html'


class BlogListView(ListView):
    """
    Blog posts/articles view.
    """
    model = BlogPost
    context_object_name = 'blog_posts'
    template_name = 'website/blog_posts.html'
    paginate_by = 4


class BlogDetailView(DetailView):
    """
    Single blog post/article view.
    """
    model = BlogPost
    context_object_name = 'blog_article'
    template_name = 'website/blog_article.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    """
    Create blog post/article view.
    """
    model = BlogPost
    context_object_name = 'blog_article_create'
    template_name = 'website/blog_article_create.html'
    fields = ['title', 'header_image', 'body', 'category', 'status']
    success_url = reverse_lazy('blog_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Blog post edit/update view.
    """
    model = BlogPost
    context_object_name = 'blog_article_update'
    template_name = 'website/blog_article_update.html'
    fields = ['title', 'header_image', 'body', 'category', 'status']
    success_url = reverse_lazy('blog_posts')

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
    context_object_name = 'blog_article_delete'
    template_name = 'website/blog_article_delete.html'
    success_url = reverse_lazy('blog_posts')

    def test_func(self):
        my_obj = self.get_object()
        return my_obj.author == self.request.user


class ContactPageView(FormView):
    """
    Email contact form view.
    """
    template_name = 'website/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['from_email']
        subj = form.cleaned_data['subject']
        msg = form.cleaned_data['message']

        try:
            send_mail(subj, msg, email, ['jkariukidev@email.com'])
            message = EmailMessage(
                name=name, email=email, subject=subj, message=msg
            )
            message.save()
        except BadHeaderError:
            return HttpResponse('Bad header found')
        return super().form_valid(form)


class BlogSearchView(ListView):
    model = BlogPost
    context_object_name = 'blog_search_list'
    template_name = 'website/blog_posts_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return BlogPost.objects.filter(
            Q(title__icontains=query) | Q(category__title__icontains=query)
        )


