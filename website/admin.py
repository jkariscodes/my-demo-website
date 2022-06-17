from django.contrib import admin

from .models import EmailMessage


class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject')


admin.site.register(EmailMessage, EmailMessageAdmin)
