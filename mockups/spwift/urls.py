from django.urls import path
from . import views
#from spwift.views import DataSetListView

app_name = 'spwift'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
#   path('digitize', views.digit, name='digit'),
    path('digit', views.digit, name='digit'),
#   path('dataset', views.dataset, name='dataset')
#    path('datasets/', DataSetListView.as_view()),
    path('dataset/<int:dataset_id>/', views.dataset, name='dataset'),
]