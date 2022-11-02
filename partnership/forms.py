from email.message import Message
from django import forms
from partnership.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]