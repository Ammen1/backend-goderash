from django.urls import path
from . views import *


app_name = 'base'

urlpatterns = [
    # Admin
    path('admin/create/', CreateService.as_view(), name='createservice'),
    path('admin/listcreate/', ServiceList.as_view(), name='listservice'),
    path('admin/detailservice/<int:id>/',
         ServiceDaitle.as_view(), name='detailservice'),
    path('admin/editservices/<int:pk>/',
         EditService.as_view(), name='editservices'),
    path('admin/deleteservice/<int:pk>/',
         DeleteService.as_view(), name='deleteservice')


]
