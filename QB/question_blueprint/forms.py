from .models import Answer
from django import forms


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }