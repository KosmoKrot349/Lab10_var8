from django.urls import path
from app.views import *


urlpatterns=[
    path('',index,name='index'),
    path('delete/<int:id>/',delete,name='delete'),
    path('Add',add,name='Add')
    ]
