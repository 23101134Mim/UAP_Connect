from django.shortcuts import render

# Create your views here.
from django.urls import path
from . import views

urlpatterns = [
    path('routine/', views.routine_list, name='routine_list'),
    path('routine/create/', views.routine_create, name='routine_create'),
    path('routine/update/<int:pk>/', views.routine_update, name='routine_update'),
    path('routine/delete/<int:pk>/', views.routine_delete, name='routine_delete'),
    path('marks/', views.marks_list, name='marks_list'),
]