"""Platzigram Views"""
#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
import json


def hello_world(request):
    """return a greeting. """
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b, %dth, %Y - %H:%M hrs')
    ))

def hi(request):
    """Hi """
    import pdb; pdb.set_trace()
    return HttpResponse('Hi!')

def sorted(request):
    """numbers order"""
    numbers = [int(i) for i in request.GET['order'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    """ import pdb; pdb.set_trace() """
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )

def personal(request, name, age):
    """Return a greeting"""
    if age < 12 :
        message = 'Sorry {} you are not allowed here'.format(name)
    else:
        message = 'Hello {}! Welcome to Platzigram'.format(name)

    return HttpResponse(message) 
