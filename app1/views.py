from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout

def asosiy(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddForm(request.POST)
            if form.is_valid():
                animal = form.save(commit=False)
                animal.foydalanuvchi = request.user
                animal.save()
            return redirect('/home/')
        data = {
            'vazifalar': Kundalik.objects.filter(foydalanuvchi=request.user),
            'forma': AddForm()
        }
        return render(request, 'todo (2).html', data)
    return redirect('/')
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

def loginview(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('l'),
                     password=request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/home/')
    return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('/')