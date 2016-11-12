from django.conf.urls import url  # that include does include all the other files

from api.v1 import views

app_name = 'api-v1'

urlpatterns = [
    url(r'^ping/', views.PingView.as_view()),
    url(r'^webhook/(?P<application>[a-z0-9]*)/$', views.WebhookView.as_view()),
    url(r'^update/(?P<device_id>[a-z0-9]*)', views.UpdateView.as_view())
]
