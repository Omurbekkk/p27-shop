from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()

    @property
    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return sum([x.value for x in ratings]) // ratings.count()
        return 0

