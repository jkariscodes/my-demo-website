from django.contrib import admin

from .models import EmailMessage


@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)

