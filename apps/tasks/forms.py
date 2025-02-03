from django import forms
from .models import Task


class TaskCreationForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'description', 'author', 'executor', 'priority')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off',
            })

class TaskEditForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'description', 'author', 'executor', 'priority', 'status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off',
            })