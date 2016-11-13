from django.conf.urls import url
#from django.contrib import admin
from . import views # . -> current directory

app_name = 'usermanager' # if you get template problems, you have probably forgotten to set namespace

urlpatterns = [
    url(r'^$', views.IndexView.as_view() , name='index'), # default: ^$ -> index
    #url(r'^(?P<some_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^register$', views.RegisterView.as_view() , name='register'),
    url(r'^login$', views.LoginView.as_view() , name='login'),
]