import uuid
from django.db import models


class Post(models.Model):
  title = models.CharField(max_length=100)
  subtitle = models.CharField(max_length=150)
  author = models.CharField(max_length=30)
  date_posted = models.DateTimeField(auto_now=True)
  thumbnail_link = models.CharField(max_length=200)
  content = models.TextField()
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Thread(models.Model):
  post = models.ForeignKey(
    Post,
    on_delete=models.PROTECT,
    related_name="post_threads"
  )

class Comment(models.Model):
  is_parent = models.BooleanField()
  date_posted = models.DateTimeField()
  content = models.TextField()
  avatar_url = models.CharField(max_length=100)
  poster = models.CharField(max_length=100)
  thread = models.ForeignKey(
    Thread, 
    on_delete=models.PROTECT,
    related_name="thread_comments"
  )
