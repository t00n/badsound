from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import Http404
from .forms import AddMusicForm, AddVoteForm, ShowRankingForm
from .models import Music, Vote
from datetime import date
from collections import defaultdict
import operator
import requests
from bs4 import BeautifulSoup

def get_menu():
    return [{'url': reverse('add_vote'), 'message': 'Voter'}, 
            {'url': reverse('add_music'), 'message': 'Ajouter une musique'},
            {'url': reverse('show_music'), 'message': 'Liste des musiques'},
            {'url': reverse('show_ranking'), 'message': 'Classement'}]

def add_music(request):
    if request.method == "POST":
        form = AddMusicForm(request.POST)
        if form.is_valid():
            music = form.save(commit=False)
            url = form.cleaned_data['url']
            title = BeautifulSoup(requests.get(url).text, "html.parser").title.string
            music.title = title
            music.save()
    form = AddMusicForm()
    return render(request, 'add_music.html', {'form': form, 'menu': get_menu()})

def add_vote(request):
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

        return render(request, 'add_vote.html', {'forms': [form1, form2], 'menu': get_menu()})
    except ValueError:
        return render(request, 'add_vote.html', { 'error': 'Pas assez de musiques. Rajoutez en !', 'menu': get_menu()})

def show_ranking(request):
    def expected_score(A, B):
        return 1/(1 + 10**((B-A)/400))
    results = []
    votes = Vote.objects.all()
    if request.method == "POST":
        form = ShowRankingForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data["start_date"]
            end_date = form.cleaned_data["end_date"]
            if start_date != None and end_date != None:
                votes = Vote.objects.filter(created_at__gte=start_date, created_at__lte=end_date)
            elif start_date != None:
                votes = Vote.objects.filter(created_at__gte=start_date)
            elif end_date != None:
                votes = Vote.objects.filter(created_at__lte=end_date)
    ratings = defaultdict(lambda: [1400, ""])
    for v in votes:
        score1 = expected_score(ratings[v.music1.url][0], ratings[v.music2.url][0])
        score2 = expected_score(ratings[v.music2.url][0], ratings[v.music1.url][0])
        ratings[v.music1.url][0] += 32 * ((v.music1 == v.winner) - score1)
        ratings[v.music2.url][0] += 32 * ((v.music2 == v.winner) - score2)
        ratings[v.music1.url][1] = v.music1.title
        ratings[v.music2.url][1] = v.music2.title
    ratings = sorted(ratings.items(), key=operator.itemgetter(1), reverse=True)[:10]
    for (k, v) in ratings:
        results.append(type('Dummy', (object,), { "url": k, "title": v[1], "rating": round(v[0]) }))
    form = ShowRankingForm()
    return render(request, 'show_ranking.html', {'form': form, 'menu': get_menu(), 'results': results})

def show_music(request):
    musics = Music.objects.order_by('title')
    return render(request, 'show_music.html', {'menu': get_menu(), 'musics': musics})