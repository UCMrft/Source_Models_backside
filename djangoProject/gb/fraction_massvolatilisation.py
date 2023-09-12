import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# parameters

# Create your views here.
@csrf_exempt
def fraction_massvolatilisation(request):
    body = json.loads(request.body)
    name = body.get('name')
    m_w = body.get('m_w')
    k = body.get('k')
    p_sat = body.get('p_sat')
    t_l = body.get('t_l')
    q_m = m_w * k * p_sat * 1000 / (t_l * 8.314)
    res = {
        'code': 1,
        'data1': name,
        'data2': q_m,
        'msg': '运算成功'
    }
    return JsonResponse(res)
