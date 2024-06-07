from django.shortcuts import render
from django.http import HttpResponse
from canvas.models import Canvas
from googleclassroom.models import Classroom
from microsoftteams.models import Team
from moodle.models import Course
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    return render(request,'index.html')
@login_required
def canvas(request):
    canvas = Canvas.objects.all()
    return render(request, "canvas.html" ,{'Canvas':canvas})

@login_required
def googleclassroom(request):
    class = Classroom.objects.all()
    return render(request, "googleclassroom.html" ,{'Classroom': class})
@login_required
def microsoftteams(request):
    micro = Team.objects.all()
    return render(request, "microsoftteams.html" ,{'Team': micro})
@login_required
def moodle(request):
    mood = Course.objects.all()
    return render(request, "moodle.html" ,{'Course': mood})
    
@login_required
def forms(request):
    # Your view logic here
    return render(request, 'Canvas_form.html')