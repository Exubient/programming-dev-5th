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
    post = forms.ModelChoiceField(queryset=Post.objects.all())
    author = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        super(CommentForm1, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['message'].initial = self.instance.message
            self.fields['author'].initial = self.instance.author
        else:
            self.instance = Comment1()

    def save(self, commit=True):
        self.instance.message = self.cleaned_data['message']
        self.instance.author = self.cleaned_data['author']
        if commit:
            self.instance.save()
        return self.instance



class CommentForm(forms.Form):
    author = forms.CharField()
    message = forms.CharField()

    def save(self, commit=True):
        comment = Comment1(author= self.cleaned_data['author'], message= self.cleaned_data['message'])
        if commit:
            comment.save()
        return comment

class CommentForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    author = forms.CharField()

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        super(CommentForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['message'].initial = self.instance.message
            self.fields['author'].initial = self.instance.author
        else:
            self.instance = Comment()

    def save(self, commit=True):
        self.instance.message = self.cleaned_data['message']
        self.instance.author = self.cleaned_data['author']
        if commit:
            self.instance.save()
        return self.instance
