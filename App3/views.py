from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def App3(request):
    return render(request,'App3.html')
    
def App32(request):
    return HttpResponse('<center><h2>This Is App32 Function File</h1></center>')
