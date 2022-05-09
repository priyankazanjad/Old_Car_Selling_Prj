from django import forms
from .models import Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['is_buy']

        widgets = {
            'seller_name': forms.TextInput(attrs={'placeholder': 'Enter Seller Name'}),
            'seller_mobile': forms.TextInput(attrs={'placeholder': '2897654326'}),
            'make': forms.TextInput(attrs={'placeholder': 'Enter Brand of Car'}),
            'model': forms.TextInput(attrs={'placeholder': 'Enter Model of Car'}),
            'year': forms.TextInput(attrs={'placeholder': '2020'}),
            'price': forms.TextInput(attrs={'placeholder': 'Enter Price of Car'}),
        }


