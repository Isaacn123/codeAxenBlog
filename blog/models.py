from email.policy import default
from enum import unique
from random import choices
from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
# Create your models here.

STATUS = (
    (0,'Draft'),
    (1,'Published')
)
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug =  models.SlugField(max_length=200,unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    video_url = models.URLField(max_length=200)
    content_text = models.TextField()
    video_tutorial = EmbedVideoField(default=None)
    status = models.IntegerField(choices= STATUS, default=0)
    update_on = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
