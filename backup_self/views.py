from django.shortcuts import render, redirect
from .models import task
from django.http import HttpResponse

# Create your views here.

def index(request):
	all_tasks = task.objects.all() # quering all task with the object manager
	if request.method == "POST":
		if "taskAdd" in request.POST:
			title = request.POST["title"]
			due_date = str(request.POST["due_date"])
			state = request.POST["state"]
			description = title + " -- " + due_date + " " + status
			alert_due_time =request.POST["alert_due_time"]

			task_todo = task(title=title, due_date = due_date, state = state, description = description, alert_due_time = alert_due_time)
			task_todo.save()
			return redirect("/")

		if "taskDelete" in request.POST:
			checkedlist = request.POST["checkedbox"]

			for task_id in checkedlist:
                task_to_del = task.objects.get(id=int(task_id)
                task_to_del.delete()

    return render(request, "index.html",{"tasks":all_tasks})