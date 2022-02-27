from rest_framework import generics, status, viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from ..models import  Pizza, Ingredient
from django.db.models import Sum
from .serializers import ( PizzaSerializer, PizzaSerializerList)
from rest_framework.permissions import IsAuthenticated
import datetime
import json

class PizzaAdd(generics.CreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer 

    def create(self, request, *args, **kwargs):
        super(PizzaAdd, self).create(request, args, kwargs)
        nowDate = str(datetime.datetime.now().strftime('%Y-%m-%d'))
        pizza = Pizza.objects.filter(date_add__icontains=nowDate, state = 1).order_by('-id')[0]
        ingredients = request.data["ingredients"]
        ingredients = json.loads(ingredients)
        ingredients_add = []
        for i in ingredients:
            ingredients_add.append(Ingredient(code=i['code'], name = i['name'], price = i['price'], pizza = pizza))
        Ingredient.objects.bulk_create(ingredients_add)
        return Response({"title": "Pizza Guardada"})

class Pizzalist(generics.ListAPIView):
    queryset = Pizza.objects.filter(state = 1)
    serializer_class = PizzaSerializerList

    def list(self, request):
        queryset = Pizza.objects.filter(state = 1).annotate(price=Sum('pizza_ingredients__price'))
        serializer = PizzaSerializerList(queryset, many=True)
        return Response(serializer.data)
