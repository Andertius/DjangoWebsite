from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets

from .serializers import *

import os
import math
import time
import random


def index(request):
    context = {
        'title': 'Home Page',
    }
    return render(request, 'IntFactorization/index.html', context)


@login_required(login_url='/accounts/login/')
def prime_fact(request):
    context = {
        'title': 'Prime Factorization',
    }
    return render(request, 'IntFactorization/prime_fact.html', context)


@login_required(login_url='/accounts/login/')
def knapsack(request):
    context = {
        'title': 'Knapsack',
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
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'IntFactorization/signup.html', {'form': form})


def factorize(request, arg):
    if arg > 100000000000000000000000000000000000000000000000000000000000000000000000000000000:
        PrimeHistory.objects.create(
            prime_answer='',
            prime_input=arg,
            prime_status='failure (code: 400)',
            user=request.user)
        return HttpResponseBadRequest(400)

    result = []

    if request.method == 'GET':
        result = prime_factors(arg)
        PrimeHistory.objects.create(
            prime_answer=str(result)[1:-1],
            prime_input=f'{arg}',
            prime_status='success (code: 200)',
            user=request.user)

    return JsonResponse(result, safe=False)


def execute_knapsack(request):
    result = 0

    if request.method == 'GET':
        if 'arg' in request.GET:
            pass
            # arg = int(request.GET['arg'])
            # result = knapsack_problem(arg)

    return JsonResponse(result, safe=False)


class FactorizeView(viewsets.ModelViewSet):
    queryset = PrimeHistory.objects.all()
    serializer_class = PrimeFactSerializer


class KnapsackView(viewsets.ModelViewSet):
    queryset = KnapsackHistory.objects.all()
    serializer_class = KnapsackSerializer


def prime_factors(number):
    result = []

    while number % 2 == 0:
        result.append(2)
        number /= 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            result.append(int(i))
            number /= i

    if number > 2:
        result.append(int(number))

    return result


def knapsack_problem(w, wt, val, n):
    time.sleep(random.randint(2, 5))

    if n == 0 or w == 0:
        return 0

    if wt[n - 1] > w:
        return knapsack_problem(w, wt, val, n - 1)
    else:
        return max(
            val[n - 1] + knapsack_problem(
                w - wt[n - 1], wt, val, n - 1),
            knapsack_problem(w, wt, val, n - 1))

# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
# n = len(val)
# print
# knapsack_problem(W, wt, val, n)


def prime_history(request):
    queryset = PrimeHistory.objects.filter(user=request.user)

    context = {
        'title': 'Prime History',
        'history': queryset,
    }

    return render(request, 'IntFactorization/prime_history.html', context)
