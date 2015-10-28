from django.forms import ModelForm, URLField
from .models import Music, Vote

class AddMusicForm(ModelForm):
    class Meta:
        model = Music
        fields = ['url']

class AddVoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = ['music1', 'music2', 'winner']