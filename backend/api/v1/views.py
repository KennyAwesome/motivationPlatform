from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseNotFound
from django.views import View


class PingView(View):
    def get(self, request):
        return HttpResponse('pong')


class WebhookView(View):
    def get(self, request, application):
        if application == 'wunderlist':
            return HttpResponse('works')
        else:
            return HttpResponseNotFound('The webhook for \'' + application + '\' is not activated')


class UpdateView(View):
    def get(self, request, device_id):
        if device_id == 'nao':
            return JsonResponse({
                'tasks': [
                    {
                        'id': 12345,
                        'due_date': '2013-08-30T08:36:13.273Z',
                        'starred': True,
                        'title': 'Clean the dishes'
                    }
                ]
            })
        else:
            return HttpResponseNotFound('The device \'' + device_id + '\' could not be found')
