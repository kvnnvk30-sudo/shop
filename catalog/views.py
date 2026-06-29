from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Item

def home(request):
    items = Item.objects.all()
    return render(request, 'catalog/home.html', {'items': items})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('catalog:home')
    else:
        form = RegisterForm()
    return render(request, 'catalog/register.html', {'form': form})