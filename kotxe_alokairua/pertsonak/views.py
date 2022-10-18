from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Pertsonak

def index(request):
  nirepertsonak = Pertsonak.objects.all().values()
  template = loader.get_template('pertsonak_index.html')
  context = {
    'nirepertsonak': nirepertsonak,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('pertsonak_add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['izena']
  y = request.POST['abizena']
  pertsona = Pertsonak(izena=x, abizena=y)
  pertsona.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Pertsonak.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  nirepertsona = Pertsonak.objects.get(id=id)
  template = loader.get_template('pertsonak_update.html')
  context = {
    'nirepertsona': nirepertsona,
  }
  return HttpResponse(template.render(context, request))
  
def updaterecord(request, id):
  izena = request.POST['izena']
  abizena = request.POST['abizena']
  member = Pertsonak.objects.get(id=id)
  member.izena = izena
  member.abizena = abizena
  member.save()
  return HttpResponseRedirect(reverse('index'))