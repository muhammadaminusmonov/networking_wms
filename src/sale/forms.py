from django import forms
from .models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['name', 'amount', 'date']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter date', 'type': 'date'}),
        }