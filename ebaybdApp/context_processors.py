
import bangla
import time
from . models import Projects, Donate, About_Us, Misc


def contain_date(request):
    bangla_date = bangla.get_date()
    return {'date_bd': bangla_date}


def project(request):
    project_list = Projects.objects.all()
    return {'context_project': project_list}


def donate(request):
    donate_list = Donate.objects.all()
    return {'context_donate': donate_list}


def aboutus(request):
    about_list = About_Us.objects.all()
    return {'context_aboutus': about_list}



def getMisc(request):

    try:
        misc = Misc.objects.first()
     
        return {'getMisc': misc}
    except Exception:
        getMiscs = {
            'about_us': str(Exception),
            'our_works': str(Exception),
            'volunteer_context': str(Exception),
            'image': "",
            'footer_about_us':str(Exception),
            'address': str(Exception),
            'google_map_link': "none",
            'email1': "none",
            'email2': "none",
            'email3': "none",
            'phone1': "none",
            'phone2': "none",
        }
        return {'getMisc': getMiscs}
