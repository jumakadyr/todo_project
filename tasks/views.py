import logging

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.utils import timezone
from .models import Task
from account.models import User
from .forms import CreateTaskForm
from django.db.models import Q



def profile(request):
    return render(request, 'account/profile.html')


@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user).order_by('deadline')
    # tasks = request.user.tasks.all.order_by('deadline')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def task_create(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.created_at = timezone.now()
            task.save()
            return redirect('tasks:task-list')
    else:
        form = CreateTaskForm(user=request.user)
    return render(request, 'tasks/task_create.html', {'form': form})

logger = logging.getLogger(__name__)

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if task.owner != request.user:
        logger.warning(f"User {request.user} attempted to edit task {task.pk}, but does not own it.")
        return HttpResponseForbidden("Вы не можете редактировать эту задачу.")

    if request.method == "POST":
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            logger.info(f"User {request.user} successfully edited task {task.pk}.")
            return redirect('tasks:task-list')
    else:
        form = CreateTaskForm(instance=task)

    return render(request, 'tasks/task_edit.html', {'form': form, 'task': task})
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('tasks:task-list')

@login_required
def task_complete(request):
    tasks = Task.objects.filter(status="Done", owner=request.user)
    return render(request, "tasks/task_completed.html", {"tasks": tasks})



def home(request):
    query = request.GET.get('q', '')
    sort_by = request.GET.get('sort', 'deadline')

    tasks = Task.objects.all()

    if query:
        tasks = tasks.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(status__icontains=query) |
            Q(priority__icontains=query)
        )

    tasks = tasks.order_by(sort_by)

    status = request.GET.get('status')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')

    if status:
        tasks = tasks.filter(status=status)
    if priority:
        tasks = tasks.filter(priority=priority)
    if deadline:
        today = timezone.now().date()
        if deadline == 'overdue':
            tasks = tasks.filter(deadline__date__lt=today)
        elif deadline == 'today':
            tasks = tasks.filter(deadline__date=today)
        elif deadline == 'week':
            week_end = today + timezone.timedelta(days=7)
            tasks = tasks.filter(deadline__date__gte=today, deadline__date__lt=week_end)

    if sort_by in ['deadline', 'priority', 'status', 'created_at']:
        tasks = tasks.order_by(sort_by)
    elif sort_by == '-deadline':
        tasks = tasks.order_by('-deadline')

    context = {'tasks': tasks,
               'status_filter': request.GET.get('status'),
               'priority_filter': request.GET.get('priority'),
               'deadline_filter': request.GET.get('deadline'),
               'sort_by': request.GET.get('sort', 'deadline'),
               'now': timezone.now()
               }
    return render(request, 'tasks/index.html', context)
