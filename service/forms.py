from tkinter import Widget
from django import forms
from django.forms import ModelForm, fields, widgets
from .models import Post, comment, Message
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(ModelForm):
    class Meta:
        model= Post
        fields="__all__"
        widgets={
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(ModelForm):
    class Meta:
        model= comment
        fields=["description"]
        widgets={
            "description": forms.Textarea(attrs={'class': 'form-control'}),
        }

class MessageForm(ModelForm):
    class Meta:
        model= Message 
        fields=["title", "body"]
        widgets={
            "body": forms.Textarea(attrs={"class": 'form-control'}),
        }

class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2']
