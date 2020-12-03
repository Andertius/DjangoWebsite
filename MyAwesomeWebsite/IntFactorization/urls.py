from django.urls import path, include
from . import views
from rest_framework import routers
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register('primeHistory', views.FactorizeView)
router.register('knapsackHistory', views.KnapsackView)

urlpatterns = [
    path('', views.index, name='index'),
    path('prime_fact/', views.prime_fact, name='prime_fact'),
    path('knapsack/', views.knapsack, name='knapsack'),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('signup/', views.signup, name='signup'),
    path('factorize/<int:arg>', views.factorize, name='factorize'),
    path('execute_knapsack/', views.execute_knapsack, name='execute_knapsack'),
    path('prime_history/', views.prime_history, name='prime_history'),

    path('', include(router.urls)),
]
