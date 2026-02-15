from django.shortcuts import render
from rest_framework import generics
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_data(request):
    data={"message":"Привет фронтенд"}
    return Response(data)



class ProductsView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class TovarView(generics.ListAPIView):
    queryset = Tovar.objects.all()
    serializer_class = TovarSerializer


class Product_2View(generics.ListAPIView):
    queryset = Product_2.objects.all()
    serializer_class = Product_2Serializer


class Card_productView(generics.ListAPIView):
    queryset = Card_product.objects.all()
    serializer_class = Card_productSerializer


class FavouritesView(generics.ListAPIView):
    queryset = Favourites.objects.all()
    serializer_class = FavouritesSerializer


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class =OrderSerializer


class ContactsView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class FeedbackView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class BasketView(generics.ListAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
