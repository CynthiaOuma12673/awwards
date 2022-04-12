from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post,Rating,Profile
from django.forms.widgets import Textarea