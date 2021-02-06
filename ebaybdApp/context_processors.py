
import bangla
import time
from . models import Projects

def contain_date(request):
    bangla_date = bangla.get_date()
    return {'date_bd': bangla_date}
def project(request):
    project_list = Projects.objects.all()
    return {'context_project':project_list}
