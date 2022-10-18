from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Kotxeak

def indexkotxeak(request):
  nirekotxeak = Kotxeak.objects.all().values()
  template = loader.get_template('kotxeak_index.html')
  context = {
    'nirekotxeak': nirekotxeak,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('kotxeak_add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['marka']
  y = request.POST['modeloa']
  z = request.POST['matrikula']
  kotxea = Kotxeak(marka=x, modeloa=y, matrikula=z)
  kotxea.save()
  return HttpResponseRedirect(reverse('indexkotxeak'))

def deletekotxeak(request, id):
  member = Kotxeak.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('indexkotxeak'))

def update(request, id):
  nirekotxea = Kotxeak.objects.get(id=id)
  template = loader.get_template('kotxeak_update.html')
  context = {
    'nirekotxea': nirekotxea,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  marka = request.POST['marka']
  modeloa = request.POST['modeloa']
  matrikula = request.POST['matrikula']
  kotxea = Kotxeak.objects.get(id=id)
  kotxea.marka = marka
  kotxea.modeloa = modeloa
  kotxea.matrikula = matrikula
  kotxea.save()
  return HttpResponseRedirect(reverse('indexkotxeak'))