from django.db import models
from .category import Category
from .user import User

class Post(models.Model):


    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=80)
    publication_date = models.DateField()
    image_url = models.CharField(max_length=200)
    content = models.TextField(max_length=500)
    approved = models.BooleanField(default=True)
