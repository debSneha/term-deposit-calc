from django.urls import path
from .views import TermDepositCalculator

urlpatterns = [
    path('', TermDepositCalculator.as_view(), name='calculate')
]