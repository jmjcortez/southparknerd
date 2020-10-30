from django.contrib import admin

from webapp.models.blog import Post, Comment, Thread
from webapp.models.character import Character
from webapp.models.episode import Episode


# Register your models here.
admin.site.register(Post)
admin.site.register(Thread)
admin.site.register(Comment)
admin.site.register(Episode)
admin.site.register(Character)
