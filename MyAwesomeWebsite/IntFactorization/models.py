from django.db import models
from django.conf import settings


class PrimeHistory(models.Model):
    prime_answer = models.CharField(max_length=9999, null=True)
    prime_input = models.IntegerField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: {self.prime_input} - ({self.prime_answer})"


class KnapsackHistory(models.Model):
    knapsack_answer = models.FloatField(null=True)
    knapsack_input = models.JSONField(blank=True, default=dict())
    knapsack_limit = models.FloatField(blank=True, default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: {self.knapsack_limit} - {self.knapsack_answer}"
