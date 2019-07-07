"""restproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from restapp.views import MusicView, SingerView, GenreView

music_list = MusicView.as_view({
    'post':'create',
    'get':'list',
})
music_detail = MusicView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})
urlpatterns = format_suffix_patterns(
    [path('admin/', admin.site.urls),
    # url 들어갈 때 주의. 127.0.0.1:8000/admin으로 해야 들어가짐
    # path('restapp/', include('restapp.urls')),
    # url 들어갈 때 주의. 127.0.0.1:8000/restapp으로 해야 들어가짐
    # REST의 조건: 앱 안에 들어가면 안됨.
    path('musics/', music_list),
    path('musics/<int:pk>/', music_detail),
    # path('singers/',),
    # path('genres/', ),
])