
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import time 
from datetime import datetime, timedelta, timezone, tzinfo

from .models import User, Run, Training

from django.http import JsonResponse
import json 
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


from datetime import date 
import calendar

from django.utils import timezone


from django.urls import reverse
from django.db.models import Min, Max, Sum
from django.shortcuts import redirect

import requests



 # Create your views here.

def index(request):
     return render(request, "running/index.html")

def my_runs(request):
    user = request.user 
    runs = Run.objects.filter(user=user).order_by("-number")
    no_of_runs = len(runs)
    return render(request, "running/my_runs.html", {
        "runs": runs,
        "no_of_runs": no_of_runs
        })
@login_required
def records(request):

    runs = Run.objects.filter(user=request.user).values_list('distance')
    run_max = runs.aggregate(Max('distance'))
    run_distance_max = run_max['distance__max']
    run_dist_max_record = '%.2f' % run_distance_max

    run_total = runs.aggregate(Sum('distance'))
    run_total_record = '%.2f' % run_total['distance__sum']


    paces = Run.objects.filter(user=request.user).values_list('pace')
    pace_min = paces.aggregate(Min('pace'))
    get_pace_min = pace_min['pace__min']
    pace_min_record = '%.2f' % get_pace_min

    longest_run = Run.objects.get(distance=run_dist_max_record)
    no_of_runs = len(Run.objects.filter(user=request.user))
    fastest_run = Run.objects.get(pace=pace_min_record)

    run_times = list(Run.objects.filter(user=request.user).values_list('time'))
   
    total_time = 0 
    for i in run_times:
        print(i)
        split_time = i[0].split(":")
        print(split_time[0])
        print(split_time[1])

        mins = int(split_time[0])

        secs = int(split_time[1])

        total_time = total_time + mins + secs/60
        time_tot = '%.2f' % total_time
        print(total_time)


    return render(request, "running/records.html", {
        
        "run_dist_max_record": run_dist_max_record,
        "run_total_record": run_total_record,
        "pace_min_record": pace_min_record,
        "longest_run": longest_run,
        "no_of_runs":no_of_runs,
        "fastest_run": fastest_run,
        "total_time":total_time,
        "time_tot":time_tot
        })

def add_run(request):

    if request.method=="POST":
        number = request.POST.get("run_number")
        title = request.POST.get("run_title")
        date = request.POST.get("run_date")
        track = request.POST.get("run_track")
        distance = request.POST.get("run_distance")
        time = request.POST.get("run_time")
        pace = request.POST.get("run_pace")

        run = Run.objects.create(user=request.user, number=number, title=title, track=track, distance=distance, time=time, pace=pace, date=date)
        return HttpResponseRedirect(reverse('my_runs'))


def training(request):

    if not Training.objects.filter(user=request.user, week=1, day=1).exists():
        training1_1 = Training.objects.create(user=request.user, week=1, day=1)

    else:
        training1_1 = Training.objects.get(user=request.user, week=1, day=1)

    if not Training.objects.filter(user=request.user, week=1, day=2).exists():
        training1_2 = Training.objects.create(user=request.user, week=1, day=2)

    else:
        training1_2 = Training.objects.get(user=request.user, week=1, day=2)

    if not Training.objects.filter(user=request.user, week=1, day=3).exists():
        training1_3 = Training.objects.create(user=request.user, week=1, day=3)

    else:
        training1_3 = Training.objects.get(user=request.user, week=1, day=3)
#week 2
    if not Training.objects.filter(user=request.user, week=2, day=1).exists():
        training2_1 = Training.objects.create(user=request.user, week=2, day=1)

    else:
        training2_1 = Training.objects.get(user=request.user, week=2, day=1)

    if not Training.objects.filter(user=request.user, week=2, day=2).exists():
        training2_2 = Training.objects.create(user=request.user, week=2, day=2)

    else:
        training2_2 = Training.objects.get(user=request.user, week=2, day=2)

    if not Training.objects.filter(user=request.user, week=2, day=3).exists():
        training2_3 = Training.objects.create(user=request.user, week=2, day=3)

    else:
        training2_3 = Training.objects.get(user=request.user, week=2, day=3)

#week 3
    if not Training.objects.filter(user=request.user, week=3, day=1).exists():
        training3_1 = Training.objects.create(user=request.user, week=3, day=1)

    else:
        training3_1 = Training.objects.get(user=request.user, week=3, day=1)

    if not Training.objects.filter(user=request.user, week=3, day=2).exists():
        training3_2 = Training.objects.create(user=request.user, week=3, day=2)

    else:
        training3_2 = Training.objects.get(user=request.user, week=3, day=2)

    if not Training.objects.filter(user=request.user, week=3, day=3).exists():
        training3_3 = Training.objects.create(user=request.user, week=3, day=3)

    else:
        training3_3 = Training.objects.get(user=request.user, week=3, day=3)

#week 4
    if not Training.objects.filter(user=request.user, week=4, day=1).exists():
        training4_1 = Training.objects.create(user=request.user, week=4, day=1)

    else:
        training4_1 = Training.objects.get(user=request.user, week=4, day=1)

    if not Training.objects.filter(user=request.user, week=4, day=2).exists():
        training4_2 = Training.objects.create(user=request.user, week=4, day=2)

    else:
        training4_2 = Training.objects.get(user=request.user, week=4, day=2)

    if not Training.objects.filter(user=request.user, week=4, day=3).exists():
        training4_3 = Training.objects.create(user=request.user, week=4, day=3)

    else:
        training4_3 = Training.objects.get(user=request.user, week=4, day=3)

