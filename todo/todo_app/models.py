from django.db import models
from django.utils import timezone

# Create your models here.

#base task class
class TodoList(models.Model): #Todolist able name that inherits models.Model
    title = models.CharField(max_length=250) # a varchar
    description = models.TextField(blank=True) # a text field 
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    alert_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    #state = models.BooleanField(default = True)
    status = models.CharField(max_length=10, default = "Pending")
    class Meta:
        ordering = ["due_date"] #ordering by the created field
    def __str__(self):
        return self.title #name to be shown when called