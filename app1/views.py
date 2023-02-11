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

def edit(request, son):
    if request.method == 'POST':
        Kundalik.objects.filter(id=son).update(
        sarlavha=request.POST.get('s'),
        vaqt=request.POST.get('v'),
        malumot=request.POST.get('m'),
        holat=request.POST.get('h')
        )
        return redirect(f"/home/")
    data = {
        'vazifa': Kundalik.objects.get(id=son)
    }
    return render(request, 'todo_edit.html', data)
