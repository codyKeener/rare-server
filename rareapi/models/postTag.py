from django.db import models
from .tag import Tag
# from .post import Post

class PostTag(models.Model):
  
  # postid = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="tagposts")
  tagid = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="posttags")
