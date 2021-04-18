from django import forms
from .models import Post, Comment
from django.forms import widgets

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =[
            'belong',
            'title',
            'content',
            'image',
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]
        widgets = {
            'text':forms.Textarea(attrs={'rows':2}),
        }