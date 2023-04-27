from django.db import models
from account.models import User
from main.models import Product


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Rating(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    value = models.IntegerField(
        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    )


class Favourite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favourites'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='favourites'
    )
