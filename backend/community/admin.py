from django.contrib import admin
from .models import Board, Favorite, Article, Comment

# Register your models here.
admin.site.register(Board)
admin.site.register(Favorite)
admin.site.register(Article)
admin.site.register(Comment)
