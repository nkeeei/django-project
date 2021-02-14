from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, SelectDateWidget, SplitDateTimeField

from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "date"]
        widgets = {"title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
        }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'}),
            "date": SelectDateWidget(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1',
                })

        }
