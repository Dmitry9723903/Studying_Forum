from django.contrib import admin
from service.models import Post, comment, Message

admin.site.register(Post)
admin.site.register(comment)
admin.site.register(Message)
