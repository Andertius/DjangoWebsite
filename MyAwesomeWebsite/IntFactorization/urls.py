from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prime_fact/', views.prime_fact, name='prime_fact'),
    path('knapsack/', views.knapsack, name='knapsack'),
    path('signup/', views.signup, name='signup'),
]
