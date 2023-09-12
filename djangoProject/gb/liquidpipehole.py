import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def liquidpipehole(request):
    body = json.loads(request.body)
    name = body.get('name')
    a = body.get('a')
    rho = body.get('rho')
    p_0 = body.get('p_0')
    c_d = body.get('c_d')
    l = a * c_d * (2 * rho * (p_0 * 1000 - 101325) * 0.98)**0.5
    print(l)
    res = {
        'code': 1,
        'data1': name,
        'data2': l,
        'msg': '运算成功'
    }
    return JsonResponse(res)
