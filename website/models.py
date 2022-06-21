from django.db import models


class EmailMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=128)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name
