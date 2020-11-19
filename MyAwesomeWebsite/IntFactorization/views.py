from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import *
from .serializers import *

import math


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


def factorize(request):
    if request == 'GET':
        pass


class FactorizeView(viewsets.ModelViewSet):
    queryset = PrimeHistory.objects.all()
    serializer_class = PrimeFactSerializer


class KnapsackView(viewsets.ModelViewSet):
    queryset = KnapsackHistory.objects.all()
    serializer_class = KnapsackSerializer


def prime_factors(n):
    result = []

    while n % 2 == 0:
        result.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            result.append(i)
            n = n / i

    if n > 2:
        result.append(2)


def knapsack_problem(w, wt, val, n):
    if n == 0 or w == 0:
        return 0

    if wt[n - 1] > w:
        return knapsack_problem(w, wt, val, n - 1)
    else:
        return max(
            val[n - 1] + knapsack_problem(
                w - wt[n - 1], wt, val, n - 1),
            knapsack_problem(w, wt, val, n - 1))
