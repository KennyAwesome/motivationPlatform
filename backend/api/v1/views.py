from django.http import HttpResponse, JsonResponse
from django.views import View


class PingView(View):
    def get(self, request):
        return HttpResponse('pong')


class WebhookView(View):
    def get(self, request, application):
        if application == 'wunderlist':
            return HttpResponse('works')