from django.urls import path, include

from rest_framework.routers import DefaultRouter

from webapp.views.blog_views import PostViewset


router = DefaultRouter()


router.register(r'posts', PostViewset, basename='posts')

urlpatterns = [
  path('', include(router.urls))
]
