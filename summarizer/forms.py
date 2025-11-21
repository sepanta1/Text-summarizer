from django import forms
from .validators import max_words_validator


class SummaryForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea,
        validators=[max_words_validator]    # limit content to 500 words
    )
