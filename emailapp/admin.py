from django.contrib import admin
from .models import *
# Register your models here.

class EmailAdmin(admin.ModelAdmin): 
    list_display = ('id','from_email','to_email','subject', 'body_text', 'sent_via', 'created')

admin.site.register(Email, EmailAdmin)
