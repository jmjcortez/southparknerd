from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from webapp.serializers.character_serializers import CharacterSerializer
from webapp.models.character import Character


class CharacterViewset(ViewSet):

  def list(self, request):

    characters = list(Character.objects.all())
    
    serializer = CharacterSerializer(characters, many=True)

    data = {
      'characters': serializer.data
    }

    return Response(status=status.HTTP_200_OK, data=data)
    