from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# parameters

# Create your views here.
@csrf_exempt
def liquid_rupture(request):
    body = json.loads(request.body)
    name = body.get('name')
    d = body.get('d')
    c_d = body.get('c_d')
    tem = body.get('tem')
    length = body.get('length')
    p_0 = body.get('p_0')
    i = body.get('i')
    h_b = body.get('h_b')
    h = body.get('h')
    u_gnd= body.get('u_gnd')
    u_d = body.get('u_d')
    u = body.get('u')
    c_s = body.get('c_s')
    m_w = body.get('m_w')
    delta_h_v = body.get('delta_h_v')
    rho_v = body.get('rho_v')
    rho_l = body.get('rho_l')
    p_sat = body.get('p_sat')
    p_sat2 = body.get('p_sat2')
    tem_a = body.get('tem_a')
    tem_b = body.get('tem_b')
    tem_p = body.get('tem_p')
    i = body.get('i')
    #初始蒸发量
    v_0 = rho_v * i
    #闪蒸部分
    f_v = (tem - tem_b) * c_s / delta_h_v
    rho_b = 1 / (f_v / rho_v - (1 - f_v) / rho_l)
    # 表观流速，距离，时间
    t = 0.45 * h ** 0.5
    v_d = 1.54 * (9.8 * h_b + 1000 * (p_0 - 101.325) / rho_b) ** 0.5
    d_d = 0.17 * (1 - f_v) / v_d / v_d
    f_d = 0.043 * v_d * v_d * m_w ** (2 / 3) * p_sat * h ** 0.5 * tem
    tem_aero = ((7.9 * u_d * (h**0.5) * tem_a * v_d * v_d) / (rho_l * (1 - f_v) + c_s * tem * f_d * delta_h_v / 2)) / ((7.9 * u_d * (h**0.5) * v_d * v_d) / (rho_l * (1 - f_v) + c_s))
    a_p = 100 * (i - v_0) / rho_l
    m_p = 0.0021 * m_w ** (2 / 3) * u**0.78 * p_sat2 / tem_p
    res = {
        'code': 1,
        'data1': i,
        'data2': t,
        'data3': v_d,
        'data4': f_v,
        'data5': f_d,
        'data6': d_d,
        'data7': tem_aero,
        'data8': m_p,
        'data9': a_p,
        'msg': '运算成功'
    }
    return JsonResponse(res)

