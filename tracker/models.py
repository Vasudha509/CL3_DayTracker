from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  null=False, default=1)  # Link to the User model
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# To-Do List
class ToDoItem(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Link to User
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Daily Log
class DailyLog(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Link to User
    date = models.DateField()
    mood = models.CharField(max_length=50, choices=[
        ('happy', 'Happy'),
        ('neutral', 'Neutral'),
        ('sad', 'Sad'),
        ('fear', 'Fear'),
        ('surprise', 'Surprise'),
        ('anger', 'Anger'),
        ('pride', 'Pride'),
        ('shame', 'Shame')
    ])
    tasks_completed = models.IntegerField(default=0)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Log for {self.date}"



# Event Scheduler
class Event(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Link to User
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} on {self.date}"


# Habit Tracker
class Habit(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Link to User
    name = models.CharField(max_length=100)
    target = models.IntegerField(default=1)  # Target frequency per day
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    count = models.IntegerField(default=0)  # How many times the habit was completed

    def __str__(self):
        return f"{self.habit.name} - {self.date}"


# Notes
class Note(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Link to User
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