#week 5
    if not Training.objects.filter(user=request.user, week=5, day=1).exists():
        training5_1 = Training.objects.create(user=request.user, week=5, day=1)

    else:
        training5_1 = Training.objects.get(user=request.user, week=5, day=1)

    if not Training.objects.filter(user=request.user, week=5, day=2).exists():
        training5_2 = Training.objects.create(user=request.user, week=5, day=2)

    else:
        training5_2 = Training.objects.get(user=request.user, week=5, day=2)

    if not Training.objects.filter(user=request.user, week=5, day=3).exists():
        training5_3 = Training.objects.create(user=request.user, week=5, day=3)

    else:
        training5_3 = Training.objects.get(user=request.user, week=5, day=3)

#week 6
    if not Training.objects.filter(user=request.user, week=6, day=1).exists():
        training6_1 = Training.objects.create(user=request.user, week=6, day=1)

    else:
        training6_1 = Training.objects.get(user=request.user, week=6, day=1)

    if not Training.objects.filter(user=request.user, week=6, day=2).exists():
        training6_2 = Training.objects.create(user=request.user, week=6, day=2)

    else:
        training6_2 = Training.objects.get(user=request.user, week=6, day=2)

    if not Training.objects.filter(user=request.user, week=6, day=3).exists():
        training6_3 = Training.objects.create(user=request.user, week=6, day=3)

    else:
        training6_3 = Training.objects.get(user=request.user, week=6, day=3)

#week 7
    if not Training.objects.filter(user=request.user, week=7, day=1).exists():
        training7_1 = Training.objects.create(user=request.user, week=7, day=1)

    else:
        training7_1 = Training.objects.get(user=request.user, week=7, day=1)

    if not Training.objects.filter(user=request.user, week=7, day=2).exists():
        training7_2 = Training.objects.create(user=request.user, week=7, day=2)

    else:
        training7_2 = Training.objects.get(user=request.user, week=7, day=2)

    if not Training.objects.filter(user=request.user, week=7, day=3).exists():
        training7_3 = Training.objects.create(user=request.user, week=7, day=3)

    else:
        training7_3 = Training.objects.get(user=request.user, week=7, day=3)

#week 8
    if not Training.objects.filter(user=request.user, week=8, day=1).exists():
        training8_1 = Training.objects.create(user=request.user, week=8, day=1)

    else:
        training8_1 = Training.objects.get(user=request.user, week=8, day=1)

    if not Training.objects.filter(user=request.user, week=8, day=2).exists():
        training8_2 = Training.objects.create(user=request.user, week=8, day=2)

    else:
        training8_2 = Training.objects.get(user=request.user, week=8, day=2)

    if not Training.objects.filter(user=request.user, week=8, day=3).exists():
        training8_3 = Training.objects.create(user=request.user, week=8, day=3)

    else:
        training8_3 = Training.objects.get(user=request.user, week=8, day=3)
    
    return render(request, "running/training.html", {
        "training1_1": training1_1,
        "training1_2": training1_2,
        "training1_3": training1_3,
        "training2_1": training2_1,
        "training2_2": training2_2,
        "training2_3": training2_3,
        "training3_1": training3_1,
        "training3_2": training3_2,
        "training3_3": training3_3,
        "training4_1": training4_1,
        "training4_2": training4_2,
        "training4_3": training4_3,
        "training5_1": training5_1,
        "training5_2": training5_2,
        "training5_3": training5_3,
        "training6_1": training6_1,
        "training6_2": training6_2,
        "training6_3": training6_3,
        "training7_1": training7_1,
        "training7_2": training7_2,
        "training7_3": training7_3,
        "training8_1": training8_1,
        "training8_2": training8_2,
        "training8_3": training8_3,


        })

   



@csrf_exempt
def completed_training(request):
    if request.method == "POST":

        # Attempt to sign user in
        week = request.POST["week"]
        day = request.POST["day"]

        training = Training.objects.get(user=request.user, week=week, day=day)
        if training.completed == True:
            training.completed = False
            training.save()
            return redirect('training')
        elif training.completed == False:
            training.completed = True
            training.save()
            return redirect('training')

          


def air(request):
    response=requests.get('https://api.airvisual.com/v2/city?city=Lahore&state=Punjab&country=Pakistan&key=54fe69d5-d16f-4cb9-b4b9-f731fe5a927e').json()
    
    aqi = response['data']['current']['pollution']['aqius']



    return render(request,'running/air.html',{
        'response':response,
        'aqi':aqi
        })
    
def air_js (request):

    response=requests.get('https://api.airvisual.com/v2/city?city=Lahore&state=Punjab&country=Pakistan&key=54fe69d5-d16f-4cb9-b4b9-f731fe5a927e').json()
    aqi = response['data']['current']['pollution']['aqius']

    if request.method == "GET":
        return JsonResponse(aqi, safe=False)

    
 




def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "running/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "running/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "running/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "running/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "running/register.html")
