from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# parameters

# Create your views here.
@csrf_exempt
def excessive_heat_reaction(request):
    body = json.loads(request.body)
    name = body.get('name')
    m = body.get('m')
    q_rx = body.get('q_rx')
    delta_h_v = body.get('delta_h_v')
    v = m * q_rx / delta_h_v
    res = {
        'code': 1,
        'data1': v,
        'data2': name,
        'msg': '运算成功'
    }
    return JsonResponse(res)
