from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['description', 'street', 'colony', 'city', 'postal_code', 'external_number', 'price', 'type', 'wide', 'long', 'ranking', 'image', 'owner']
