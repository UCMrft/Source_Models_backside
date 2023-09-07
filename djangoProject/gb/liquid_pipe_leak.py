import json
import numpy as np
import math
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

anticipate_value = 5
@csrf_exempt
def liquid_pipe_leak(request):
    body = json.loads(request.body)
    z = body.get('z')
    d = body.get('d')
    epsilon = body.get('epsilon')
    myu = body.get('myu')
    rho = body.get('rho')
    length = body.get('length')
    u_0 = body.get('u_0')
    for i in range(100):
        re = d * u_0 * rho / myu
        aa = ((epsilon / d)**1.1098) / 2.8257 + 5.8506 / (re**0.8981)
        intermidiate = -4 * np.log10((epsilon / d / 3.7065) - 5.0452 * np.log10(aa) / re)
        f = intermidiate**(-2)
        k_f = 460 / re + 1320 * f + 1.6
        ff = (660 * f + 0.8) * u_0 * u_0
        u = (-2 * 9.8 * z - 2 * 0.98 * ff)**(-0.5)
        if abs(u - u_0) > 0.001:
            return
        else: print(u)






