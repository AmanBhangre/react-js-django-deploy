from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    