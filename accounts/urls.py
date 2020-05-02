from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('add_to_favourite/<str:pk>/', views.add_to_favourite, name='add_to_favourite'),
]