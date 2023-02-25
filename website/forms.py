from django.forms import ModelForm
from .models import EmailMessage


class ContactForm(ModelForm):
    class Meta:
        model = EmailMessage
        fields = ["name", "email", "subject", "message"]
