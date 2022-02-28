from django.urls import path
from . import views
from .api.viewsets import PizzaAdd,Pizzalist, SaleAdd,SaleList, IngredientsPizza


urlpatterns = [
    path('pizza/add', PizzaAdd.as_view(), name=None),
    path("pizza", Pizzalist.as_view(), name=None),
    path("pizza/<int:pk>/ingredients", IngredientsPizza.as_view(), name=None),
    path('sale', SaleList.as_view(), name=None),
    path('sale/add', SaleAdd.as_view(), name=None),
]
