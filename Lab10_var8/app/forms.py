from django import forms
from app.models import Dogs


class DogForm(forms.ModelForm):

    class Meta:
        model=Dogs
        fields=(
            'weight','height','classification','sound','food','name','age'
            )

