from django.shortcuts import render
from django.http import JsonResponse
from .models import Task, scheduleObject
import json
import operator
import datetime

def sched(request):
    context = {
        'title': 'Calendar',
    }
    return render(request, 'scheduler/sched.html', context=context)

def createTask(request):
    if request.method == "POST":
        task_instance = Task()
        task_instance.name = request.POST['taskName']
        task_instance.details = request.POST['taskDetail']
        year, month, day = request.POST['taskDate'].split('-')
        task_instance.date = datetime.date(int(year), int(month), int(day))
        task_instance.owner = request.user
        task_instance.save()

        return JsonResponse({
            'msg': 'success'
        })

def removeTask(request):
    if request.method == "POST":
        taskName = request.POST['taskName']
        year, month, day = request.POST['taskDate'].split("-")

        Task.objects.get(name=taskName, date=datetime.date(int(year), int(month), int(day))).delete()

        return JsonResponse({
            'msg': 'success'
        })

def getTasksData(request):
    if request.method == "POST":
        this_day = int(request.POST['tasks_day'])
        this_month = int(request.POST['tasks_month'])
        this_year = int(request.POST['tasks_year'])
        task_dict = {}

        if int(request.POST.get("task_view")) == 0:
            this_tasks = Task.objects.filter(owner=request.user,
                                             date=datetime.date(this_year,
                                                                this_month,
                                                                this_day)).order_by('completed')
            for task in this_tasks:
                task_dict[task.name] = task.completed
        elif int(request.POST.get("task_view")) == 1:
            this_tasks = Task.objects.filter(completed=False, owner=request.user).order_by('date')
            for task in this_tasks:
                task_dict[task.name] = "{}/{}/{}".format(task.date.month,
                                                         task.date.day,
                                                         task.date.year)

        return JsonResponse({
            'msg': 'success',
            'tasks': task_dict
        })

def updateTasks(request):
    if request.method == "POST":
        TaskList = json.loads(request.POST['newtaskList'])
        print(TaskList)
        for key in TaskList:
            year, month, day = TaskList[key][1].split("-")
            task_date = datetime.date(int(year), int(month), int(day))
            task_instance = Task.objects.get(name=key, date=task_date)
            task_instance.completed = TaskList[key][0]
            task_instance.save()

        return JsonResponse({
            'msg':'success'
        })

def getDaySchedule(request):
    if request.method == 'POST':
        weekday = request.POST['weekday']
        subjectsObj = scheduleObject.objects.filter(weekday__icontains=weekday).order_by('time')
        subj_dict = {}
        for subj in subjectsObj:
            hr, min, sec = str(subj.time).split(":")
            set = 'am'
            if int(hr) > 12:
                hr = int(hr) - 12
                set = 'pm'
            subj_dict[subj.name] = [str(hr), min, set]

        #subj_dict = sorted(subj_dict.values(), key=operator.itemgetter(0))

        return JsonResponse({
            'msg': 'success',
            'subjects': subj_dict
        })
