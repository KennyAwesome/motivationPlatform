import logging

from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseNotFound
from django.views.generic import View

from azure.messageservice import AzureMessageService
from config import api
from connectors.apps.wunderlist import WunderlistConnector
from connectors.storage.database import DatabaseConnector
from logic import moodscore

logger = logging.getLogger(__name__)
db_conn = DatabaseConnector()

LIST_INBOX_ID = 276664080


class PingView(View):
    def get(self, request):
        return HttpResponse('pong')


class WebhookView(View):
    def get(self, request, application):
        # user mocking
        user = db_conn.get_user(api.KENNY_USER_ID)

        if application == 'wunderlist':
            wl_conn = WunderlistConnector(api.CLIENT_ID, user.access_token)
            return JsonResponse(wl_conn.get_webhooks(LIST_INBOX_ID), safe=False)
        else:
            return HttpResponseNotFound

    def post(self, request, application):
        # user mocking
        user = db_conn.get_user(api.KENNY_USER_ID)

        if application == 'wunderlist':
            ws_conn = WunderlistConnector(api.CLIENT_ID, user.access_token)
            ams = AzureMessageService()

            tasks = ws_conn.get_tasks(LIST_INBOX_ID)

            # TODO calculate mood values here
            mood = {'name': 'excited'}  # CALCULATE ACTUAL MOOD!!
            speech = moodscore.get_speech(mood)
            print speech

            result = {
                'tasks': tasks,
                'speech': speech,
                'mood': mood
            }

            # TODO enable sending
            #ams.write(result)

            ams.exit()

            return HttpResponse()

        else:
            wl_conn = WunderlistConnector(api.CLIENT_ID, user.access_token)

            return JsonResponse(wl_conn.add_webhook(LIST_INBOX_ID))

    def delete(self, request, application):
        # user mocking
        user = db_conn.get_user(api.KENNY_USER_ID)

        wl_conn = WunderlistConnector(api.CLIENT_ID, user.access_token)

        lists = wl_conn.get_lists()

        for entry in lists:
            list_id = entry['id']
            list_rev = entry['revision']

            webhooks = wl_conn.get_webhooks(list_id)

            for webhook in webhooks:
                wh_id = webhook['id']

                wl_conn.remove_webhook(wh_id, list_rev)

        return HttpResponse()


class UpdateView(View):
    def get(self, request, device_id):
        # user mocking
        user = db_conn.get_user(api.KENNY_USER_ID)

        ws_conn = WunderlistConnector(api.CLIENT_ID, user.access_token)

        tasks = ws_conn.get_tasks(LIST_INBOX_ID)

        # TODO calculate mood values here
        mood = {'name': 'excited'}  # CALCULATE ACTUAL MOOD!!
        speech = moodscore.get_speech(mood)

        result = {
            'tasks': tasks,
            'speech': speech,
            'mood': mood
        }

        return JsonResponse(result)
