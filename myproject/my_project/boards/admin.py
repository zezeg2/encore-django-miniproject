from django.contrib import admin
from .models import Post, Board, Favorite, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Board)
admin.site.register(Favorite)
admin.site.register(Comment)