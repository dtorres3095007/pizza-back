from ..models import Pizza
from rest_framework import serializers

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = "__all__"
