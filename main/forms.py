from django.forms import ModelForm
from main.models import Product
from django import forms

class StockUpdateForm(forms.Form):
    action = forms.CharField(widget=forms.HiddenInput())

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "image", "author", "year", "publisher", "genre", "description", "rating", "amount"]