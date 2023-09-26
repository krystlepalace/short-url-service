from django import forms
from main.models import Tokens


class URLForm(forms.Form):
    class Meta:
        model = Tokens
        fields = ['full_link']
    
    full_link = forms.URLField(widget=forms.URLInput(attrs={
        'class': 'form-control',
        'aria-describedby': "emailHelp",
        'placeholder': "Введите ссылку"
    }))