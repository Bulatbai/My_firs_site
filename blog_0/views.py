from django.shortcuts import render, HttpResponse
from . import models
def Logic(request):
    choose_all = models.Post.objects.all()
    return  render(request,'index.html', {'post': choose_all}) 


def Logik(request):
    return HttpResponse("<h1>Hello Bill</h1>")






# Create your views here.
