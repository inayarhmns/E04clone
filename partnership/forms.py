from email.message import Message
from django import forms
from partnership.models import Comment

class ComForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]