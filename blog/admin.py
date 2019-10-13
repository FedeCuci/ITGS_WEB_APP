from django.contrib import admin
from .models import Post
from .models import Comment

admin.site.register(Comment)
admin.site.register(Post)
