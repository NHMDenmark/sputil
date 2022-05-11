from tkinter import CASCADE
from urllib.parse import _NetlocResultMixinStr
from django.db import models

class SpecifyUser(models.Model):
    spid = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    # django user ? 

    def __str__(self):
        return self.name

class Discipline(models.Model):
    spid = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Collection(models.Model):
    spid = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=48)
    discipline = models.ForeignKey(Discipline, on_delete=models.DO_NOTHING, null=True)
    # division
    # institution
    collectioncode = models.CharField(max_length=12)
    
    def __str__(self):
        return self.collectioncode + ":" + self.name + " [" + str(self.spid) + "] (" + str(self.pk) + ")"

class PreparationType(models.Model):
    spid = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=64)
    collection = models.ForeignKey(Collection, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class HigherTaxon(models.Model):
    spid = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=128)
    discipline = models.ForeignKey(Discipline, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return str(self.pk)  + ":" +  self.name + "[" + str(self.spid) + "]"

class BroadGeographicRegion(models.Model):
    spid = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=512)
    # discipline = models.ForeignKey(Discipline, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name

class Session(models.Model):
    spuser = models.ForeignKey(SpecifyUser, on_delete=models.DO_NOTHING)
    startdatetime = models.DateTimeField()
    currentcollection = models.ForeignKey(Collection, on_delete=models.DO_NOTHING)
    currentpreptype = models.ForeignKey(PreparationType, on_delete=models.DO_NOTHING)
    csfrtoken = models.CharField(max_length=64, null=True, blank=True)
    sessionid = models.CharField(max_length=64, null=True, blank=True)
    state = models.CharField(max_length=8, null=True, blank=True)

class DataSet(models.Model):
    spid = models.IntegerField(null=True, blank=True)
    spuser = models.ForeignKey(SpecifyUser, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=128)
    collection = models.ForeignKey(Collection, on_delete=models.DO_NOTHING)
    public = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class DataSetRow(models.Model):
    spid = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    dataset = models.ForeignKey(DataSet, on_delete=models.CASCADE)
    datetimecreated = models.DateTimeField(null=True, blank=True)
    datetimemodified = models.DateTimeField(null=True, blank=True)
    catalognr = models.CharField(max_length=128, null=True, blank=True)
    barcode = models.CharField(max_length=128, null=True, blank=True)
    type = models.CharField(max_length=16, null=True, blank=True)
    determination = models.CharField(max_length=256, null=True, blank=True)
    broadgeography = models.CharField(max_length=65536, null=True, blank=True)
    storage = models.CharField(max_length=65536, null=True, blank=True)
    preptype = models.CharField(max_length=256, null=True, blank=True) #models.ForeignKey(PreparationType, on_delete=models.DO_NOTHING, null=True)
    highertaxon = models.CharField(max_length=256, null=True, blank=True) 

    def updatename(self):
        self.name = 'DataSetRow (' + self.dataset.name + ') '
        if self.catalognr is not None: self.name = self.name + "[" + self.catalognr + "]" 
        else: self.name = self.name + "[]"
        if self.barcode is not None: self.name = self.name + "[" + self.barcode + "]" 
        else: self.name = self.name + "[]"
        if self.determination is not None: self.name = self.name + "[" + self.determination[0:16] + "...]" 
        else: self.name = self.name + "[]"
        if self.broadgeography is not None: self.name = self.name + "[" + self.broadgeography[0:16] + "...]" 
        else: self.name = self.name + "[]"
        if self.storage is not None: self.name = self.name + "[" + self.storage[0:16] + "...]" 
        else: self.name = self.name + "[]"

    def __str__ (self):     
        return self.name 
    
    


    



