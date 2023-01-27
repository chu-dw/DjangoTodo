from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class meta:
        model = Todo
        fields = ('title', 'description', 'important')