#from os import path
from django.urls import path

from catalog import views
from catalog.views import ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, active

app_name = 'catalog'


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('testik/', ProductCreateView.as_view(), name='create'),
    path('one/<int:pk>/', ProductDetailView.as_view(), name='one'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('bloglist/', BlogListView.as_view(), name='bloglist'),
    path('blogdetail/<slug:slug>/', BlogDetailView.as_view(), name='blogdetail'),
    path('blogcreate/', BlogCreateView.as_view(), name='blogcreate'),
    path('blogedit/<slug:slug>/', BlogUpdateView.as_view(), name='blogedit'),
    path('blogdelete/<slug:slug>/', BlogDeleteView.as_view(), name='blogdelete'),
    path('active/<slug:slug>/', active, name='active')
]