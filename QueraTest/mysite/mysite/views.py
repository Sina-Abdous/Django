from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
import datetime


def hello(request):
    return HttpResponse('Hello World')


def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(dict({'current_date': now}))
    return HttpResponse(html)


def hour_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = get_template('hours_ahead.html')
    html = t.render(dict({'hour_offset': offset, 'next_time': dt}))
    return HttpResponse(html)
