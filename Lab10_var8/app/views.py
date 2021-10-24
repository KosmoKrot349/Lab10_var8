from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from app.models import Dogs
from app.forms import *


def index(request):
    dogList = Dogs.objects.all()
    context = {
        'dogs':dogList
        }
    return render(request,'index.html',context)

def delete(request,id):
    dogForKill=Dogs.objects.get(id=id)
    dogForKill.delete()

    dogList = Dogs.objects.all()
    context = {
        'dogs':dogList
        }
    return render(request,'index.html',context)

def add(request):
    form=DogForm(request.POST or None)
    if request.method=='GET':
        context= {'form':form}
        return render(request,'AddDog.html',context)
    else:
       
        if form.is_valid():
            form.save()
            dogList = Dogs.objects.all()
            context = {
            'dogs':dogList
            }
            return render(request,'index.html',context)
        else:
            return render(request,'AddDog.html',{'form':form})






