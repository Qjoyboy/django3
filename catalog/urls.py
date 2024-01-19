#from os import path
from django.urls import path

from catalog import views
from catalog.views import ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'catalog'


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('testik/', ProductCreateView.as_view(), name='create'),
    path('one/<int:pk>/', ProductDetailView.as_view(), name='one'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete')
]