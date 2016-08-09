from django import forms
from django.db import models
from blog.models import Comment, Post, Comment1

class PostModelForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title', 'content', 'lnglat', 'photo']

class CommentModelForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['message', 'author', 'post', 'jjal']

class CommentForm1(forms.Form):
    model=Comment1
    post = forms.ModelChoiceField(queryset=Post.objects.all())
    author = forms.CharField()
    message = forms.CharField()


    def save(self, commit=True):
        comment = Comment1(post=self.cleaned_data['post'], author= self.cleaned_data['author'], message= self.cleaned_data['message'])
        if commit:
            comment.save()
        return comment



class CommentForm(forms.Form):
    author = forms.CharField()
    message = forms.CharField()

    def save(self, commit=True):
        comment = Comment1(author= self.cleaned_data['author'], message= self.cleaned_data['message'])
        if commit:
            comment.save()
        return comment

