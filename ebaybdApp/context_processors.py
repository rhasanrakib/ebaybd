
import bangla
import time
from . models import Projects,Donate,About_Us

def contain_date(request):
    bangla_date = bangla.get_date()
    return {'date_bd': bangla_date}
def project(request):
    project_list = Projects.objects.all()
    return {'context_project':project_list}

def donate(request):
    donate_list = Donate.objects.all()
    return {'context_donate':donate_list}
def aboutus(request):
    about_list = About_Us.objects.all()
    return {'context_aboutus':about_list}
