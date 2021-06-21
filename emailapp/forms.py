from django import forms
from .models import *

#form to add new task 
class EmailForm(forms.ModelForm):
    
    class Meta:
        model = Email
        fields = ['id','from_email','to_email','subject', 'body_text', 'sent_via']                                                          