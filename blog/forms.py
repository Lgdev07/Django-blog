from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment


class NewPostImageForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ['image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)