from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import Http404
from .forms import AddMusicForm, AddVoteForm
from .models import Music, Vote
from datetime import date

def add_music(request):
    if request.method == "POST":
        form = AddMusicForm(request.POST)
        if form.is_valid():
            music = form.save(commit=False)
            music.save()
    menu = [{'url': reverse('add_vote'), 'message': 'Accueil/Vote'}]
    form = AddMusicForm()
    return render(request, 'add_music.html', {'form': form, 'menu': menu})

def add_vote(request):
    menu = [{'url': reverse('add_music'), 'message': 'Ajouter une musique'}]
    if request.method == "POST":
        form = AddVoteForm(request.POST)
        if form.is_valid():
            vote = form.save()
    try:
        music1, music2 = Music.objects.order_by('?')[:2]
        form1 = AddVoteForm(instance=Vote(music1=music1, music2=music2, winner=music1))
        form2 = AddVoteForm(instance=Vote(music1=music1, music2=music2, winner=music2))
        form1.video_url = music1.url
        form2.video_url = music2.url

        return render(request, 'add_vote.html', {'forms': [form1, form2], 'menu': menu})
    except ValueError:
        return render(request, 'add_vote.html', { 'error': 'Pas assez de musiques. Rajoutez en !', 'menu': menu})