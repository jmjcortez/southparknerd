from django.urls import path, include

from rest_framework.routers import DefaultRouter

from webapp.views.blog_views import PostViewset
from webapp.views.character_views import CharacterViewset
from webapp.views.episode_views import EpisodeViewset

router = DefaultRouter()


router.register(r'posts', PostViewset, basename='posts')
router.register(r'characters', CharacterViewset, basename='characters')
router.register(r'episodes', EpisodeViewset, basename='episodes')

urlpatterns = [
  path('', include(router.urls))
]
