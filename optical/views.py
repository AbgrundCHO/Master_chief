from django.shortcuts import render, reverse
from django.http import HttpResponse
from . import models


# Create your views here.
def homepage(request):
    return render(request, 'index.html')