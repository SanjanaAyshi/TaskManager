from django.shortcuts import render
from task.models import Tasks


def home(request):
    data = Tasks.objects.all()
    return render(request, 'home.html', {'data': data})
