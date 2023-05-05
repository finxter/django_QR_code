from django.shortcuts import render
from qrcode import make
from django.conf import settings
from time import time
# Create your views here.


def generate_QR_code(request):
    if request.method == 'POST':
        data = request.POST['text']
        img = make(data)
        img_name = f'{str(time())}.png'
        img.save(settings.MEDIA_ROOT + '/' + img_name)
        context = {
            'img_name': img_name
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')

