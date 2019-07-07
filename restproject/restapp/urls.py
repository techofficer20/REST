from django.contrib import admin
from django.urls import path, include
from restapp import views

urlpatterns = [
    path('', views.index_view, name = 'index'),
    path('<int:pk>/', views.detail_view, name = 'detail'),
]