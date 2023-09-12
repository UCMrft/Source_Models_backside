import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# parameters

# Create your views here.
@csrf_exempt
def fractionevaporation(request):
    body = json.loads(request.body)
    name = body.get('name')
    c_p = body.get('c_p')
    m = body.get('m')
    t_0 = body.get('t_0')
    t_b = body.get('t_b')
    delta_h_v = body.get('delta_h_v')
    m_v = m * c_p * (t_0 - t_b) / delta_h_v
    res = {
        'code': 1,
        'data1': name,
        'data2': m_v,
        'msg': '运算成功'
    }
    return JsonResponse(res)
