from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post,Rating,Profile
from django.forms.widgets import Textarea

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model = User  
        fields= ['username','email','password1','password2']
        
        help_texts = { 'username': None, 'password2': None, }


User._meta.get_field('email')._unique = True 

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('photo', 'title', 'url', 'description', 'technologies_used',)
        


        