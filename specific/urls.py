from specific.views import *

from django.urls import path

app_name='anime'

urlpatterns=[
    path('sasuke/',sasuke,name='sasuke'),
    path('itachi/',itachi,name='itachi'),

]