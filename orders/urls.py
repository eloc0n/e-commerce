from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('address/', views.address, name='address'),
    path('order/<str:pk>/', views.order, name='order'),
]