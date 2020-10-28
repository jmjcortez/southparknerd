import time

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from webapp.serializers.blog_serializers import PostSerializer
from webapp.models.blog import Post


class PostViewset(ViewSet):

  authentication_classes = ()
  permission_classes = ()

  def list(self, request):

    posts = list(Post.objects.all())

    serializer = PostSerializer(posts, many=True)

    data = {
      'posts': serializer.data
    }

    return Response(status=status.HTTP_200_OK, data=data)

  def retrieve(self, request, pk=None):

    posts = Post.objects.all()
    post = get_object_or_404(posts, pk=pk)
    
    serializer = PostSerializer(post)

    return Response(serializer.data)

  @action(detail=False, url_path='latest-post')
  def get_latest_post(self, request):

    latest_post = self._get_latest_post()

    serializer = PostSerializer(latest_post)

    return Response(serializer.data)

  @staticmethod
  def _get_latest_post():
    posts = Post.objects.all()
    return posts.order_by('-date_posted').first()