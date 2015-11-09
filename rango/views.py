from django.shortcuts import render

from django.http import HttpResponse
import os
from django.shortcuts import render

# Create your views here.


def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'rango/index.html', context_dict)


def about(request):

    print __file__
    print os.path.dirname(__file__)
    print os.path.dirname(os.path.dirname(__file__))
    print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return HttpResponse("Rango says what about you")