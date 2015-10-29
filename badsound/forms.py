from django.forms import ModelForm, URLField, DateField, Form
from bootstrap3_datetime.widgets import DateTimePicker
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
    start_date = DateField(required=False, input_formats=['%d/%m/%Y'], widget=DateTimePicker(options={'format': 'DD/MM/YYYY', 'pickTime': False}))
    end_date = DateField(required=False, input_formats=['%d/%m/%Y'], widget=DateTimePicker(options={'format': 'DD/MM/YYYY', 'pickTime': False}))

    def clean(self):
        cleaned_data = super(ShowRankingForm, self).clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        status = cleaned_data.get("status")

        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError(
                    "La date de fin ne peut etre avant la date de debut"
                )