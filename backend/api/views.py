from django.http import HttpResponse, JsonResponse


def ping(request):
    html = 'hello world!'
    return HttpResponse(html)


def update_nao(request):
    # do something

    return JsonResponse({
        'text': 'hello world!'
    })


def update_todo(request):
    return HttpResponse('works')


def receive_access_token(request):
    return