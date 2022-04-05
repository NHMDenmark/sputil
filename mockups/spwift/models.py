from django.db import models

class SpecifyUser(models.Model):
    spid = models.IntegerField(null=True)
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    # django user ? 

    def __str__(self):
        return self.name

class SpCollection(models.Model):
    spid = models.IntegerField(null=True)
    # spcollectionid = models.BigIntegerField(null=True)
    name = models.CharField(max_length=48)
    # spdisciplineid = models.IntegerField(null=True)
    # spdivisionid = models.IntegerField(null=True)
    # spinstitutionid = models.IntegerField(null=True)
    collectioncode = models.CharField(max_length=12)
    
    def __str__(self):
        return self.collectioncode + ":" + self.name + " [" + str(self.spid) + "] (" + str(self.pk) + ")"

class PreparationType(models.Model):
    spid = models.IntegerField(null=True)
    sppreptypeid = models.IntegerField(null=True)
    name = models.CharField(max_length=64)
    collection = SpCollection()

    def __str__(self):
        return self.name

class Session(models.Model):
    spuser = SpecifyUser()
    startdatetime = models.DateTimeField()
    currentcollection = SpCollection()
    currentpreptype = PreparationType()
    csfrtoken = models.CharField(max_length=64, null=True, blank=True)
    sessionid = models.CharField(max_length=64, null=True, blank=True)

class CollObjectRecord(models.Model):
    spid = models.IntegerField(null=True)
    spcollectionobjectid = models.BigIntegerField(null=True, blank=True)
    barcode = models.CharField(max_length=64, null=True, blank=True)
    catalogNumber = models.CharField(max_length=32, null=True, blank=True)

class DataSet(models.Model):
    spid = models.IntegerField(null=True)
    spuser = SpecifyUser()
    name = models.CharField(max_length=128)
    public = models.BooleanField(null=True)

class DataSetRow(models.Model):
    spid = models.IntegerField(null=True)
    dataset = DataSet()
    datetimecreated = models.DateTimeField(null=True)
    datetimemodified = models.DateTimeField(null=True)


    



