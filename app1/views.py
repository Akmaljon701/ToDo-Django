from django.shortcuts import render
from .models import *

def asosiy(request):
    data = {
        'vazifalar': Kundalik.objects.all()
    }
    return render(request, 'todo (2).html', data)
