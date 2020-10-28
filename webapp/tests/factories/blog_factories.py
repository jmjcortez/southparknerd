import factory

from webapp.models.blog import Post


class PostFactory(factory.django.DjangoModelFactory):

  class Meta:
    model = Post

  title = factory.Faker('text')
  subtitle = factory.Faker('text')
  author = factory.Faker('text')
  date_posted = factory.Faker('date')
  thumbnail_link = factory.Faker('text')
  content = factory.Faker('name')
  
