from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    bio = models.CharField(max_length=400)
    profile_image_url = models.TextField(default="https://www.shutterstock.com/image-vector/avatar-photo-default-user-icon-600nw-2345549599.jpg")
    email = models.CharField(max_length=150)
    created_on = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    is_staff =  models.BooleanField(default=True)
    uid = models.CharField(max_length=50)
