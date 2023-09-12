import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sympy import *
import sys
sys.setrecursionlimit(100000)
# parameters

# Create your views here.
@csrf_exempt
def gaspipeleak_adiabatic(request):
    body = json.loads(request.body)
    name = body.get('name')
    m_w = body.get('m_w')
    f = body.get('f')
    d = body.get('d')
    length = body.get('length')
    tem_1 = body.get('tem_1')
    p_1 = body.get('p_1')
    p_2 = body.get('p_2')
    gamma = body.get('gamma')
    #塞流计算上游马赫数
    left = 0.001
    right = 1

    def function(ma):
        function = (gamma + 1) / 2 * ln(2 * (1 + (gamma - 1) * ma * ma / 2) / (gamma + 1) / ma / ma) - (
                    1 / ma / ma - 1) + 4 * f * length / d
        return function

    for i in range(100):
        x = (left + right) / 2
        if function(x) == 0:
            break
        else:
            pass
        if function(left) * function(right) < 0:
            left = left
            right = x
        elif function(left) * function(right) > 0:
            left = x
            right = right
        else:
            break
    print((left + right) / 2)
    ma_1 = (left + right) / 2
    y_1 = 1 + (gamma - 1) / 2 * ma_1 * ma_1
    p_choked = p_1 * 1000 * ma_1 * (2 * y_1 / (gamma + 1))**0.5
    tem_choked = ma_1 * ((gamma + 1) / (2 * y_1))**0.5
    #非塞流计算下游温度
    def func(bottom):
        func = (ma_1 * ma_1 + (gamma - 1) / 2 * bottom * bottom) / (bottom * bottom + (gamma - 1) / 2 * ma_1 * ma_1) - (
                    p_1 / p_2) ** 2
        return func

    lt = 0
    rt = ma_1 - 0.001

    for j in range(100):
        y = (lt + rt) / 2
        if func(y) == 0:
            break
        else:
            pass
        if func(lt) * func(rt) < 0:
            lt = lt
            rt = y
        elif func(lt) * func(rt) > 0:
            lt = y
            rt = rt
        else:
            break
    print((lt + rt) / 2)
    ma_2 = (lt + rt) / 2
    y_2 = 1 + (gamma - 1) / 2 * ma_2 * ma_2
    tem_2 = y_1 / y_2 * tem_1
    if p_choked < p_2:
        g = ma_2 * p_2 * 1000 * (gamma * 0.98 * m_w / 8.314 / tem_2)**0.5,
    else: g = p_choked * (gamma * 0.98 * m_w / 8.314 / tem_choked)**0.5
    v = g * pi * d * d / 4
    res = {
        'code': 1,
        'data1': name,
        'data2': v,
        'msg': '运算成功'
    }
    return JsonResponse(res)
