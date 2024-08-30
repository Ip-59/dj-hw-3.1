from rest_framework import serializers

from main.models import Review, Product



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['product', 'text', 'mark', 'created_at']


class ProductListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'reviews']

    def __str__(self):
        return self.title
    
      



