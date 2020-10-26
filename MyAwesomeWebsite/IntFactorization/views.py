from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def index(request):
    context = {
        'title': 'Home Page'
    }
    return render(request, 'IntFactorization/index.html', context)


def prime_fact(request):
    context = {
        'title': 'Prime Factorization'
    }
    return render(request, 'IntFactorization/prime_fact.html', context)


def knapsack(request):
    context = {
        'title': 'Knapsack'
    }
    return render(request, 'IntFactorization/knapsack.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'IntFactorization/signup.html', {'form': form})
