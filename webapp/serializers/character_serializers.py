from rest_framework import serializers

from webapp.models.character import Character


class CharacterSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Character
    fields = (
      'name', 'bio', 'avatar_url',
    )
