from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('primeHistory', views.FactorizeView)
router.register('knapsackHistory', views.KnapsackView)

urlpatterns = [
    path('', views.index, name='index'),
    path('prime_fact/', views.prime_fact, name='prime_fact'),
    path('knapsack/', views.knapsack, name='knapsack'),
    path('signup/', views.signup, name='signup'),
    path('', include(router.urls)),
]
