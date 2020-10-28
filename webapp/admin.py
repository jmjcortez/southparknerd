from django.contrib import admin

from webapp.models.blog import Post, Comment, Thread


# Register your models here.
admin.site.register(Post)
admin.site.register(Thread)
admin.site.register(Comment)
