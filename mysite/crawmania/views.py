from multiprocessing import context
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from crawmania.forms import prizeform
from django.views.generic import ListView
from polls import forms
from .models import PrizeWinners, Reservation
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.views import generic
from django.views.generic.dates import YearArchiveView


def guestlist(request):
    guest= Reservation.objects.all().values()
    template = loader.get_template('crawmania/guestlist.html')
    context= {
        'guest': guest,
    }
    return HttpResponse(template.render(context, request))

def join(request):
  template = loader.get_template('crawmania/join.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['name']
  name = Reservation(name=x)
  name.save()
  return HttpResponseRedirect('http://127.0.0.1:8000/crawmania/')

def about(request):
    template = loader.get_template('crawmania/about.html')
    return HttpResponse(template.render({}, request))

def crawmania(request):
    template = loader.get_template('crawmania/attemp.html')
    return HttpResponse(template.render({}, request))

def reservations(request):
    names_list= Reservation.objects.get(pk=1)
    template= loader.get_template('crawmania/reservation.html')
    context= {
        'names_list': names_list,
        'poob':"poob",
    }
    return HttpResponse(template.render(context,request))

#def prize(response):
    form= prizeform()
    return render(response, "crawmania/prizedisplay.html",{"form":form})

class prizeview(ListView):
    model = PrizeWinners
    context_object_name='year'
    template_name = ('crawmania/prizedisplay.html')
    
    def get_queryset(self):
        mydata=PrizeWinners.objects.values_list('pub_date', flat=True)
        listdata=[]
        for x in mydata:
            if x not in listdata:
                listdata.append(x)
                
        listdata.sort()        
        return listdata
class CrawmaniaYearArchiveView(YearArchiveView):
    queryset = PrizeWinners.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True