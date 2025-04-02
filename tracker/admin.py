from django.contrib import admin
from .models import UserProfile, ToDoItem, DailyLog, Event, Habit, HabitLog, Note

admin.site.register(UserProfile)
admin.site.register(ToDoItem)
admin.site.register(DailyLog)
admin.site.register(Event)
admin.site.register(Habit)
admin.site.register(HabitLog)
admin.site.register(Note)
