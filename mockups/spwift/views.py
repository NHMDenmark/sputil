from datetime import datetime
import re
from time import strftime 
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse 
import requests, ssl, sys

from .models import PreparationType, Session, SpecifyUser, SpCollection, DataSet 

def index(request):
    print('index')
    userid = request.session.get('userid', -1)
    if userid < 1:
        logout(request)
        context = { }
    else:
        username = request.session.get('username', 'error')
        if username == 'error':
            user = SpecifyUser.objects.get(pk=userid)
            username = user.name
            request.session.set('username', username)

#        collections = '[]'
#        url = 'https://specify-test.science.ku.dk/context/login/'
#
#        try:
#            r = requests.get(url, verify=False)
#            print('result: %s' % r)  
#            collections = r.json()['collections']
#        except:
#            print('error fetching url: %s' % sys.exc_info()[0])

        collections = SpCollection.objects.all()

        datasets = DataSet.objects.all()
        
        context = {
            'userid' : userid, 
            'username' : username,
            'collections' : collections, 
            'datasets' : datasets,

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

    request.session['username'] = spuser.name 
    request.session['userid'] = spuser.pk
    return HttpResponseRedirect(reverse('spwift:index', args=()))

def logout(request):
    print('logout')
    try:
        del request.session['userid']
    except:
        print('error on logout')
    return HttpResponseRedirect(reverse('spwift:index', args=()))

#def digitize(request):
def digit(request):
    # context = { }
    userid = request.session.get('userid', -1)
    #if userid < 1:
    #    logout(request)
    #else:
    user = SpecifyUser.objects.get(pk=userid)    
    collectionid = int(request.POST.get('collection', -1))
    collection = SpCollection(spid=collectionid)
    datasetid = int(request.POST.get('dataset', -1))
    
    if datasetid <= 0: 
        dataset = DataSet(
                    name=user.name + '_' + 
                    collection.collectioncode + '_' + 
                    datetime.now().strftime('%Y%m%d_%H%M%S'))
        dataset.save()
        datasetid = dataset.pk
    else:
        dataset = DataSet.objects.get(pk=datasetid)
    
        #return render(request, 'spwift/digit.html', context)
#        return digit(request)

#def digit(request):
    #userid = request.session.get('userid', -1)
    #collectionid = request.session.get('collectionid', -1)
    #datasetid = request.session.get('datasetid', -1)

    if userid > 0 and collectionid > 0 and datasetid > 0:
        collection = SpCollection(spid=collectionid)
        user = SpecifyUser.objects.get(pk=userid)
        #collection = SpCollection.objects.get(pk=collectionid)

        preptypes = PreparationType.objects.all()
        collections = SpCollection.objects.all()
        dataset = DataSet.objects.get(pk=datasetid)

        context = {
            'userid' : userid, 
            'user' : user,
            'collectionid' : collectionid,
            'collection' : collection,
            'preptypes' : preptypes,
            'collections' : collections, 
            'datasetid' : datasetid, 
            'dataset_name' : dataset.name 
            }

        return render(request, 'spwift/digit.html', context)
    else:
        return logout(request)
