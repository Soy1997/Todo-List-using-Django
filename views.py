import json
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Handling todos

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            # Setting priority level
            todo.priority = request.POST.get('priority', 1)  # Default priority level
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'create_todo.html', {'form': form})


def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            # Updating priority level
            todo.priority = request.POST.get('priority', todo.priority)  # Keep existing if not changed
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'update_todo.html', {'form': form, 'todo': todo})
