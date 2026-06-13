from django import forms
from .models import Todo, Category


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'category', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Vazifa nomi...', 'class': 'form-input'}),
            'description': forms.Textarea(attrs={'placeholder': 'Tavsif (ixtiyoriy)...', 'rows': 3, 'class': 'form-input'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
            'priority': forms.Select(attrs={'class': 'form-input'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'color']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Kategoriya nomi...', 'class': 'form-input'}),
            'color': forms.TextInput(attrs={'type': 'color', 'class': 'form-input color-input'}),
        }
