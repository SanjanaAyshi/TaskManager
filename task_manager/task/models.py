from django.db import models
from category.models import Category  # Make sure this import is correct


class Tasks(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)
    taskAssignDate = models.DateField()  # Using snake_case for consistency

    def __str__(self):
        return self.title
