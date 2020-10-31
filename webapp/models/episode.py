from django.db import models

from webapp.models.character import Character


class EpisodeManager(models.Manager):

  def filter_episodes(self, characters=[], seasons=[], is_classic=False):

    q = self.get_queryset()

    if characters:
      for character in characters:
        q = q.filter(characters__name=character)

    if seasons:
      q = q.filter(season__in=seasons)

    if is_classic:
      # get top 30 percentile so order by tapos top 30 or %10 ng total
      q = q.filter(rating__gte=9.0)    

    return q

class Episode(models.Model):
  season = models.IntegerField()
  title = models.CharField(max_length=200)
  rating = models.FloatField()
  episode_number = models.IntegerField()
  is_sad = models.BooleanField(default=False)
  screenshot_url = models.TextField(null=True, blank=True)
  characters = models.ManyToManyField(Character, blank=True)
  synopsis = models.TextField()
  objects = EpisodeManager()

  def __str__(self):
    return "S{}E{}".format(self.season, self.episode_number)
