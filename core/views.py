import json
import os
import re

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Enter


PHONE_PATTERN = re.compile(r'^1[3-9]\d{9}$')
DEFAULT_ALLOWED_ORIGINS = {
    'https://fathers-day-website-5dxq.vercel.app',
    'https://fathers-day-website-ten.vercel.app',
}


def get_allowed_origin(request):
    request_origin = request.headers.get('Origin')
    configured_origins = {
        origin.strip()
        for origin in os.environ.get('CORS_ALLOWED_ORIGIN', '').split(',')
        if origin.strip()
    }
    allowed_origins = configured_origins | DEFAULT_ALLOWED_ORIGINS

    if request_origin in allowed_origins:
        return request_origin

    return next(iter(configured_origins), request_origin or '*')


def api_response(request, data, status=200):
    response = JsonResponse(data, status=status)
    response['Access-Control-Allow-Origin'] = get_allowed_origin(request)
    response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


def health_check(request):
    return JsonResponse({'success': True, 'message': 'ok'})


def parse_enter_payload(request):
    try:
        payload = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return None, '提交的数据格式不正确。'

    username = str(payload.get('username', '')).strip()
    phone = str(payload.get('phone', '')).strip()

    if not username:
        return None, '请输入用户名。'

    if not PHONE_PATTERN.fullmatch(phone):
        return None, '请输入正确的 11 位手机号。'

    return {'username': username, 'phone': phone}, ''


@csrf_exempt
def register_enter(request):
    if request.method == 'OPTIONS':
        return api_response(request, {})

    if request.method != 'POST':
        return api_response(request, {'success': False, 'message': '只支持 POST 请求。'}, status=405)

    payload, error = parse_enter_payload(request)
    if error:
        return api_response(request, {'success': False, 'message': error}, status=400)

    if Enter.objects.filter(username=payload['username']).exists():
        return api_response(request, {'success': False, 'message': '这个用户名已经注册过了，请切换到登录。'}, status=409)

    enter = Enter.objects.create(username=payload['username'], phone=payload['phone'])
    return api_response(request, {
        'success': True,
        'message': '注册成功。',
        'data': {
            'id': enter.id,
            'username': enter.username,
            'phone': enter.phone,
        },
    }, status=201)


@csrf_exempt
def login_enter(request):
    if request.method == 'OPTIONS':
        return api_response(request, {})

    if request.method != 'POST':
        return api_response(request, {'success': False, 'message': '只支持 POST 请求。'}, status=405)

    payload, error = parse_enter_payload(request)
    if error:
        return api_response(request, {'success': False, 'message': error}, status=400)

    enter = Enter.objects.filter(username=payload['username'], phone=payload['phone']).first()
    if not enter:
        return api_response(request, {'success': False, 'message': '还没有注册过这组信息，请先注册后再登录。'}, status=404)

    return api_response(request, {
        'success': True,
        'message': '登录成功。',
        'data': {
            'id': enter.id,
            'username': enter.username,
            'phone': enter.phone,
        },
    })
