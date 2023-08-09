from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    detail = models.CharField(max_length=300)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("sns:post", kwargs={'pk' : self.pk})