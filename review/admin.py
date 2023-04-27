from django.contrib import admin
from .models import Comment, Rating, Favourite

admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Favourite)

