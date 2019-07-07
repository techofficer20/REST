from django.shortcuts import render
from .models import Music, Singer, Genre
# Create your views here.

def index_view(request):
    musics = Music.objects.all()
    singers = Singer.objects.all()
    genres = Genre.objects.all()
    context = {
        'musics' : musics,
        'singers' : singers,
        'genres' : genres,
    }
    return render(request, 'index.html', context)

def detail_view(request, pk):
    music = Music.objects.get(id=pk)
    context = {'music': music}
    return render(request, 'detail.html', context)