#from os import path
from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, active

app_name = 'blog'

urlpatterns=[
    path('bloglist/', BlogListView.as_view(), name='bloglist'),
    path('blogdetail/<slug:slug>/', BlogDetailView.as_view(), name='blogdetail'),
    path('blogcreate/', BlogCreateView.as_view(), name='blogcreate'),
    path('blogedit/<slug:slug>/', BlogUpdateView.as_view(), name='blogedit'),
    path('blogdelete/<slug:slug>/', BlogDeleteView.as_view(), name='blogdelete'),
    path('active/<slug:slug>/', active, name='active')
    ]