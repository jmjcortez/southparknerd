import factory

from webapp.models.character import Character


class CharacterFactory(factory.django.DjangoModelFactory):

  class Meta:
    model = Character

  avatar_url = factory.Faker('text')
  bio = factory.Faker('text')
  name = factory.Faker('name')
  
