from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseNotFound
from django.views.generic import View

from config import config
from connectors.wunderlist import WunderlistConnector


class PingView(View):
    def get(self, request):
        return HttpResponse('pong')


class WebhookView(View):
    def get(self, request, application):
        if application == 'wunderlist':
            print ' --- WEBHOOK TRIGGERED ---'
            print request.body

            return HttpResponse('works')

        wl_conn = WunderlistConnector(config.CLIENT_ID, config.ACCESS_TOKEN)

        return HttpResponse(str(wl_conn.get_webhooks(276664080)))

    def post(self, request, application):
        wl_conn = WunderlistConnector(config.CLIENT_ID, config.ACCESS_TOKEN)

        return HttpResponse(str(wl_conn.add_webhook(276664080)))


class UpdateView(View):
    def get(self, request, device_id):
        if device_id == 'test':

            return HttpResponse('worked')

        else:
            response = JsonResponse({
                'tasks': [
                    {
                        'id': 12345,
                        'due_date': '2013-08-30T08:36:13.273Z',
                        'starred': True,
                        'title': 'Clean the dishes'
                    }
                ],
                'dialogs': [
                    'You are doing great today!',
                    'Keep it up!'
                ],
                'mood': {
                    'feeling': 'excited',
                    'value': 0.85
                }
            })

        return response
        # else:
        #     return HttpResponseNotFound('The device \'' + device_id + '\' could not be found')


class CallbackView(View):
    def get(self, request, application):
        return HttpResponse(request.body.decode('utf-8'))
