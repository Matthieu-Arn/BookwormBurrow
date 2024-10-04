from .models import Bookreview
from django import forms


class BookreviewForm(forms.ModelForm):
    class Meta:
        model = Bookreview
        fields = ('reviewcontent',)