from django.shortcuts import render, redirect
from .models import *

def asosiy(request):
    data = {
        'vazifalar': Kundalik.objects.all()
    }
    return render(request, 'todo (2).html', data)

def delete(request, son):
    ish = Kundalik.objects.get(id=son)
    ish.delete()

    return redirect('/home/')
