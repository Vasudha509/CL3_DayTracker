from django.shortcuts import render,get_object_or_404, redirect
from .models import UserProfile, ToDoItem, DailyLog, Event, Habit, HabitLog, Note
from .forms import ToDoForm, DailyLogForm, Habit, HabitLog
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from datetime import date

# Home view
def home(request):
    return render(request, 'tracker/home.html')


# To-Do List Page
def todo_list(request):
    user_profile = UserProfile.objects.get(user=request.user)
    tasks = ToDoItem.objects.filter(user=user_profile)  # Fetch tasks for the logged-in user
    return render(request, 'tracker/todo.html', {'tasks': tasks})

# Add New Task
def add_task(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            # Save the task with the current logged-in user
            task = form.save(commit=False)
            user_profile = UserProfile.objects.get(user=request.user)  # Get the UserProfile for the logged-in user
            task.user = user_profile  # Assign the UserProfile to the task
            task.save()
            return redirect('todo')  # Redirect to the To-Do list page after saving
    else:
        form = ToDoForm()

    return render(request, 'tracker/add_task.html', {'form': form})

# Mark Task as Completed
def todo_mark_complete(request, task_id):
    task = get_object_or_404(ToDoItem, id=task_id)
    task.completed = True  # Mark the task as completed
    task.save()  # Save the change to the database
    return redirect('todo')  # Redirect to the To-Do list page after updating

# Delete Task
def todo_delete(request, task_id):
    task = get_object_or_404(ToDoItem, id=task_id)
    task.delete()  # Delete the task
    return redirect('todo')  # Redirect to the To-Do list page after deleting


# Daily Log List
def daily_log(request):
    # Fetch logs for the logged-in user
    user_profile = get_object_or_404(UserProfile, user=request.user)
    logs = DailyLog.objects.filter(user=user_profile).order_by('-date')
    return render(request, 'tracker/daily_log.html', {'logs': logs})

# Add New Daily Log
@login_required
def add_daily_log(request):
    if request.method == 'POST':
        user_profile = get_object_or_404(UserProfile, user=request.user)
        mood = request.POST.get('mood')
        notes = request.POST.get('notes')
        date = request.POST.get('date')  # Ensure you pass a valid date format from the form
        DailyLog.objects.create(user=user_profile, mood=mood, notes=notes, date=date)
        return redirect('daily_log')
    return render(request, 'tracker/add_daily_log.html')



# Event Scheduler View
def event_scheduler(request):
    events = Event.objects.filter(user=request.user.userprofile).order_by('date', 'start_time')
    return render(request, 'tracker/event_scheduler.html', {'events': events})

# Add Event Page
@login_required
def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        description = request.POST.get('description', '')
        
        # Create a new event
        Event.objects.create(
            user=request.user.userprofile,
            title=title,
            date=date,
            start_time=start_time,
            end_time=end_time,
            description=description
        )
        return redirect('event_scheduler')
    return render(request, 'tracker/add_event.html')

def delete_event(request, event_id):
    # Fetch the event by ID and ensure it belongs to the logged-in user
    event = get_object_or_404(Event, id=event_id, user=request.user.userprofile)
    if request.method == 'POST':
        event.delete()
        return redirect('event_scheduler')
    return render(request, 'tracker/confirm_delete.html', {'event': event})

def confirm_delete(request, event_id):
    # Fetch the event to delete
    event = get_object_or_404(Event, id=event_id, user=request.user.userprofile)
    if request.method == 'POST':
        # If confirmed, delete the event
        event.delete()
        return redirect('event_scheduler')
    return render(request, 'tracker/confirm_delete.html', {'event': event})



# Habit Tracker View
def habit_tracker(request):
    habits = Habit.objects.filter(user=request.user.userprofile)
    return render(request, 'tracker/habit_tracker.html', {'habits': habits})

# Add New Habit
@login_required
def add_habit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        target = request.POST.get('target')
        
        Habit.objects.create(
            user=request.user.userprofile,
            name=name,
            target=target
        )
        return redirect('habit_tracker')
    
    return render(request, 'tracker/add_habit.html')

# Log Habit Completion
@login_required
def habit_log(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user.userprofile)
    if request.method == 'POST':
        count = int(request.POST.get('count', 0))
        log_date = date.today()
        
        # Record the habit completion
        HabitLog.objects.create(
            habit=habit,
            date=log_date,
            count=count
        )
        return redirect('habit_tracker')

    return render(request, 'tracker/habit_log.html', {'habit': habit})

# Delete Habit
@login_required
def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user.userprofile)
    habit.delete()
    return redirect('habit_tracker')

# Notes View
def notes(request):
    user_notes = Note.objects.filter(user=request.user.userprofile)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user.userprofile
        Note.objects.create(user=user, title=title, content=content)
        return redirect('notes')

    return render(request, 'tracker/notes.html', {'notes': user_notes})
