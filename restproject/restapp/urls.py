from django.contrib import admin
from django.urls import path, include
from restapp import views

urlpatterns = [
    path('', views.index_view, name = 'index'),
    path('<int:pk>/', views.detail_view, name = 'detail'),
    path('new/', views.create_new, name = 'create'),
    path('<int:pk>/update/', views.update_view, name = 'update'),
]