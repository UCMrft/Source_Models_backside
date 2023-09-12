from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# parameters

# Create your views here.
@csrf_exempt
def excessive_heat_transfer(request):
    body = json.loads(request.body)
    name = body.get('name')
    u = body.get('u')
    a_ht = body.get('a_ht')
    t_hm = body.get('t_hm')
    tem_r = body.get('tem_r')
    delta_h_v = body.get('delta_h_v')
    v = u * a_ht * (t_hm - tem_r) / delta_h_v
    res = {
        'code': 1,
        'data1': v,
        'data2': name,
        'msg': '运算成功'
    }
    return JsonResponse(res)
