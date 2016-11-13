from django.conf.urls import url, include  # that include does include all the other files
from django.contrib import admin

from config import api
from connectors.storage.database import DatabaseConnector
from models.user import User

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('usermanager.urls', namespace='usermanager')),  # includes the sub urls structure of the app
    url(r'^api/', include('api.urls', namespace='api'))  # includes the api module
]

# write some default values into the DB
db_conn = DatabaseConnector()
db_conn.set_user(User(api.KENNY_USER_ID, api.KENNY_USER_NAME, 0, api.KENNY_ACCESS_TOKEN))
