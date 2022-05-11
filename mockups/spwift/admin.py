from django.contrib import admin

from .models import Session
from .models import SpecifyUser, Collection, PreparationType, Discipline 
from .models import HigherTaxon, BroadGeographicRegion
from .models import DataSet, DataSetRow

admin.site.register(SpecifyUser)
admin.site.register(Session)
admin.site.register(Collection)
admin.site.register(Discipline)
admin.site.register(PreparationType)
admin.site.register(DataSet)
admin.site.register(DataSetRow)
admin.site.register(HigherTaxon)
admin.site.register(BroadGeographicRegion)

