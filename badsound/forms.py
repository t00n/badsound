from django.forms import ModelForm, URLField
from .models import Music

class AddMusicForm(ModelForm):
    class Meta:
        model = Music
        fields = ['url']