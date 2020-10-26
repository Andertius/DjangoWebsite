from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserAcc(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return self.name


class UserHistory(models.Model):
    prime_answer = models.CharField(max_length=9999, null=True, blank=True)
    knapsack_answer = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(UserAcc, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user} {self.prime_answer} {self.knapsack_answer}"
