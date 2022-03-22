from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse 
import requests, ssl, sys

from .models import Session, SpecifyUser, SpCollection

def index(request):
    print('index')
    session_userid = request.session.get('userid', '')
    collections = '[]'
    url = 'https://specify-test.science.ku.dk/context/login/'

    try:
        r = requests.get(url, verify=False)
        print('result: %s' % r)  
        collections = r.json()['collections']
        #for key in collections:
            #value = collections[key]
            # print("{} : {}".format(value, key))
    except:
        print('error fetching url: %s' % sys.exc_info()[0])

    
    context = {
        'session_userid' : session_userid, 
        'collections' : collections
        }

    return render(request, 'spwift/index.html', context)

def login(request):
    posted_username = request.POST['username']
    print('login attempt: ' + posted_username)
    try:
        spuser = SpecifyUser.objects.get(name=posted_username)
    except SpecifyUser.DoesNotExist:
        print('handling 404')
        response = render(request, 'spwift/index.html', {'username': posted_username, 'error_message':'Specify user "' + posted_username + '" does not exist.'})
        response.delete_cookie('userid')
        return response

    request.session['userid'] = posted_username 
    return HttpResponseRedirect(reverse('spwift:index', args=()))

def logout(request):
    print('logout')
    del request.session['userid']
    return HttpResponseRedirect(reverse('spwift:index', args=()))


def digit(request):
    session_userid = request.session.get('userid', '')
    
    context = {
        'session_userid' : session_userid, 
        # collection
        }

    return render(request, 'spwift/digit.html', context)
