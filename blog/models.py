from django.db import models
from django.utils import timezone
from better_auth.models import User

class Tag(models.Model):
    text = models.CharField(max_length=10000, default=None)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    text = models.CharField(max_length=10000)
    created_at = models.DateTimeField(default=timezone.now)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, default=None, null=True)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.title


class PostTagConnect(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)