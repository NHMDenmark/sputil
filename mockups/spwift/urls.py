from django.urls import path
from . import views
from django.views.generic import RedirectView 
from django.conf.urls import url 
#from spwift.views import DataSetListView

app_name = 'spwift'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
#   path('digitize', views.digit, name='digit'),
    path('digit', views.digit, name='digit'),
#   path('dataset', views.dataset, name='dataset')
#    path('datasets/', DataSetListView.as_view()),
    path('dataset/<int:dataset_id>/', views.dataset, name='dataset'),
    path('taxa', views.TaxonListView.as_view(), name='main-view'),
]