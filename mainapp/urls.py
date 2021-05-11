from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('basket-page', views.basket_page)
]
