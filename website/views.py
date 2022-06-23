from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
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

