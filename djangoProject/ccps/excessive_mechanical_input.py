from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# parameters

# Create your views here.
@csrf_exempt
def excessive_mechanical_input(request):
    body = json.loads(request.body)
    name = body.get('name')
    q_me = body.get('q_me')
    u = body.get('u')
    a_s = body.get('a_s')
    tem_r = body.get('tem_r')
    tem_a = body.get('tem_a')
    delta_h_v = body.get('delta_h_v')
    v = q_me - u * a_s * (tem_r - tem_a) / delta_h_v
    res = {
        'code': 1,
        'data1': v,
        'msg': '运算成功'
    }
    return JsonResponse(res)