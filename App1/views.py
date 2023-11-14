from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def App11(request):
    return render(request,'App1.html')

def App12(request):
    return HttpResponse('<center><h3>This is App11 Function</h3></center>')