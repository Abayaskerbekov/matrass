from django.contrib import admin
from . models import *



@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name", "name2", 'visit','image', 'bool1']
    search_fields = ["name", "name2"]
    list_filter = ["name",]



@admin.register(Tovar)
class TovarAdmin(admin.ModelAdmin):
    list_filter = ['name', 'visit', 'name2', 'image', 'bool1']
    list_display = ['name', 'name2', 'image', 'visit', 'bool1']



@admin.register(Product_2)
class Product_2Admin(admin.ModelAdmin):
    list_filter = ['name','name2', 'image', 'visit', 'have','created_at', 'bool1' ]
    list_display = ['name','name2', 'image', 'visit', 'have','created_at', 'bool1'  ]



@admin.register(Card_product)
class Card_productAdmin(admin.ModelAdmin):
    list_filter = ["name", "image", "visit","name2", "text", "price", "image2", "favourites", "basket", "favourites2", "basket2"]
    list_display = ["name", "image", "visit", "name2", "text", "price", "image2", "favourites", "basket", "favourites2", "basket2"]



@admin.register(Favourites)
class FavouritesAdmin(admin.ModelAdmin):
    list_filter = ['name','image','name2','visit','img']
    list_display = ['name','image','name2','visit','img', 'bool1']



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ['name','organization','contact_person','phone','emile','city','street','house','comment','total_price']
    list_display = ['name','organization','contact_person','phone','emile','city','street','house','comment','total_price']



@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_filter = ['discription', 'phone', 'mail']
    list_display = ['discription', 'phone', 'mail']



@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_filter = ['name', 'phone', 'comment']
    list_display = ['name', 'phone', 'comment']



@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_filter = ['product','total', 'name', 'registration']
    list_display = ['product', 'total', 'name', 'registration']
