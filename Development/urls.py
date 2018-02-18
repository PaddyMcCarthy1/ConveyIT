from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.development_list, name='development_list'),
]