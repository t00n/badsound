from django.shortcuts import render
from django.core.urlresolvers import reverse
from .forms import AddMusicForm

def add_music(request):
    if request.method == "GET":
        form = AddMusicForm()
    elif request.method == "POST":
        form = AddMusicForm(request.POST)
        if form.is_valid():
            music = form.save(commit=False)
            music.user = request.user
            music.save()
    form.action = reverse('add_music')
    form.method = "POST"
    return render(request, 'add_music.html', {'form': form})