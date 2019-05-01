from django import forms
from .models import Profile, Trucker


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'pub_date','likes']

class TruckerForm(forms.ModelForm):
    class Meta:
        model = Trucker
        exclude = ['user']
