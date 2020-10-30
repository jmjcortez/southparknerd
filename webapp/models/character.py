from django.db import models


class Character(models.Model):
  name = models.CharField(max_length=100)
  bio = models.TextField(null=True, blank=True)
  avatar_url = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.name