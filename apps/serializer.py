from rest_framework import serializers
from .models import *


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"



class TovarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tovar
        fields = "__all__"



class Product_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_2
        fields = "__all__"



class Card_productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card_product
        fields = "__all__"



class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourites
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"
