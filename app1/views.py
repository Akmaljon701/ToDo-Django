from django.shortcuts import render, redirect
from .models import *
from .forms import *

def asosiy(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home/')
    data = {
        'vazifalar': Kundalik.objects.all(),
        'forma': AddForm()
    }
    return render(request, 'todo (2).html', data)

def delete(request, son):
    ish = Kundalik.objects.get(id=son)
    ish.delete()

    return redirect('/home/')
