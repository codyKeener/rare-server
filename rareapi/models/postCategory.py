from django.db import models
from .category import Category

class PostCategory(models.Model):
  categoryid = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="postcategory")
