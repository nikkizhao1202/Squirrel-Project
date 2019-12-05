from django import forms
from .models import Squirreldata


class SquirrelForm(forms.ModelForm):
    class Meta:
        model = Squirreldata
        fields = '__all__'
        labels = {"unique_squirrel_id": "Unique_squirrel_id[Hectare-Shift-Date(%m%d)-Squirrel Number]"}