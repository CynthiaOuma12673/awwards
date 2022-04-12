from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField

# Create your models here.
# profile class
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(max_length=400, blank=True)
    name = models.CharField(blank=True, max_length=120)
    profile_pic = models.ImageField(upload_to='images/',default='v1639327874/images/default_drurzc.jpg')
    phone_number = PhoneField(max_length=15, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

# post class
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    url = models.URLField(max_length=400)
    photo = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    upload_date = models.DateTimeField(auto_now_add=True, blank=True)
    technologies_used = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.title}'

    def delete_post(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()

    def save_post(self):
        self.save()

class Rating(models.Model):
    rating = (
        (1,'1')
        (2,'2')
        (4,'3')
        (4,'4')
        (5,'5')
        (6,'6')
        (7,'7')
        (8,'8')
        (9,'9')
        (10,'10')
    )