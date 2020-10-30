from django.urls import path, include

from rest_framework.routers import DefaultRouter

from webapp.views.blog_views import PostViewset
from webapp.views.character_views import CharacterViewset

router = DefaultRouter()


router.register(r'posts', PostViewset, basename='posts')
router.register(r'characters', CharacterViewset, basename='characters')

urlpatterns = [
  path('', include(router.urls))
]
