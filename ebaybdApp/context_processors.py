
import bangla
import time


def contain_date(request):
    bangla_date = bangla.get_date()
    return {'date_bd': bangla_date}
