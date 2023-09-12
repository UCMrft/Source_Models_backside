from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# parameters

# Create your views here.
@csrf_exempt
def excessive_heat_input(request):
    body = json.loads(request.body)
    name = body.get('name')
    q_fire = body.get('q_fire')
    delta_h_v = body.get('delta_h_v')
    v = q_fire / delta_h_v
    res = {
        'code': 1,
        'data1': v,
        'data2': name,
        'msg': '运算成功'
    }
    return JsonResponse(res)
