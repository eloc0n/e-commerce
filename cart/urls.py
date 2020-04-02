from django.urls import path

from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<str:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<str:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart/<str:pk>/', views.update_cart, name='update_cart'),
]