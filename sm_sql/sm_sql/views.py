from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('hello world')

def hello_world(request):
    context = {}
    context['hello_world'] = 'Hello World!'
    return render(request,'hello_world.html',context)