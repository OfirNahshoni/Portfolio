import django_filters
from django_filters import CharFilter
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import *

class PostFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit Post'))

    headline = CharFilter(field_name='headline', lookup_expr='icontains', label='Headline')
    tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(),
            widget=forms.CheckboxSelectMultiple())
    
    class Meta:
        model = Post
        fields = ['headline', 'tags']