import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# parameters

# Create your views here.
@csrf_exempt
def fraction_saturationvapor(request):
    body = json.loads(request.body)
    a = body.get('a')
    delta_h_v = body.get('delta_h_v')
    v_fg = body.get('v_fg')
    t = body.get('t')
    c_s = body.get('c_s')
    q_m = delta_h_v * a / v_fg * (0.98 / t / c_s)**0.5
    res = {
        'code': 1,
        'data': q_m,
        'msg': '运算成功'
    }
    return JsonResponse(res)