from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'website/home.html'


class AboutPageView(TemplateView):
    template_name = 'website/about.html'


class BlogPageView(TemplateView):
    template_name = 'website/blog.html'


# class BlogArticlePageView(TemplateView):
#     template_name = 'website/home.html'


class ContactPageView(TemplateView):
    template_name = 'website/contact.html'
