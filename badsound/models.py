from django.db import models

class Music(models.Model):
    url = models.URLField(verbose_name="URL")

class Comparison(models.Model):
    music1 = models.ForeignKey(Music, related_name="comparison1")
    music2 = models.ForeignKey(Music, related_name="comparison2")

class Vote(models.Model):
    comparison = models.ForeignKey(Comparison)
    vote = models.ForeignKey(Music)