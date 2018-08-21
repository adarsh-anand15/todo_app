from django.db import models
from django.utils import timezone

# Create your models here.

#base task class
class task(models.Model):
	title = models.CharField(max_length = 200)
	description = models.TextField(blank=True)
	due_date = models.DateField(default = timezone.now().strftime("%Y-%m-%d"))
	state_choices = ((True, 'Completed'),(False,'Pending'),)
	state = models.BooleanField(choices = state_choices, default = False)
	alert_due_time = models.IntegerField(default = 0)
	class Meta:
		ordering = ["-due_date"] # ordering by due date

	def __str__(self):
		return self.title
