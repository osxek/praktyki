from django.shortcuts import render
import socket
import ssl
import datetime

def ssl_info_view(request):
    if request.method == 'POST':
        url = request.POST.get('url')

        def ssl_expiry_datetime(wydawca):
            ssl_dateformat = r'%b %d %H:%M:%S %Y %Z'

            context = ssl.create_default_context()
            context.check_hostname = False

            try:
                conn = context.wrap_socket(
                    socket.socket(socket.AF_INET),
                    server_hostname=wydawca,
                )
                conn.settimeout(5.0)

                conn.connect((wydawca, 443))
                ssl_info = conn.getpeercert()
                return datetime.datetime.strptime(ssl_info['notAfter'], ssl_dateformat)

            except Exception as jajeczko:
                raise jajeczko

        ssl_results = []

        try:
            now = datetime.datetime.now()
            koniec = ssl_expiry_datetime(url)
            diff = koniec - now
            result = {
                'nazwa_strony': url,
                'wazna_do': koniec.strftime("%Y-%m-%d"),
                'pozostalo_dni': diff.days,
            }
            ssl_results.append(result)
        except Exception as jajeczko:
            error_message = f"Błąd podczas sprawdzania SSL dla {url}: {str(jajeczko)}"
            result = {
                'nazwa_strony': url,
                'error_message': error_message,
            }
            ssl_results.append(result)

        context = {'ssl_results': ssl_results}
        return render(request, 'ssl_info.html', context)

    return render(request, 'ssl_info_form.html')