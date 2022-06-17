from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm
from .models import EmailMessage


class HomePageView(TemplateView):
    template_name = 'website/home.html'


class AboutPageView(TemplateView):
    template_name = 'website/about.html'


class BlogPageView(TemplateView):
    template_name = 'website/blog.html'


# class BlogArticlePageView(TemplateView):
#     template_name = 'website/home.html'


class ContactPageView(FormView):
    template_name = 'website/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        email = form.cleaned_data['from_email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        message = EmailMessage(email=email, subject=subject, message=message)
        message.save()
        return super().form_valid(form)


