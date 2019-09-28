"""map_highchart_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from .views import *

urlpatterns = [
   path('chart',chart,name="chart"),
   path('map',chart2,name="chart"),
   path('map2',chart3,name="chart"),
   path('map3',chart4,name="chart"),
   path('map4',chart5,name="chart"),
   path('barisal',barisal,name="chart"),
   path('mymensingh',mymensingh,name="chart"),
   path('dhaka',dhaka,name="chart"),
   path('rajshahi',rajshahi,name="chart"),
   path('rangpur',rangpur,name="chart"),
   path('khulna',khulna,name="chart"),
   path('sylhet',sylhet,name="chart4"),
   path('chittagong',chittagong,name="chart"),
   path('mymensingh',mymensingh,name="chart"),
   path('barchart',barchart,name="bar_chart"),
   path('stack',stackedbarchart,name="stacked_bar_chart"),
   path('gauge',gaugechart,name="gauge_chart"),
   path('bubble',bubblechart,name="bubble_chart"),
   path('led',ledChart,name="led_chart"),
   path('bd',linkedchart,name="led_chart"),
   path('bb',bubblechart3,name="led_chart"),
   path('l2',ledChart2,name="led_chart"),
   path('bs',bubble_slide,name="bubble_slide"),
   path('b1',bubblechart4,name="bubble_slide"),
   path('svg',svg_map,name="bubble_slide"),
   path('table',table,name="bubble_slide"),
   path('svgid',svgid,name="bubble_slide"),
   path('fsvg',fetch_svg,name="bubble_slide"),
   path('drilldown',drillDown,name="bubble_slide"),
   path('drill',drillDown_test,name="bubble_slide"),
   path('on',onclickev,name="bubble_slide"),
   path('multi',multishadowclone,name="bubble_slide"),
   path('div',divtest,name="bubble_slide"),
   path('click',clicktest,name="bubble_slide"),
   path('mainframe',mainframe,name="bubble_slide"),
]
