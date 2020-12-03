from .models import *
from rest_framework import serializers


class PrimeFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimeHistory
        fields = ['id', 'prime_input', 'prime_answer', 'user']


class KnapsackSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnapsackHistory
        fields = ['id', 'knapsack_input', 'knapsack_answer', 'user']
