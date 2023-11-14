from django.urls import path
from App2.views import *

urlpatterns=[
    path('App2/',App2,name='App2'),
    path('App21/',App21,name='App21'),
]