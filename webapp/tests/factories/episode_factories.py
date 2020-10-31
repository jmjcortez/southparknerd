import factory, random

from webapp.models.episode import Episode


class EpisodeFactory(factory.django.DjangoModelFactory):

  class Meta:
    model = Episode

  season = random.randrange(24)
  title = factory.Faker('text')
  rating = 8
  is_sad = False
  episode_number = random.randrange(10)
  synopsis = factory.Faker('text')
