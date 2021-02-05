from django.shortcuts import render
import bangla
import time
# Create your views here.


def home_view(request):
    bangla_date = bangla.get_date()
    return render(request, 'home.html',{'date_bd':bangla_date})


