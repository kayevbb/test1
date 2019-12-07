from django import forms
from .models import Fields


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Fields
        fields = '__all__'