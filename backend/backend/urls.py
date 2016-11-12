from django.conf.urls import url, include  # that include does include all the other files
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('userManager.urls', namespace='userManager')),  # includes the sub urls structure of the app
    url(r'^api/', include('api.urls', namespace='api'))  # includes the api module
]
