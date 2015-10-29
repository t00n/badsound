from django.forms import ModelForm, URLField, DateField, Form
from .models import Music, Vote

class AddMusicForm(ModelForm):
    class Meta:
        model = Music
        fields = ['url']

class AddVoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = ['music1', 'music2', 'winner']

class ShowRankingForm(Form):
    start_date = DateField(required=False)
    end_date = DateField(required=False)