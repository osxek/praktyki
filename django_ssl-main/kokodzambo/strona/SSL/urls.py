from django.urls import path
from . import views

urlpatterns = [
    path('ssl_info/', views.ssl_info_view, name='ssl_info'),
]