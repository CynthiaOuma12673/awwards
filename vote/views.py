from django.shortcuts import render
from django.http  import HttpResponseRedirect,Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import  UpdateUserForm, UpdateUserProfileForm, UserRegisterForm,PostForm,RatingForm
from .models import Post, Profile, Rating
# Create your views here.
