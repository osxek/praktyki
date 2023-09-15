from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_ssl/', views.check_ssl, name='check_ssl'),
    path("accounts/", include("django.contrib.auth.urls")),
]

