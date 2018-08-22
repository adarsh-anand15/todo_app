from django.shortcuts import render,redirect
from .models import TodoList
def index(request): #the index view
    todos = TodoList.objects.all() #quering all todos with the object manager
    print(todos[1].status)
    #categories = Category.objects.all() #getting all categories with object manager
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["title"] #title
            due_date = str(request.POST["dueDate"]) #date
            alert_date = str(request.POST["alertDate"])
            #category = request.POST["category_select"] #category
            description = request.POST["description"] #content
            Todo = TodoList(title=title, description=description, due_date=due_date, alert_date=alert_date)
            Todo.save() #saving the todo 
            return redirect("/todo_app/") #reloading the page
        if "taskDone" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.status='Completed'
                todo.save() 
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo
    return render(request, "todo_app/index.html", {"todos": todos})