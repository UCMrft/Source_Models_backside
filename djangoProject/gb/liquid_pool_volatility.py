import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# parameters

# Create your views here.
@csrf_exempt
def liquid_pool_volatility(request):
    body = json.loads(request.body)
    name = body.get('name')
    m_w = body.get('m_w')
    k = body.get('k')
    p_sat = body.get('p_sat')
    tem_l = body.get('tem_l')
    q_m = m_w * k * p_sat * 1000 / 8.314 / tem_l
    res = {
        'code': 1,
        'data1': name,
        'data2': q_m,
        'msg': '运算成功'
    }
    return JsonResponse(res)
