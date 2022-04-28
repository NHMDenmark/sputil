from datetime import datetime
from queue import Empty
# import re
from time import strftime
from xmlrpc.client import DateTime 
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect #, JsonResponse
from django.urls import reverse 
# import requests, ssl, sys

from .models import DataSetRow, PreparationType, Session, SpecifyUser, SpCollection, DataSet 
from django.views.generic import ListView 

def index(request):
    print('index')
    userid = request.session.get('userid', -1)
    if userid < 1:        
        context = { }
        logout(request)
    else:
        username = request.session.get('username', 'error')
        if username == 'error':
            context = { }
            logout(request)
        else:
            user = SpecifyUser.objects.get(pk=userid)
            username = user.name
            request.session['username'] = username
            datasets = DataSet.objects.filter(spuser=user)
            collections = SpCollection.objects.all()

#        collections = '[]'
#        url = 'https://specify-test.science.ku.dk/context/login/'
#
#        try:
#            r = requests.get(url, verify=False)
#            print('result: %s' % r)  
#            collections = r.json()['collections']
#        except:
#            print('error fetching url: %s' % sys.exc_info()[0])

            context = {
                'userid' : userid, 
                'username' : username,
                'collections' : collections, 
                'datasets' : datasets,

                }
        
    return render(request, 'spwift/index.html', context)

#def digitize(request):
def digit(request):
    userid = request.session.get('userid', -1)          
    if userid > 0:
        user = SpecifyUser.objects.get(pk=userid)
    else:
        # handle empty user id
        context = { 'error': 'Current user void. Please log in again.' }
        return logout(request, context)
    #set up sticky variables
    preptypeid = -1
    highertaxon = -1
    taxon  = 'incertae sedis'
    region = 'unspecified'
    storage= 'unspecified'

    # TODO diff between POST origin (index or digit)
    post_origin = request.POST.get('post_origin', 'unknown')
    if post_origin == "index":        
        #TODO get form data incl dataset or create new if none selected
        collectionid = int(request.POST.get('collection', -1))
        #request.session['collectionid'] = collectionid
        collection = SpCollection.objects.get(pk=collectionid)
        datasetid = int(request.POST.get('dataset', -1))
        #request.session['datasetid'] = datasetid
        #preptypeid = -1
        if datasetid <= 0: 
            dataset = DataSet(name=user.name + '_' + 
                                    collection.collectioncode + '_' + 
                                    datetime.now().strftime('%Y%m%d_%H%M%S'), 
                              spuser = user,
                              collection = collection, 
                              public = False)
            dataset.save()
            datasetid = dataset.pk
        else:
            dataset = DataSet.objects.get(pk=datasetid)
        
    elif post_origin == "digit":
        #TODO get session and save form data
        datasetid = request.session.get('datasetid', -1)
        collectionid = request.session.get('collectionid', -1)

        if datasetid > 0: 
            dataset = DataSet.objects.get(pk=datasetid)
            if request.POST.get('type','')=='on': type='type'
            else: type=''
            dsrow = DataSetRow(dataset=dataset,
                               datetimecreated=datetime.now(), 
                               type=type,
                               determination=request.POST.get('taxon', 'incertae sedis'),
                               broadgeography=request.POST.get('region', 'unspecified'),
                               storage=request.POST.get('storage', 'unspecified'))
            dsrow.updatename()
            dsrow.save()
            
            taxon = request.POST.get('taxon', 'incertae sedis')
            region = request.POST.get('region', 'unspecified')
            storage = request.POST.get('storage', 'unspecified')

            #TODO handle edits to existing datasetrow
        
    elif post_origin is Empty:
        # handle unknown origin
        context = { 'error': 'Session not initiated. Please try again.' }
        return index(request, context)
    
    if collectionid > 0 and datasetid > 0:
        preptypes = PreparationType.objects.all()
        collections = SpCollection.objects.all()
        
        user = SpecifyUser.objects.get(pk=userid)
        request.session['userid'] = userid
        collection = SpCollection.objects.get(pk=collectionid)
        request.session['collectionid'] = collectionid
        dataset = DataSet.objects.get(pk=datasetid)
        request.session['datasetid'] = datasetid

        context = {
            'userid' : userid, 
            'user' : user,
            'collectionid' : collectionid,
            'collection' : collection,
            'preptypeid' : preptypeid,
            'preptypes' : preptypes,
            'collections' : collections, 
            'datasetid' : datasetid, 
            'dataset_name' : dataset.name, 
            'region' : region,
            'taxon' : taxon, 
            'storage' : storage, 
            'highertaxon' : highertaxon 
            }

        return render(request, 'spwift/digit.html', context)
    else:
        context = { 'error': 'User login session invalid! Please log in again.' }
        return logout(request, context)

def savedatasetrow(request):
    #TODO Alternative path
    userid = request.session.get('userid', -1)
    collectionid = request.session.get('collectionid', -1)

    context = {
            'userid' : userid, 
            #'user' : user,
            'collectionid' : collectionid,
            #'collection' : collection,
            #'preptypeid' : preptypeid,
            #'preptypes' : preptypes,
            #'collections' : collections, 
            #'datasetid' : datasetid, 
            #'dataset_name' : dataset.name 
            }

    return render(request, 'spwift/digit.html', context)
    

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

def dataset(request):
    context = {

    }
    return render(request, 'spwift/dataset.html', context)

def logout(request):
    print('logout')
    try:
        del request.session['userid']
    except:
        print('error on logout')
    return HttpResponseRedirect(reverse('spwift:index', args=()))

class DataSetListView(ListView):
    model = DataSet