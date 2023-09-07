

"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# 国标源模型
from gb import liquidpipehole as gb_views2
from gb import liquidtankhole as gb_views3
from gb import fractionevaporation as gb_views4
from gb import fraction_twophase as gb_views5
from gb import fraction_saturationvapor as gb_views6
from gb import fraction_massvolatilisation as gb_views7
from gb import gaspipehole as gb_views8
from gb import gaspipeleak_adiabatic as gb_views9
from gb import gaspipeleak_isothermal as gb_views10
from gb import liquid_pool_volatility as gb_views11
from gb import liquid_pool_boil as gb_views12
from gb import liquid_pipe_leak as gb_views13

# CCPS Source Models
from ccps import gas as ccps_views
from ccps import liquid_fraction_evaporation as ccps_views1
from ccps import liquid_rupture as ccps_views2
from ccps import excessive_heat_input as ccps_views3
from ccps import excessive_heat_reaction as ccps_views4
from ccps import excessive_heat_transfer as ccps_views5
from ccps import excessive_mechanical_input as ccps_views6

urlpatterns = [
    path('admin/', admin.site.urls),
    path('liquidpipehole',gb_views2.liquidpipehole),
    path('liquidtankhole', gb_views3.liquidtankhole),
    path('fractionevaporation', gb_views4.fractionevaporation),
    path('fraction_twophase', gb_views5.fraction_twophase),
    path('fraction_saturationvapor', gb_views6.fraction_saturationvapor),
    path('fraction_massvolatilisation', gb_views7.fraction_massvolatilisation),
    path('gaspipehole', gb_views8.gaspipehole),
    path('gaspipeleak_adiabatic', gb_views9.gaspipeleak_adiabatic),
    path('gaspipeleak_isothermal', gb_views10.gaspipeleak_isothermal),
    path('liquid_pool_volatility', gb_views11.liquid_pool_volatility),
    path('liquid_pool_boil', gb_views12.liquid_pool_boil),
    path('liquid_pipe_leak', gb_views13.liquid_pipe_leak),
    path('gas', ccps_views.gas),
    path('liquid_fraction_evaporation', ccps_views1.liquid_fraction_evaporation),
    path('liquid_rupture', ccps_views2.liquid_rupture),
    path('excessive_heat_input', ccps_views3.excessive_heat_input),
    path('excessive_heat_reaction', ccps_views4.excessive_heat_reaction),
    path('excessive_heat_transfer', ccps_views5.excessive_heat_transfer),
    path('excessive_mechanical_input', ccps_views6.excessive_mechanical_input)
]
