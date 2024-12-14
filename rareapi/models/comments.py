# going to need
# author_id --> int this will be a PK of RareUsers (Users)
# post_id --> int this will be a PK of Posts
# content --> varchar
# created_on --> datetime

from django.db import models
from .user import User
from .post import Post 

class Comments(models.Model):

    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='', null='false')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='', null='false')
    content = models.CharField(max_length=250)
    created_on = models.DateField()