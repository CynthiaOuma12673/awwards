from django.shortcuts import render
from django.http  import HttpResponseRedirect,Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import  UpdateUserForm, UpdateUserProfileForm, UserRegisterForm,PostForm,RatingForm
from .models import Post, Profile, Rating
import random
# Create your views here.

def index(request):
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(reverse("home"))
    else:
        form = PostForm()
    
    try:
        posts = Post.objects.all()
        posts = posts[::-1]
        post_index = random.randint(0, len(posts)-1)
        random_post = posts[post_index]
        print(random_post.photo)
    except Post.DoesNotExist:
        posts = None
    return render(request, 'all-votes/home.html',{'form':form,'current_user':current_user,'random_post': random_post,'posts':posts})

