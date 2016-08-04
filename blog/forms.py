from django import forms
from blog.models import Comment, Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title', 'content', 'lnglat']

class CommentModelForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['post', 'message', 'author']

