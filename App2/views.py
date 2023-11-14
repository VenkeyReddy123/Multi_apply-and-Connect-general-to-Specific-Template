from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def App2(request):
    return render(request,'App2.html')
def App21(request):
    return HttpResponse('<center><h3>This Is App21 Function File </h3></center>')
