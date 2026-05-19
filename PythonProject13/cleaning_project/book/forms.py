from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'address', 'service', 'date', 'time']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border p-3 rounded-lg',
                'placeholder': 'Your Name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full border p-3 rounded-lg',
                'placeholder': 'Phone Number'
            }),
            'address': forms.Textarea(attrs={
                'class': 'w-full border p-3 rounded-lg',
                'placeholder': 'Your Address',
                'rows': 3
            }),
            'service': forms.Select(attrs={
                'class': 'w-full border p-3 rounded-lg'
            }),
            'date': forms.DateInput(attrs={
                'class': 'w-full border p-3 rounded-lg',
                'type': 'date'
            }),
            'time': forms.TimeInput(attrs={
                'class': 'w-full border p-3 rounded-lg',
                'type': 'time'
            }),
        }