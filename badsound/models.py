from django.db import models
from embed_video.fields import EmbedVideoField

class Music(models.Model):
    url = EmbedVideoField(verbose_name="URL", unique=True)
    title = models.TextField(verbose_name="Titre")

class Vote(models.Model):
    music1 = models.ForeignKey(Music, related_name="vote1")
    music2 = models.ForeignKey(Music, related_name="vote2")
    winner = models.ForeignKey(Music)
    created_at = models.DateField(auto_now_add=True)