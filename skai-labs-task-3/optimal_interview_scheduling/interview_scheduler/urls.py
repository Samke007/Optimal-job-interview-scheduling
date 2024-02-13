from django.urls import path
from .views import calculate_max_interviews

urlpatterns = [
    path('calculate_max_interviews/', calculate_max_interviews, name='calculate_max_interviews'),
]
