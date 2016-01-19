# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import Post

class post_forms(ModelForm):
    class Meta:
        model = Post
        fields = ['id', 'title', 'message']
        widgets = {'title': forms.TextInput(attrs={'class':"form-control",}),
                   'message': forms.Textarea(attrs={'class':"form-control",})
                   }