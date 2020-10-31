from rest_framework import serializers

from webapp.models.episode import Episode
from webapp.serializers.character_serializers import CharacterSerializer


class EpisodeSerializer(serializers.ModelSerializer):

  characters = CharacterSerializer(read_only=True, many=True)

  class Meta:
    model = Episode
    fields = (
      'season', 'title', 'rating', 'episode_number',
      'is_sad', 'screenshot_url', 'characters', 'synopsis', 
    )