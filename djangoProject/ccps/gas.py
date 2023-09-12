from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# parameters

# Create your views here.
@csrf_exempt
def gas(request):
    body = json.loads(request.body)
    name = body.get('name')
    d = body.get('d')
    c_d = body.get('c_d')
    tem = body.get('tem')
    p_0 = body.get('p_0')
    i = body.get('i')
    m_w = body.get('m_w')
    v = 23 * c_d * d * d * p_0 * (((101.325 / p_0)**1.429 - (101.325 / p_0)**1.714) * m_w / tem)**0.5
    v10 = 600 * v
    v60 = 6 * v10
    t = i / v
    if t >= 3600:
        res = {
            'code': 1,
            'data1': v,
            'data2': v10,
            'data3': v60,
            'data4': i,
            'data5': name,
            'msg': '运算成功'
            }
    elif 60 <= t < 3600:
        res = {
            'code': 1,
            'data1': v,
            'data2': v10,
            'data3': i,
            'data4': name,
            'msg': '运算成功'
            }
    else: res = {
            'code': 1,
            'data1': v,
            'data2': i,
            'data3': name,
            'msg': '运算成功'
            }
    return JsonResponse(res)
