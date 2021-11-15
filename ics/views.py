from django.shortcuts import render
from icalendar import Calendar, Event
from datetime import datetime, timezone, timedelta
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

def index(request):
    if request.method != 'GET':
        return  HttpResponse('method not allowed.', content_type='application/json', status=405)

    return render(request, 'ics/index.html')

def generate_ics_file(request):
    if request.method != 'POST':
        return  HttpResponse('method not allowed.', content_type='application/json', status=405)

    post_data = request.POST

    cal = Calendar()
    cal.add('prodid', '-//ics generator//')
    cal.add('version', '2.0')

    event = Event()
    event.add('summary', post_data.get('summary'))
    event.add('description', post_data.get('description'))
    event.add('dtstart', datetime.strptime(post_data.get('startTime'), '%Y-%m-%dT%H:%M'))
    event.add('dtend', datetime.strptime(post_data.get('endTime'), '%Y-%m-%dT%H:%M'))
    event.add('dtstamp', datetime.now())

    cal.add_component(event)

    response = HttpResponse(cal.to_ical(), content_type='text/calendar')
    response['Content-Disposition'] = 'attachment; filename=event.ics'

    return response