from rest_framework import serializers

from webapp.models.blog import Post, Thread, Comment



class PostSerializer(serializers.ModelSerializer):

  date_posted = serializers.DateTimeField(format="%d %B, %Y")

  class Meta:
    model = Post
    fields = (
      'id','title', 'subtitle', 'author', 'date_posted', 'thumbnail_link', 'content',
    )