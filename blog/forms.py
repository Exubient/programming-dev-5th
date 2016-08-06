from django import forms
from blog.models import Comment, Post, Comment1

class PostModelForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title', 'content', 'lnglat']

class CommentModelForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['message', 'author', 'post']

class CommentForm(forms.Form):
    author = forms.CharField()
    message = forms.CharField()

    def save(self, commit=True):
        comment = Comment1(author= self.cleaned_data['author'], message= self.cleaned_data['message'])
        if commit:
            comment.save()
        return comment

