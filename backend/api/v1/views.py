from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseNotFound
from django.views.generic import View
import logging

from config import config
from connectors.wunderlist import WunderlistConnector
from azure.messageservice import AzureMessageService

logger = logging.getLogger(__name__)

LIST_INBOX_ID = 276664080


class PingView(View):
    def get(self, request):
        return HttpResponse('pong')


class WebhookView(View):
    def get(self, request, application):
        if application == 'wunderlist':
            wl_conn = WunderlistConnector(config.CLIENT_ID, config.ACCESS_TOKEN)
            return JsonResponse(wl_conn.get_webhooks(LIST_INBOX_ID), safe=False)
        else:
            return HttpResponseNotFound

    def post(self, request, application):
        if application == 'wunderlist':
            ws_conn = WunderlistConnector(config.CLIENT_ID, config.ACCESS_TOKEN)
            ams = AzureMessageService()

            tasks = ws_conn.get_tasks(LIST_INBOX_ID)

            ams.write({
                'tasks': tasks,
                'dialogs': [
                    'You are doing great today!',
                    'Keep it up!'
                ],
                'mood': {
                    'feeling': 'excited',
                    'value': 0.85
                }
            })

            ams.exit()

            return HttpResponse()

        else:
            wl_conn = WunderlistConnector(config.CLIENT_ID, config.ACCESS_TOKEN)

            return JsonResponse(wl_conn.add_webhook(LIST_INBOX_ID))

    def delete(self, request, application):
        wl_conn = WunderlistConnector(config.CLIENT_ID, config.ACCESS_TOKEN)

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
        ws_conn = WunderlistConnector(config.CLIENT_ID, config.ACCESS_TOKEN)

        tasks = ws_conn.get_tasks(LIST_INBOX_ID)

        return JsonResponse({
            'tasks': tasks,
            'dialogs': [
                'You are doing great today!',
                'Keep it up!'
            ],
            'mood': {
                'feeling': 'excited',
                'value': 0.85
            }
        })


class CallbackView(View):
    def get(self, request, application):
        return HttpResponse(request.body.decode('utf-8'))
