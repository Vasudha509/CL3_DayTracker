from django import forms
from .models import ToDoItem, DailyLog, Habit, HabitLog

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['title', 'description', 'completed']  # Specify the fields you want in the form

    # You can add custom validation or clean methods if necessary


class DailyLogForm(forms.ModelForm):
    class Meta:
        model = DailyLog
        fields = ['date', 'mood', 'tasks_completed', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'mood': forms.Select(),
            'tasks_completed': forms.NumberInput(),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'target']

class HabitLogForm(forms.ModelForm):
    class Meta:
        model = HabitLog
        fields = ['habit', 'count', 'date']