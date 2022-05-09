from django import forms
from .models import Enquiry

class EnquiryModelForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Buyer Name'}),
            'mobile': forms.TextInput(attrs={'placeholder': '2897654326'}),
        }