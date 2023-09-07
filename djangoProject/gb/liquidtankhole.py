import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# parameters
p_a = 101325
g_c = 0.98
g = 9.8

# Create your views here.
@csrf_exempt
def liquidtankhole(request):
    body = json.loads(request.body)
    a = body.get('a')
    rho = body.get('rho')
    p_0 = body.get('P_0')
    c_d = body.get('C_d')
    h_b = body.get('h_b')
    l = rho * a * c_d * (2 * 0.98 * (p_0 * 1000 - 101325) / rho + 9.8 * h_b)**0.5
    res = {
        'code': 1,
        'data': l,
        'msg': '运算成功'
    }
    return JsonResponse(res)