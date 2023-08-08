from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    detail = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)