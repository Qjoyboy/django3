#from os import path
from django.urls import path

from catalog import views
from catalog.views import menu, testik,one

app_name = 'catalog'

urlpatterns = [
    path('', menu),
    path('testik/', testik),
    path('<int:pk>/one/', one, name='one')
]