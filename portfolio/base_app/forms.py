from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        # For the Tags list - Checkbox instead of just a list
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }