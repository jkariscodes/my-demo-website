from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    from_email = forms.EmailField(max_length=254, required=True)
    subject = forms.CharField(max_length=128, required=True)
    message = forms.CharField(max_length=500, widget=forms.Textarea, required=True)
