from django.urls import path
from . import views





#urlpatterns = [
#	path(r'^$', views.index, name='index')
#    ]

from django.urls import path

urlpatterns = [
    #Home page,
    path('',views.index, name='index'),
]