from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('ssl_checker_app/', views.index, name='index'),
    path('check_ssl/', views.check_ssl, name='check_ssl'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.home, name='home'),
    path('ssl_data/', views.ssl_data, name='ssl_data'),
    path('videos/', views.video_list, name='video_list'),
    path('videos/play/<str:video_name>/', views.play_video, name='play_video'),
    path('profil/', views.user_profile, name='user_profile'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    
] 

