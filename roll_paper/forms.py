from django import forms
from .models import RollPaper

class RollPaperForm(forms.ModelForm):

    class Meta:
        model = RollPaper
        fields = ('title', 'content', 'author', )