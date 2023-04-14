import json

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseNotAllowed, HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


def calc(request: WSGIRequest, *args, **kwargs):
    if request.body:
        data = json.loads(request.body)
        try:
            a = int(data['A'])
            b = int(data['B'])
        except Exception:
            response_data = {'error': 'Некорректный набор данных'}
            response = JsonResponse(response_data)
            response.status_code = 400
            return response
        if request.path == '/add/':
            answer = {'answer': a + b}
        elif request.path == '/subtract/':
            answer = {'answer': a - b}
        elif request.path == '/multiply/':
            answer = {'answer': a * b}
        elif request.path == '/divide/':
            if b == 0:
                response_data = {'error': 'Division by zero!'}
                response = JsonResponse(response_data)
                response.status_code = 400
                return response
            else:
                answer = {'answer': a / b}
        answer_as_json = json.dumps(answer)
        response = HttpResponse(answer_as_json, content_type='application/json')
        return response
    else:
        response_data = {'error': 'Некорректный набор данных'}
        response = JsonResponse(response_data)
        response.status_code = 400
        return response


@ensure_csrf_cookie
def get_token_view(request: WSGIRequest, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(f'Only GET request are allowed{request.method}')
