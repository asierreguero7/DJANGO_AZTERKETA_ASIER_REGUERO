from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from alokairuak.models import Alokairuak
from kotxeak.models import Kotxeak
from pertsonak.models import Pertsonak

def index(request):
  nirealokairuak = Alokairuak.objects.all().values()
  nirekotxeak = Kotxeak.objects.all().values()
  nirepertsonak = Pertsonak.objects.all().values()

  template = loader.get_template('alokairuak_index.html')
  context = {
    'nirealokairuak': nirealokairuak,
    'nirepertsonak': nirepertsonak,
    'nirekotxeak': nirekotxeak,
  }
  return HttpResponse(template.render(context, request))