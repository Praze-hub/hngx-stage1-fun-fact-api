from django.urls import path
from .views import number_fact

urlpatterns = [
    path('api/number/<int:number>/', number_fact, name='number_fact'),
]