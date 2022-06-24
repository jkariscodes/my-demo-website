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
    template_name = 'website/home.html'


class AboutPageView(TemplateView):
    template_name = 'website/about.html'


class BlogListView(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'
    template_name = 'website/blog_posts.html'


class BlogDetailView(DetailView):
    model = BlogPost
    context_object_name = 'blog_article'
    template_name = 'website/blog_article.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    context_object_name = 'blog_article_create'
    template_name = 'website/blog_article_create.html'
    fields = ['title', 'body', 'category', 'status']
    success_url = reverse_lazy('blog_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    context_object_name = 'blog_article_update'
    template_name = 'website/blog_article_update.html'
    fields = ['title', 'body', 'category', 'status']
    success_url = reverse_lazy('blog_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        my_obj = self.get_object()
        return my_obj.author == self.request


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    context_object_name = 'blog_article_delete'
    template_name = 'website/blog_article_delete.html'
    success_url = reverse_lazy('blog_posts')

    def test_func(self):
        my_obj = self.get_object()
        return my_obj.author == self.request


class ContactPageView(FormView):
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

