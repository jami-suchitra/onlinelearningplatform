from django import forms
from .models import Canvas

class CanvasForm(forms.ModelForm):
    class Meta:
         model = Canvas
         fields = ['name','description','width','height','created_at','modified_at']
         widgets = {
             'Canvas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter User_id name'}),
            
}