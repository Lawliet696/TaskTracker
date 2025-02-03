from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskCreationForm, TaskEditForm

@login_required
def list_tasks(request):
    tasks = Task.objects.exclude(status='completed')
    context = {
        'tasks': tasks,
    }
    return render(request, template_name='tasks/task_list.html', context=context)


@login_required
def completed_list_tasks(request):
    tasks = Task.objects.filter(status='completed')
    context = {
        'tasks': tasks,
    }
    return render(request, template_name='tasks/completed_task_list.html', context=context)

@login_required
def edit_task(request, uuid):
    try:
        task = get_object_or_404(Task, uuid=uuid)
    except:
        raise Http404('Такой задачи нет')

    if request.method == "POST":
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(f'/')

    else:
        form = TaskEditForm(instance=task)
        context = {
            'form': form,
        }
        return render(request, template_name='tasks/task_edit.html', context=context)

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskCreationForm(request.POST)
        form.save()
        return redirect('/')

    else:
        form = TaskCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'tasks/create_task.html', context=context)

@login_required
def detail_task(request, uuid):
    try:
        task = get_object_or_404(Task, uuid=uuid)
    except:
        raise Http404('Такой задачи не существует')

    context = {
        'task': task,
    }
    return render(request, 'tasks/task_detail.html', context=context)

@login_required
def delete_task(request, uuid):
    try:
        task = get_object_or_404(Task, uuid=uuid)
    except:
        raise Http404('Такой задачи не существует')

    task.delete()
    return redirect('/')