from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse



# Create your views here.

def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFOD=TopicForm(request.POST)
        if TFOD.is_valid():
            TFOD.save()
            return HttpResponse('Topic data inserted')
    return render(request,'insert_Topic.html',d)


def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}
    if request.method=='POST':
        WFOD=WebpageForm(request.POST)
        if WFOD.is_valid():
            WFOD.save()
            return HttpResponse('Webpage data inserted')  
    return render(request,'insert_webpage.html',d)


def insert_Access(request):
    AFO=AccessForm()
    d={'AFO':AFO}
    if request.method=='POST':
        AFOD=AccessForm(request.POST)
        if AFOD.is_valid():
            AFOD.save()
            return HttpResponse('Access data inserted')  
    return render(request,'insert_Access.html',d)