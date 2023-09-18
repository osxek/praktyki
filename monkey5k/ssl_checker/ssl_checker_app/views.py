from django.shortcuts import render, get_object_or_404
import os
from django.http import JsonResponse
from .models import SSLCertificate
from .models import Video
import ssl
import socket
import datetime
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import VideoSearchForm
@login_required


def video_list(request):
    media_folder = 'media'
    video_files = [f for f in os.listdir(media_folder) if f.endswith(('.mp4', '.avi', '.mkv'))]
    videos = [{'title': os.path.splitext(video)[0], 'file': f'/{media_folder}/{video}'} for video in video_files]

    form = VideoSearchForm(request.GET)
    search_query = request.GET.get('search_query', '')
    clear_search = request.GET.get('clear_search', '')

    if clear_search:
        search_query = ''
        form = VideoSearchForm()

    if search_query:
        videos = [video for video in videos if search_query.lower() in video['title'].lower()]

    return render(request, 'video_list.html', {'videos': videos, 'form': form, 'search_query': search_query})

def play_video(request, video_name):
    video_folder = 'media' 
    video_path = os.path.join(video_folder, video_name)
    return render(request, 'play_video.html', {'video_path': video_path})




def index(request):
    return render(request, 'index.html')

def ssl_data(request):
    certificates = SSLCertificate.objects.all().order_by('-created_at')
    return render(request, 'ssl_data.html', {'certificates': certificates})

def check_ssl(request):
    if request.method == 'POST':
        domain = request.POST.get('domain')
        try:
            context = ssl.create_default_context()
            with socket.create_connection((domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert(binary_form=True)

            x509_cert = x509.load_der_x509_certificate(cert, default_backend())
            cert_end_date = x509_cert.not_valid_after
            days_left = (cert_end_date - datetime.datetime.now()).days

            ssl_cert = SSLCertificate.objects.create(
                domain=domain,
                valid_until=cert_end_date,
            )
            ssl_cert.save()

            response_data = {
                'success': True,
                'domain': domain,
                'valid_until': cert_end_date.strftime('%Y-%m-%d'),
                'days_left': days_left
            }
        except Exception as e:
            response_data = {
                'success': False,
                'message': str(e)
            }
        return JsonResponse(response_data)
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
