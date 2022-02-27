from django.urls import path
from . import views
from .api.viewsets import PizzaAdd,Pizzalist


urlpatterns = [
    path('pizza/add', PizzaAdd.as_view(), name=None),
    path("pizza", Pizzalist.as_view(), name=None),
]
