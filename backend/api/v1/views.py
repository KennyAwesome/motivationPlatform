import logging

from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseNotFound
from django.views.generic import View

from config import api
from connectors.apps.wunderlist import WunderlistConnector
from connectors.devices.messageservice import AzureConnector
from connectors.storage.database import DatabaseConnector
from logic import moodscore
from logic.moodscore import calculate_points, calculate_score
from models.tasks import get_today_tasks, get_n_open, get_n_overdue, enrich_tasks_dates

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
            az_conn = AzureConnector()

            tasks_open = ws_conn.get_tasks(LIST_INBOX_ID)
            tasks_completed = ws_conn.get_completed_tasks(LIST_INBOX_ID)

            reminders = ws_conn.get_reminders(LIST_INBOX_ID)

            # print 'open: ' + str(tasks_open)
            # print 'completed: ' + str(tasks_completed)
            # print 'reminders: ' + str(reminders)

            enrich_tasks_dates(tasks_open, reminders)
            enrich_tasks_dates(tasks_completed, reminders)

            tasks_open_today = get_today_tasks(tasks_open)
            tasks_completed_today = get_today_tasks(tasks_completed)

            n_overd_reg, n_overd_star = get_n_overdue(tasks_open_today)
            n_done_reg, n_done_star = get_n_open(tasks_completed_today)

            # print 'n overd reg: ' + str(n_overd_reg) + ' n overd star: ' + str(n_overd_star)
            # print 'n done reg: ' + str(n_done_reg) + ' n done star: ' + str(n_done_star)

            points = calculate_points(n_done_reg, n_done_star, n_overd_reg, n_overd_star)
            mood, pleasure = calculate_score(points)

            mood['points'] = points
            mood['pleasure'] = pleasure

            speech = moodscore.get_speech(mood)

            # print ' points: ' + str(points) + ' speech: ' + speech

            result = {
                'tasks': tasks_open,
                'speech': speech,
                'mood': mood
            }

            az_conn.write(result)

            az_conn.exit()

            return HttpResponse()

        else:
            return HttpResponseNotFound('webhook endpoint not defined')

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

        tasks_open = ws_conn.get_tasks(LIST_INBOX_ID)
        tasks_completed = ws_conn.get_completed_tasks(LIST_INBOX_ID)

        reminders = ws_conn.get_reminders(LIST_INBOX_ID)

        # print 'open: ' + str(tasks_open)
        # print 'completed: ' + str(tasks_completed)
        # print 'reminders: ' + str(reminders)

        enrich_tasks_dates(tasks_open, reminders)
        enrich_tasks_dates(tasks_completed, reminders)

        tasks_open_today = get_today_tasks(tasks_open)
        tasks_completed_today = get_today_tasks(tasks_completed)

        n_overd_reg, n_overd_star = get_n_overdue(tasks_open_today)
        n_done_reg, n_done_star = get_n_open(tasks_completed_today)

        # print 'n overd reg: ' + str(n_overd_reg) + ' n overd star: ' + str(n_overd_star)
        # print 'n done reg: ' + str(n_done_reg) + ' n done star: ' + str(n_done_star)

        points = calculate_points(n_done_reg, n_done_star, n_overd_reg, n_overd_star)
        mood, pleasure = calculate_score(points)

        mood['points'] = points
        mood['pleasure'] = pleasure

        speech = moodscore.get_speech(mood)

        # print ' points: ' + str(points) + ' speech: ' + speech

        result = {
            'tasks': tasks_open,
            'speech': speech,
            'mood': mood
        }

        return JsonResponse(result)
