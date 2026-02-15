from rest_framework import permissions
from django.urls import path
from .views import *

urlpatterns = [
    path('Products/', ProductsView.as_view()),
    path('Tovar/', TovarView.as_view()),
    path('Product_2/', Product_2View.as_view()),
    path('Card_product/', Card_productView.as_view()),
    path('Favourites/', FavouritesView.as_view()),
    path('Order/', OrderView.as_view()),
    path('Contacts/',ContactsView.as_view()),
    path('Feedback/', FeedbackView.as_view()),
    path('Basket/', BasketView.as_view())
]

