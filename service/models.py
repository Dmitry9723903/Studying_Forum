from enum import auto
from tabnanny import verbose
from turtle import title
from django.db import models
from django.forms import DateTimeField
from django.urls import reverse
from django.urls import reverse_lazy

class Post(models.Model):

    title=models.CharField(verbose_name= 'название', max_length=100)
    description=models.TextField(verbose_name= 'описание', null=True, blank=True)
    image=models.ImageField(verbose_name= 'картинка', null=True, blank=True)
    created_at = models.DateTimeField(('created_at'), auto_now_add=True)
    updated_at=models.DateTimeField(('updated_at'), auto_now=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolut_url(self):
        return reverse("index")


class comment(models.Model):
    description=models.TextField(verbose_name= 'описание', null=True, blank=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(('created_at'), auto_now_add=True)

    def __str__(self):
        return f'{self.description}'

    def get_absolut_url(self):
        return reverse("index")
    

class Message(models.Model):
    title = models.CharField(verbose_name= 'Subject', max_length=250, null=True, blank=True)
    body = models.TextField(verbose_name= 'body')

    def __str__(self):
        return f'{self.body}'

    #def get_absolut_url(self):
        #return reverse_lazy("index")


    
    
