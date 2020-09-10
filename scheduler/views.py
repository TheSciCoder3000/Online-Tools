from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
import datetime

def sched(request):
    context = {
        'title': 'Calendar'
    }
    return render(request, 'scheduler/sched.html', context=context)

def getTasksData(request):
    if request.method == "POST":
        this_day = int(request.POST['tasks_day'])
        this_month = int(request.POST['tasks_month'])
        this_year = int(request.POST['tasks_year'])

        this_tasks = Task.objects.filter(date=datetime.date(this_year,
                                                         this_month,
                                                         this_day))
        task_dict = {}
        for task in this_tasks:
            task_dict[task.name] = task.completed
        print(this_tasks)
        return JsonResponse({
            'msg': 'success',
            'tasks': task_dict
        })
