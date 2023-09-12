import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# parameters

# Create your views here.
@csrf_exempt
def gaspipehole(request):
    body = json.loads(request.body)
     name = body.get('name')
    p_0 = body.get('p_0')
    gamma = body.get('gamma')
    rho = body.get('rho')
    m_w = body.get('m_w')
    tem = body.get('t')
    a = body.get('a')
    c_d = body.get('c_d')
    p_choked = p_0 * 1000 * (2 / gamma + 1)**(gamma / gamma + 1)
    if p_choked <= 101325:
        q_m = rho * a * c_d * (((2 * 0.98 * m_w) / 8.314 * tem) * (gamma / (gamma - 1) * ((p_0 / (p_0 - 101325)**(2 / gamma) - (p_0 / (p_0 - 101325)**(gamma + 1 / gamma))))))**0.5
    else: q_m = rho * a * c_d * ((0.98 * m_w) / (8.314 * tem) * (2 / (gamma + 1)**((gamma + 1) / (gamma - 1))))**0.5
    res = {
        'code': 1,
        'data1': name,
        'data2': q_m,
        'msg': '运算成功'
        }
    return JsonResponse(res)
