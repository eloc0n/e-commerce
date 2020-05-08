from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_to_favourite/<str:pk>/', views.add_to_favourite, name='add_to_favourite'),
    path('remove_from_favourite/<str:pk>/', views.remove_from_favourite, name='remove_from_favourite'),
]