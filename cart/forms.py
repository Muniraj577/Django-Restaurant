from django import forms

DISH_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 16)]


class CartAddDishForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=DISH_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
