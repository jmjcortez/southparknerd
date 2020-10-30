from django.db import models

from webapp.models.character import Character


class Episode(models.Model):
  season = models.IntegerField()
  title = models.CharField(max_length=200)
  rating = models.FloatField()
  episode_number = models.IntegerField()
  is_sad = models.BooleanField(default=False)
  screenshot_url = models.TextField(null=True, blank=True)
  characters = models.ManyToManyField(Character)

  def __str__(self):
    return "S{}E{}".format(self.season, self.episode_number)