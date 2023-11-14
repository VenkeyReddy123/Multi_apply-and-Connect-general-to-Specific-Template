from django.urls import path
from App3.views import *

urlpatterns=[
    path('App3/',App3,name='App3'),
    path('App32/',App32,name='App32')
]