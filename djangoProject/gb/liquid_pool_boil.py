import json
from sympy import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# parameters

# Create your views here.
@csrf_exempt
def liquid_pool_boil(request):
    body = json.loads(request.body)
    k_s = body.get('k_s')
    tem_g = body.get('tem_g')
    tem_l = body.get('tem_l')
    delta_h_v = body.get('delta_h_v')
    a_s = body.get('a_s')
    t = body.get('t')
    a = body.get('a')
    q_m = k_s * (tem_g - tem_l) * a / delta_h_v / (pi * a_s * t)**0.5
    res = {
        'code': 1,
        'data': q_m,
        'msg': '运算成功'
    }
    return JsonResponse(res)