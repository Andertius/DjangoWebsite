from django.db import models
from django.conf import settings


class PrimeHistory(models.Model):
    prime_answer = models.CharField(max_length=9999)
    prime_input = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: {self.prime_input} - ({self.prime_answer})"


class KnapsackHistory(models.Model):
    knapsack_answer = models.FloatField()
    knapsack_input = models.JSONField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: {self.knapsack_input} - {self.knapsack_answer}"
