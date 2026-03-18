from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo.models import Todoo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('eml')
        pwd = request.POST.get('pwd')

        my_user = User.objects.create_user(fnm, emailid, pwd)
        my_user.save()

        user = authenticate(request, username=fnm, password=pwd)
        if user is not None:
            login(request, user)
            return redirect("/todo")

    return render(request, "signup.html")


def login_view(request):
    if request.method == "POST":
        fnm = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(request, username=fnm, password=pwd)
        if user is not None:
            login(request, user)
            return redirect("/todo")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


@login_required(login_url='/login')
def todo_view(request):
    if request.method == "POST":
        if 'add_todo' in request.POST:
            title = request.POST.get('title')
            if title:
                Todoo.objects.create(title=title, description="", user=request.user)

        elif 'toggle' in request.POST:
            todo_id = request.POST.get('todo_id')
            try:
                todo = Todoo.objects.get(id=todo_id, user=request.user)
                todo.completed = not todo.completed
                todo.save()
            except Todoo.DoesNotExist:
                pass

        elif 'delete_todo' in request.POST:
            todo_id = request.POST.get('todo_id')
            try:
                todo = Todoo.objects.get(id=todo_id, user=request.user)
                todo.delete()
            except Todoo.DoesNotExist:
                pass

        return redirect('/todo')

    todos = Todoo.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "todo.html", {'todos': todos})


def logout_view(request):
    logout(request)
    return redirect('/login')