from rest_framework.serializers import ModelSerializer
from .models import Category, Product
from review.serializers import CommentSerializer
from .helpers import send_spam

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance: Product):
        rep = super().to_representation(instance)
        rep["rating"] = instance.average_rating
        rep["comments"] = CommentSerializer(
            instance.comments.all(),
            many=True,
            context=self.context
            ).data
        return rep

    def create(self, validated_data):
        product = super().create(validated_data)
        send_spam(product)
        return product


