from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

class Music(models.Model):
    user = models.ForeignKey(User)
    url = EmbedVideoField(verbose_name="URL")
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = (("user", "created_at"),)

class Comparison(models.Model):
    music1 = models.ForeignKey(Music, related_name="comparison1")
    music2 = models.ForeignKey(Music, related_name="comparison2")
    created_at = models.DateField(auto_now_add=True)

class Vote(models.Model):
    comparison = models.ForeignKey(Comparison)
    vote = models.ForeignKey(Music)
    created_at = models.DateField(auto_now_add=True)