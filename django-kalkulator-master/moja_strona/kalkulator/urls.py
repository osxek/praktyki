
from django.urls import path
from . import views

urlpatterns = [
    path('kalkulator/', views.kalkulator, name='kalkulator'),
]
