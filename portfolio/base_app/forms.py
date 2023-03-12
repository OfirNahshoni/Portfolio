from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Post

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit Post'))

    class Meta:
        model = Post
        fields = '__all__'
        # For the Tags list (Checkbox instead of just a list)
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }