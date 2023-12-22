from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('add/', views.addTask, name='add_Task'),
    path('edit/<int:id>', views.edit_Task, name='edit_task'),
    path('delete/<int:id>', views.deleteTask, name='delete_task'),
]
