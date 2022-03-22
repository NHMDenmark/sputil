from django.db import models

class SpecifyUser(models.Model):
    # spuserid = models.BigIntegerField() 
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    # django user ? 

    def __str__(self):
        return self.name

class SpCollection(models.Model):
    spcollectionid = models.BigIntegerField()
    name = models.CharField(max_length=64)
    # collectioncode 
    # discipline 

    def __str__(self):
        return self.name

class PreparationType(models.Model):
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
    spcollectionobjectid = models.BigIntegerField(null=True, blank=True)
    barcode = models.CharField(max_length=64, null=True, blank=True)
    catalogNumber = models.CharField(max_length=32, null=True, blank=True)


    



