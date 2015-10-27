from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import Http404
from .forms import AddMusicForm, AddVoteForm
from .models import Comparison, Music, Vote
from datetime import date

def add_music(request):
    if request.method == "GET":
        form = AddMusicForm()
    elif request.method == "POST":
        form = AddMusicForm(request.POST)
        if form.is_valid():
            music = form.save(commit=False)
            music.user = request.user
            music.save()
            musics = Music.objects.filter(created_at=date.today())
            if len(musics) == 2:
                comparison = Comparison()
                comparison.music1 = musics[0]
                comparison.music2 = musics[1]
                comparison.save()
    form.action = reverse('add_music')
    form.method = "POST"
    return render(request, 'add_music.html', {'form': form})

def add_vote(request):
    if request.method == "GET":
        form1 = AddVoteForm()
        form2 = AddVoteForm()
        try:
            comparison = Comparison.objects.order_by('-pk')[0]
            form1 = AddVoteForm(instance=Vote(comparison=comparison, vote=comparison.music1))
            form2 = AddVoteForm(instance=Vote(comparison=comparison, vote=comparison.music2))
            return render(request, 'add_vote.html', {'form1': form1, 'form2': form2})
        except IndexError:
            raise Http404
    elif request.method == "POST":
        form = AddVoteForm(request.POST)
        if form.is_valid():
            vote = form.save()