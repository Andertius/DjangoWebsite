from django.urls import path, include
from .models import *
from rest_framework import routers, serializers, viewsets


class PrimeFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimeHistory
        fields = ['prime_input', 'prime_answer', 'user']


class KnapsackSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnapsackHistory
        fields = ['knapsack_input', 'knapsack_answer', 'user']
