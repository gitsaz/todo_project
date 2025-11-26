from django import forms
from .models import TODO

class TodoForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ("title", "status", 'priority', "date")
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter task title"
            }),
            "status": forms.Select(attrs={
                "class": "form-select"
            }),
            "priority": forms.Select(attrs={
                "class": "form-select"
            }),
            "date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),
        }
        
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_priority(self):
        priority = self.cleaned_data.get('priority')
        if TODO.objects.filter(user=self.user, priority=priority).exists():
            raise forms.ValidationError("You already have a TODO with this priority")
        return priority

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if TODO.objects.filter(user=self.user, title=title).exists():
            raise forms.ValidationError("You already have a TODO with this title")
        return title