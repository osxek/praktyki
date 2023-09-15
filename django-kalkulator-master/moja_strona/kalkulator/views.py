from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
@login_required
def kalkulator(request):
    template = loader.get_template('kalk.html')
    return HttpResponse(template.render())
  