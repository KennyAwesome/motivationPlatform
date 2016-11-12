from django.conf.urls import url, include  # that include does include all the other files

app_name = 'api'  # if you get template problems, you have probably forgotten to set namespace

urlpatterns = [
    url(r'^v1/', include('api.v1.urls', namespace='api-v1'))
]
