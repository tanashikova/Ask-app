from django import forms
from .models import Answer


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content',)
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }
 

  