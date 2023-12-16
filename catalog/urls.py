#from os import path
from django.urls import path

from catalog.views import menu, dop, testik

app_name = 'catalog'

urlpatterns = [
    path('', menu),
    path('testik.html', testik),
    path('dop.html',dop)
]