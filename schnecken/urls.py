from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^schnecken$', views.schnecken_bilder, name='schnecken'),
    url(r'^dachwurzen$', views.dachwurzen_bilder, name='dachwurzen'),
    url(r'^maerkte$', views.markt, name='maerkte'),

]