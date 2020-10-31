import random

from random import shuffle

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from webapp.serializers.episode_serializers import EpisodeSerializer
from webapp.models.episode import Episode


class EpisodeViewset(ViewSet):

  def list(self, request):

    episodes = list(Episode.objects.all())

    serializer = EpisodeSerializer(episodes, many=True)

    data = {
      'episodes': serializer.data
    }

    return Response(status=status.HTTP_200_OK, data=data)

  @action(detail=False, url_path='random')
  def random(self, request):

    characters = request.query_params.getlist('characters', [])
    seasons = list(map(int, request.query_params.getlist('seasons', [])))
    is_classic = True if request.query_params.get('is_classic', '0') == '1' else False

    episodes = list(Episode.objects.filter_episodes(characters=characters, seasons=seasons, is_classic=is_classic))
    selected_episode = random.choice(episodes) if episodes else []

    if selected_episode:
      serializer = EpisodeSerializer(selected_episode)
      data = serializer.data
    else:
      data = {}
      
    return Response(status=status.HTTP_200_OK, data=data) 