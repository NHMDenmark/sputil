from django.contrib import admin

from .models import SpecifyUser
from .models import Session
#from .models import CollObjectRecord
from .models import SpCollection
from .models import PreparationType
from .models import DataSet
from .models import DataSetRow

admin.site.register(SpecifyUser)
admin.site.register(Session)
#admin.site.register(CollObjectRecord)
admin.site.register(SpCollection)
admin.site.register(PreparationType)
admin.site.register(DataSet)
admin.site.register(DataSetRow)

