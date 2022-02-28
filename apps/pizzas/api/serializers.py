from ..models import Pizza, Sale,Ingredient
from rest_framework import serializers

class PizzaSerializerList(serializers.ModelSerializer):
    price = serializers.IntegerField(default=0)

    class Meta:
        model = Pizza
        fields = [ "id","image","name","description", "price"]


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = "__all__"

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = "__all__"

class SaleSerializerList(serializers.ModelSerializer):
    total = serializers.IntegerField(default=0)

    class Meta:
        model = Sale
        fields = [ "id","client","phone", "total", "price", "date"]
