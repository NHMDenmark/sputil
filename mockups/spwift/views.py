from datetime import datetime
from queue import Empty
# import re
from time import strftime
from xmlrpc.client import DateTime 
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect #, JsonResponse
from django.urls import reverse 
# import requests, ssl, sys
import json 

from .models import DataSetRow, Discipline, HigherTaxon, PreparationType, SpecifyUser, Collection, DataSet, Taxon # , Session 
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
            collections = Collection.objects.all()

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
    highertaxonid = -1
    collectionid = -1
    taxon  = 'incertae sedis'
    region = 'unspecified'
    storage= 'unspecified'
    datasetrow = DataSetRow()
    datasetrow.determination = 'Incertae sedis'
    datasetrow.broadgeography = 'unspecified'
    datasetrow.storage = 'unspecified'

    # TODO diff between POST origin (index or digit)
    post_origin = request.POST.get('post_origin', 'unknown')
    if post_origin == "index" or post_origin == "dataset":        
        #TODO get form data incl dataset or create new if none selected
        collectionid = int(request.POST.get('collection', -1))
        collection = Collection.objects.get(pk=collectionid)
        datasetid = int(request.POST.get('dataset', -1))
        
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

        #TODO handle content of existing datasetrow
        if post_origin == "dataset":
            datasetrowid = int(request.POST.get('datasetrowid', -1))
            print(datasetrowid)
            if datasetrowid > 0: 
                print('fetch row data')
                datasetrow = DataSetRow.objects.get(pk=datasetrowid)
                if highertaxonid > 0:
                    highertaxon = HigherTaxon.objects.get(pk=highertaxonid)
                # region = datasetrow.broadgeography
                # storage = datasetrow.storage
                datasetrowid = datasetrow.id
        else:
            datasetrowid = -1
        
    elif post_origin == "digit":
        #TODO get session and save form data
        datasetid = request.session.get('datasetid', -1)
        collectionid = request.session.get('collectionid', -1)

        datasetrowid = int(request.POST.get('datasetrowid',-1))

        if datasetid > 0: 
            dataset = DataSet.objects.get(pk=datasetid)
            if request.POST.get('type','')=='on': type='type'
            else: type = ''
            catalognr = request.POST.get('catnr', '')
            barcode = request.POST.get('barcode', '')
            taxon = request.POST.get('taxon', 'incertae sedis')
            region = request.POST.get('region', 'unspecified')
            storage = request.POST.get('storage', 'unspecified')
            preptypeid = request.POST.get('preptype', 'unspecified')
            highertaxonid = int(request.POST.get('highertaxonid', -1))
            saveaction = request.POST.get('save', 'unspecified')

            if datasetrowid < 1:
                datasetrow = DataSetRow(dataset=dataset,
                                datetimecreated=datetime.now(), 
                                type=type,                
                                catalognr=catalognr,
                                barcode=barcode,
                                determination=taxon,
                                broadgeography=region,
                                storage=storage,
                                highertaxonid=highertaxonid)
            else:
                datasetrow = DataSetRow.objects.get(pk=datasetrowid)
                datasetrow.catalognr = catalognr
                datasetrow.barcode = barcode
                datasetrow.type=type
                datasetrow.determination=taxon
                datasetrow.broadgeography=region
                datasetrow.storage=storage
                datasetrow.highertaxonid=highertaxonid
            
            datasetrow.updatename()
            datasetrow.save()
            
            if saveaction == 'savenext':
                datasetrow = DataSetRow(catalognr = '',
                                barcode = '',
                                determination=taxon,
                                broadgeography=region,
                                storage=storage)
                datasetrowid
            elif saveaction == 'savegoback':
                pass
        
    elif post_origin is Empty:
        # handle unknown origin
        context = { 'error': 'Session not initiated. Please try again.' }
        return index(request, context)
    
    if collectionid > 0 and datasetid > 0:
        collections = Collection.objects.all()
        user = SpecifyUser.objects.get(pk=userid)
        request.session['userid'] = userid
        
        collection = Collection.objects.get(pk=collectionid)
        request.session['collectionid'] = collectionid
        
        preptypes = PreparationType.objects.filter(collection=collection)        
        highertaxa = HigherTaxon.objects.filter(discipline=collection.discipline_id)

        dataset = DataSet.objects.get(pk=datasetid)
        request.session['datasetid'] = datasetid
        
        taxa = Taxon.objects.values()
        qs_json = json.dumps(list(taxa))

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
            'datasetrowid' : datasetrow.pk,
            'datasetrow' : datasetrow,
            'region' : region,
            'taxon' : taxon, 
            'storage' : storage, 
            'highertaxonid' : highertaxonid, 
            'highertaxa' : highertaxa, 
            'qs_json' : qs_json
            }

        return render(request, 'spwift/digit.html', context)
    else:
        context = { 'error': 'User login session invalid! Please log in again.' }
        return logout(request, context)

""" def savedatasetrow(request):
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

    return render(request, 'spwift/digit.html', context) """
    

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

def dataset(request, dataset_id):
    userid = request.session.get('userid', -1)
    errormsg = ''
    context = {}
    try:
        dataset = DataSet.objects.get(pk=dataset_id)
        print(dataset.datasetrow_set.count())
        context = {
            'userid' : userid,
            'datasetid' : dataset_id,
            'dataset' : dataset,
            'datasetrows' : dataset.datasetrow_set.all(),
            'error' : errormsg,
            'hidesession' : True,
            'contentwidth' : 12,
        }
    except DataSet.DoesNotExist:
        errormsg = 'No dataset with id %s exists' % dataset_id 
        context = {
            'userid' : userid,
            'datasetid' : dataset_id,
            'error' : errormsg,
            'hidesession' : True,
        }

    return render(request, 'spwift/dataset.html', context)

#class DataSetListView(ListView):
#    model = DataSet

def logout(request):
    print('logout')
    try:
        del request.session['userid']
    except:
        print('error on logout')
    return HttpResponseRedirect(reverse('spwift:index', args=()))


class TaxonListView(ListView):
    model = Taxon
    template_name = 'spwift/taxa.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        taxa = Taxon.objects.values()
        context["qs_json"] = json.dumps(list(taxa))
        return context
