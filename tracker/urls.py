from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/', views.todo_list, name='todo'),
    path('todo/add/', views.add_task, name='todo_add'),
    path('todo/delete/<int:task_id>/', views.todo_delete, name='todo_delete'),
    path('todo/complete/<int:task_id>/', views.todo_mark_complete, name='todo_mark_complete'),
    path('daily_log/', views.daily_log, name='daily_log'),
    path('dailylog/add/', views.add_daily_log, name='add_daily_log'),
    path('events/', views.event_scheduler, name='event_scheduler'),
    path('events/add/', views.add_event, name='add_event'),    path('habit_tracker/', views.habit_tracker, name='habit_tracker'),
    path('events/confirm_delete/<int:event_id>/', views.confirm_delete, name='confirm_delete'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('habits/', views.habit_tracker, name='habit_tracker'),  # Habit tracker page
    path('habits/add/', views.add_habit, name='add_habit'),  # Add new habit
    path('habits/log/<int:habit_id>/', views.habit_log, name='habit_log'),  # Log habit completion
    path('habits/delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),  # Delete habit

    path('notes/', views.notes, name='notes'),
]
