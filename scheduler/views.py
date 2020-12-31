from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Task, scheduleObject
import json
import operator
import datetime

def sched(request):
    if request.user.is_authenticated:
        context = {
            'title': 'Calendar',
        }
        return render(request, 'scheduler/sched.html', context=context)

    else:
        return redirect('login')

def createTask(request):
    if request.method == "POST":
        if Task.objects.filter(name=request.POST['name']).exists():
            return JsonResponse({
                'msg': 'name repeated'
            })

        task_instance = Task()
        task_instance.name = request.POST['name']
        task_instance.details = request.POST['details']
        year, month, day = request.POST['date'].split('-')
        task_instance.date = datetime.date(int(year), int(month), int(day))
        task_instance.owner = request.user
        task_instance.save()

        return JsonResponse({
            'msg': 'success'
        })

def removeTask(request):
    if request.method == "POST":
        taskName = request.POST['task_name']
        year, month, day = request.POST['task_date'].split("-")

        Task.objects.get(owner=request.user,
                         name=taskName,
                         date=datetime.date(int(year), int(month), int(day))).delete()

        return JsonResponse({
            'msg': 'success'
        })

def getTasksData(request):
    if request.method == "GET":
        data_task_list = []
        # If view Mode 1, send all unfinished Tasks
        if request.GET['view_mode'] == '0':
            UFTasks = Task.objects.filter(completed=False,
                                          owner=request.user).order_by("date")
            for task in UFTasks:
                data_task_list.append([task.name, task.completed,
                                       task.date, task.details])

        elif request.GET['view_mode'] == '1':
            month, day, year = request.GET['task_date'].split("/")

            date_tasks = Task.objects.filter(owner=request.user,
                                             date=datetime.date(int(year),
                                                                int(month),
                                                                int(day))).order_by('date')
            for task in date_tasks:
                data_task_list.append([task.name, task.completed,
                                       task.date, task.details])

        return JsonResponse({
            'msg': 'success',
            'task_data': data_task_list
        })


def updateTasks(request):
    if request.method == "POST":
        TaskList = json.loads(request.POST['tasks_list'])
        for task in TaskList:
            print(task)
            year, month, day = task[1].split("-")
            task_date = datetime.date(int(year), int(month), int(day))
            task_instance = Task.objects.get(name=task[0], date=task_date)
            task_instance.completed = task[2]
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
            subj_dict[subj.name] = [str(hr), min, set, subj.links]

        #subj_dict = sorted(subj_dict.values(), key=operator.itemgetter(0))

        return JsonResponse({
            'msg': 'success',
            'subjects': subj_dict
        })
