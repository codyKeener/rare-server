from django.db import models
from .tag import Tag
from .post import Post

class PostTag(models.Model):
  
  post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, related_name="tagposts")
  tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE, null=False, related_name="posttags")
