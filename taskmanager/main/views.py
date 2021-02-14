from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def delete(request, t_id):
    task = Task.objects.get(id=t_id)
    task.delete()
    return redirect('home')


def update(request, t_id):
    try:
        task = Task.objects.get(id=t_id)

        if request.method == "POST":
            task.title = request.POST.get("title")
            task.task = request.POST.get("task")
            task.save()
            return redirect('home')
        else:
            return render(request, "update.html", {"task": task})
    except Task.DoesNotExist:
        return redirect('home')
