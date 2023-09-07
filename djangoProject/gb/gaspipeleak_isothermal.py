import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sympy import *
import sys
sys.setrecursionlimit(100000)
# parameters

# Create your views here.
@csrf_exempt
def gaspipeleak_isothermal(request):
    body = json.loads(request.body)
    m_w = body.get('m_w')
    f = body.get('f')
    d = body.get('d')
    length = body.get('length')
    tem = body.get('tem')
    p_1 = body.get('p_1')
    p_2 = body.get('p_2')
    gamma = body.get('gamma')
    #塞流计算上游马赫数
    ma = symbols('ma')
    expr1 = ln(1 / gamma / ma / ma) - (1 / gamma / ma / ma - 1) + 4 * f * length / d
    r1 = solve(expr1, ma)
    ma_1 = r1[2]
    p_choked = p_1 * 1000 * ma_1 * gamma ** 0.5,

    # 非塞流计算质量通量G
    if p_2 > p_1 * ma_1 * gamma ** 0.5:
        g_solve = symbols('g_solve')
        expr2 = 2 * ln(p_1 / p_2) - 0.98 * m_w / (g_solve * 8.314 * tem) * (p_1 * 1000 - p_2 * 1000) * (p_1 * 1000 + p_2 * 1000) + 4 * f * length / d
        g_0 = solve(expr2, g_solve)
        g = g_0[0]
    else:
        g = p_choked * (0.98 * m_w / tem / 8.314) ** 0.5
    v = g * 3.14 * d * d / 4
    res = {
        'code': 1,
        'data': v,
        'msg': '运算成功'
    }
    return JsonResponse(res)