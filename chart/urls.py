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
from .views import chart,barchart,stackedbarchart,gaugechart,bubblechart,bubblechart2,ledChart,chart2,barisal,dhaka,rajshahi,khulna,sylhet,mymensingh,rangpur,mymensingh,chittagong,chart3,chart4,chart5
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
]
