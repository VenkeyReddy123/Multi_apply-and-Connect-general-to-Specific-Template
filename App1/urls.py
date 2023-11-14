from django.urls import path
from App1.views import *

urlpatterns=[
    path('App11',App11,name='App11'),
    path('App12',App12,name='App12')
]