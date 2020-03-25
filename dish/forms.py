from django import forms
from . models import Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DishForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select Category"