from ..models import Pizza
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
