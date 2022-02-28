from rest_framework import generics, status, viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from ..models import  Pizza, Ingredient ,Sale, DetailSale
from django.db.models import Sum,Count
from .serializers import ( PizzaSerializer, PizzaSerializerList,SaleSerializer, SaleSerializerList, IngredientSerializer)
from rest_framework.permissions import IsAuthenticated
import datetime
import json

class PizzaAdd(generics.CreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer 

    def create(self, request, *args, **kwargs):
        super(PizzaAdd, self).create(request, args, kwargs)
        pizza = Pizza.objects.filter(state = 1).order_by('-id')[0]
        print(pizza)
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

class SaleAdd(generics.CreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer 

    def create(self, request, *args, **kwargs):
        super(SaleAdd, self).create(request, args, kwargs)
        sale = Sale.objects.filter(state = 1).order_by('-id')[0]
        pizza = request.data["pizza"]
        detail_add = []
        for i in pizza:
            pizza = Pizza.objects.get(pk = i['id'])
            detail_add.append(DetailSale(pizza = pizza, price = i['price'], sale = sale))
        DetailSale.objects.bulk_create(detail_add)
        return Response({"title": "Venta Guardada"})

class SaleList(generics.ListAPIView):
    queryset = Sale.objects.filter(state = 1)
    serializer_class = SaleSerializerList

    def list(self, request):
        queryset = Sale.objects.filter(state = 1).annotate(total=Count('sale_detail'))
        serializer = SaleSerializerList(queryset, many=True)
        return Response(serializer.data)

class IngredientsPizza(generics.ListAPIView):
    queryset = Ingredient.objects.filter(state = 1)
    serializer_class = IngredientSerializer

    def list(self, request,pk):
        queryset = Ingredient.objects.filter(state = 1, pizza = pk)
        serializer = IngredientSerializer(queryset, many=True)
        return Response(serializer.data)

class Information(generics.ListAPIView):
    def list(self, request):
        pizza = Pizza.objects.filter(state = 1).count()
        sales = DetailSale.objects.filter(state = 1).count()
        client = Sale.objects.filter(state = 1).count()
        return Response({"pizza" : pizza,"sales" : sales,"client" : client})