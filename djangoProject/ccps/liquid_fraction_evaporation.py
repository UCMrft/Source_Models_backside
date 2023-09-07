from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# parameters

# Create your views here.
@csrf_exempt
def liquid_fraction_evaporation(request):
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
    # 泄露速率
    if length > 0.1 and p_sat > 101.325:
        l = 1.2 * c_d * d * d * (rho_l * (9.8 * rho_l * h_b + 1000 * (p_0 - 101.325)))**0.5
    else: l = 20 * d * d *delta_h_v / (1 / rho_v - 1 / rho_l) / (c_s * tem)**0.5
    #表观流速，距离，时间
    t = 0.45 * h**0.5
    v_d = 4 * l / (3.14 * d * d * c_d * rho_l)
    s = v_d * t
    #初始蒸发量
    v_0 = rho_v * i
    #闪蒸部分
    f_v = (tem - tem_b) * c_s / delta_h_v
    d_d = 0.17 * (1 - f_v) / v_d / v_d
    f_d = 0.043 * v_d * v_d * m_w ** (2 / 3) * p_sat * h ** 0.5 * tem
    tem_aero = ((7.9 * u_d * (h**0.5) * tem_a * v_d * v_d) / (rho_l * (1 - f_v) + c_s * tem * f_d * delta_h_v / 2)) / ((7.9 * u_d * (h**0.5) * v_d * v_d) / (rho_l * (1 - f_v) + c_s))
    rho_b = 1 / (f_v / rho_v - (1 - f_v) / rho_l)
    #液池@
    v_d2 = 4 * l / (3.14 * d * d * c_d * (1 / (f_v / rho_v + (1 - f_v) / rho_l)))
    f_d2 = 0.043 * v_d2 * v_d2 * m_w ** (2 / 3) * p_sat * h ** 0.5 * tem
    l_b = l * (1 - f_v) * (1 - f_d)
    m_p = 0.0021 * m_w ** (2 / 3) * u**0.78 * p_sat2 / tem_p
    a_p = l_b / ((rho_l / 100 / t) + m_p / 2)
    evap_rate = m_p * a_p
    aero_rate = evap_rate + l * (f_v + f_d2 * (1 - f_v))
    res = {
        'code': 1,
        'data1': l,
        'data2': i,
        'data3': t,
        'data4': v_d,
        'data5': s,
        'data6': f_v,
        'data7': f_d,
        'data8': d_d,
        'data9': tem_aero,
        'data10': m_p,
        'data11': a_p,
        'data12': aero_rate,
        'msg': '运算成功'
    }
    return JsonResponse(res)