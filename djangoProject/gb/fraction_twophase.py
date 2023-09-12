import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# parameters

# Create your views here.
@csrf_exempt
def fraction_twophase(request):
    body = json.loads(request.body)
    name = body.get('name')
    a = body.get('a')
    rho = body.get('rho')
    c_d = body.get('c_d')
    p_sat = body.get('p_sat')
    q_m = a * c_d * (2 * rho * 0.98 * (101325 - p_sat * 1000))
    res = {
        'code': 1,
        'data1': name,
        'data2': q_m,
        'msg': '运算成功'
    }
    return JsonResponse(res)
