from django import forms
from haystack.forms import SearchForm


class BasicSearchForm(SearchForm):
    q = forms.CharField(required=False, label='',
                        widget=forms.TextInput(attrs={'type': 'search'}))
