from django.shortcuts import render, redirect
from . import forms
# Create your views here.
from . import models


def addTask(request):
    if request.method == 'POST':
        TaskForm = forms.TaskFrom(request.POST)
        if TaskForm.is_valid():
            TaskForm.save()
            return redirect('add_Task')

    else:
        TaskForm = forms.TaskFrom()
    return render(request, 'addTask.html', {'form': TaskForm})


def edit_Task(request, id):
    task = models.Tasks.objects.get(pk=id)
    taskForm = forms.TaskFrom(instance=task)
    if request.method == 'POST':
        taskForm = forms.TaskFrom(request.POST, instance=task)
        if taskForm .is_valid():
            taskForm .save()
            return redirect('homepage')

    return render(request, 'addTask.html', {'form':  taskForm})


def deleteTask(request, id):
    Task = models.Tasks.objects.get(pk=id)
    Task.delete()
    return redirect('homepage')

