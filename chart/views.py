from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .fusioncharts import FusionCharts
from collections import OrderedDict

# Loading Data from a Ordered Dictionary
# Example to create a World Map with the chart data passed as Dictionary format.
# The `chart` method is defined to load chart data from Dictionary.

def chart(request):

  # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
  dataSource = OrderedDict()

  # The `mapConfig` dict contains key-value pairs data for chart attribute
  mapConfig = OrderedDict()
  mapConfig["caption"] = "Average Annual Population Growth"
  mapConfig["subcaption"] = "1955-2015"
  mapConfig["numbersuffix"] = "%"
  mapConfig["includevalueinlabels"] = "1"
  mapConfig["labelsepchar"] = ":"
  mapConfig["theme"] = "fusion"

  # Map color range data
  colorDataObj = { "minvalue": "0", "code" : "#FFE0B2", "gradient": "1",
    "color" : [
        { "minValue" : "0.5", "maxValue" : "1", "code" : "#FFD74D" },
        { "minValue" : "1.0", "maxValue" : "2.0", "code" : "#FB8C00" },
        { "minValue" : "2.0", "maxValue" : "3.0", "code" : "#E65100" }
    ]
  }

  dataSource["chart"] = mapConfig
  dataSource["colorrange"] = colorDataObj
  dataSource["data"] = []


  # Map data array
  mapDataArray = [
    ["NA", "0.82", "1"],
    ["SA", "2.04", "1"],
    ["AS", "1.78", "1"],
    ["EU", "0.40", "1"],
    ["AF", "2.58", "1"],
    ["AU", "1.30", "1"]
  ]


  # Iterate through the data in `mapDataArray` and insert in to the `dataSource["data"]` list.
  # The data for the `data` should be in an array wherein each element of the array is a JSON object
  # having the `id`, `value` and `showlabel` as keys.
  for i in range(len(mapDataArray)):
      dataSource["data"].append({"id": mapDataArray[i][0], "value": mapDataArray[i][1], "showLabel": mapDataArray[i][2] })

  # Create an object for the world map using the FusionCharts class constructor
  # The chart data is passed to the `dataSource` parameter.
  fusionMap = FusionCharts("maps/world", "ex1" , "650", "450", "chart-1", "json", dataSource)

  # returning complete JavaScript and HTML code, which is used to generate map in the browsers.
  return  render(request, 'index.html', {'output' : fusionMap.render(), 'chartTitle': 'Simple Map Using Array'})


def barchart(request):
   chartObj = FusionCharts( 'column2d','ex1',"70%","400",'chart-1','json', """{
  "chart": {
    "caption": "Shoppers",
    "numbersuffix": "K",
    "theme": "fusion",
    "palettecolors":"333333,26bfff,ff6b5e",
    "showYAxisValues": "0",
  },
  "data": [
    {
      "label": "High",
      "value": "12.345"
    },
    {
      "label": "Medium",
      "value": "9.345"
    },
    {
      "label": "Low",
      "value": "32.345"
    }
  ]
}""")
   return render(request, 'index.html', {'output': chartObj.render()})


def stackedbarchart(request):
   chartObj = FusionCharts( 'stackedcolumn2d', 'chart-container', '70%', '400', 'chart-1', 'json', """{
    "chart": {
     
        "theme": "fusion",
        "showYAxisValues": "0",
        "showsum" : "1",
        "showLegend": "0"

    },
    "categories": [ 
        {
            "category": [
                {
                    "label": "High"
                },
                {
                    "label": "Medium"
                },
                {
                    "label": "Large"
                },
            
            ]
        }
    ],
    "dataset": [
        {
            "seriesname": "Male",
            "data": [
                {
                    "value": "11000",
                    "color" : "333333"
                },
                {
                    "value": "15000",
                    "color" : "26bfff"

                },
                {
                    "value": "13500",
                    "color" : "ff6b5e"

                    
                },
              
            ]
        },
        {
            "seriesname": "Female",
            "data": [
                {
                    "value": "11400",
                    "color" : "656965"
                },
                {
                    "value": "9800",
                    "color" : "96e0ff"

    
                },
                {
                    "value": "8300",
                    "color" : "ff8f85"

                },
            
            ]
        }
        
    ],  
    
}""")
   return render(request, 'index.html', {'output': chartObj.render()})




def gaugechart(request):

    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = FusionCharts("angulargauge", "ex1" , "100%", "400", "chart-1", "json",
        # The data is passed as a string in the `dataSource` as parameter.
        """{
            "chart": {
               
                "theme": "fusion",
                "chartBottomMargin": "50",
                "showValue": "0",
                "showTickMarks": "0",
                "showTickValues": "0",
                "pivotFillColor": "#ffffff",
                "pivotFillAlpha": "0",
                "showhovereffect": "1",
               "showHoverAnimation": "1",
               "plotHoverEffect" : "1"



                
            },
            "colorRange": {
                "color": [{
                    "minValue": "0",
                    "maxValue": "300",
                    "code": "#26bfff",           
                   

                    
                }
               , {
                    "minValue": "301",
                    "maxValue": "500",
                    "code": "#ff6b5e"
                }, ]
            },
              "dials": {
                "dial": [{
                    "value": "70",
                    "id": "dial1",
                    "radius":"0",
                    "pivotRadius":"0",
                    "rearExtension":"0",
                    
                }]
            }
         
        }"""
        )
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return  render(request, 'index.html', {'output' : angularGauge.render(),'chartTitle': 'Update data at runtime'})


def bubblechart(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = FusionCharts("bubble", "ex1", "70%", "400", "chart-1", "json",
                                """{
                    "chart": {
                    "paletteColors": "#008ee4",
                    "showPlotBorder": "0",
                    "showAlternateHGridColor": "0",
                    "xAxisName": "Month",
                    "yAxisName": "Total Sales",
                    "chartRightMargin": "30",
                    "bgAlpha": "0",
                    "borderAlpha": "20",
                    "canvasBorderAlpha": "0",
                    "plotBorderAlpha": "10",
                    "plotFillAlpha": "70",
                    "captionPadding": "20",
                    "showAxisLines": "1",
                    "axisLineAlpha": "25",
                    "divLineAlpha": "15",
                    "plotFillHoverColor": "#6baa01",
                    "numDivlines": "2",
                    "showTrendlineLabels": "0",
            },
                "categories": [{
                "verticalLineAlpha": "20",
                    "category": [{
                    "label": "Jan",
                        "x": "0"
                }, {
                    "label": "Feb",
                        "x": "1500",
                }, {
                    "label": "Mar",
                        "x": "3000",
                }, {
                    "label": "Apr",
                        "x": "4500",
                }, {
                    "label": "May",
                        "x": "6000",
                }]
            }],
                "dataset": [{
                "data": [ {
                    "x": "911",
                        "y": "500",
                        "z": "13",
                        "name": "Pepsi"
                },
                {
                    "x": "2573",
                        "y": "258",
                        "z": "2",
                        "name": "Coca Cola"
                }]
            }]
                               
                               
                               
                               
                               
                               
                                }"""
                                )
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output': angularGauge.render(), 'chartTitle': 'Update data at runtime'})


def bubblechart2(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = FusionCharts("bubble", "ex1", "70%", "400", "chart-1", "json",
                                """{
                        "chart": {
        "theme": "fusion",
        "caption": "Sales Analysis of Shoe Brands",
        "subcaption": "Last Quarter",
        "xAxisMinValue": "0",
        "xAxisMaxValue": "100",
        "yAxisMinValue": "0",
        "yAxisMaxValue": "30000",
        "plotFillAlpha": "70",
        "plotFillHoverColor": "#6baa01",
        "showPlotBorder": "0",
        "xAxisName": "Average Price",
        "yAxisName": "Units Sold",
        "xNumberPrefix": "$",
        "showValues": "1",
        "showCanvasBorder": "0",
        "showTrendlineLabels": "0",
        "plotTooltext": "$name : Profit Contribution - $zvalue%",
        "adjustVDiv": "1",
        "showXAxisValues": "1",
        "numVDivlines": "5",
        "xAxisValuesStep": "1",
        "vDivlineColor": "ff0000",
        "vDivlineThickness": "5",
        "vDivlineAlpha": "70",
        "vDivlineIsDashed": "1",
        "vDivlineDashLen": "4",
        "vDivlineDashGap": "3",
        "showAlternateVGridColor": "1",
        "alternateVGridColor": "0ffff0",
        "alternateVGridAlpha": "40",
        "valueFontSize": "10"
      },
      "categories": [{
        "category": [{
          "label": "0",
          "x": "0"
        }, {
          "label": "$10",
          "x": "10",
          "showverticalline": "1"
        }, {
          "label": "$30",
          "x": "30",
          "showverticalline": "1"
        }, {
          "label": "$50",
          "x": "50",
          "showverticalline": "1"
        }, {
          "label": "$70",
          "x": "70",
          "showverticalline": "1"
        }, {
          "label": "$90",
          "x": "90",
          "showverticalline": "1"
        }]
      }],
      "dataset": [{
        "color": "#00aee4",
        "data": [{
          "x": "80",
          "y": "15000",
          "z": "24",
          "name": "Nike"
        }, {
          "x": "60",
          "y": "18500",
          "z": "26",
          "name": "Adidas"
        }, {
          "x": "50",
          "y": "19450",
          "z": "19",
          "name": "Puma"
        }, {
          "x": "65",
          "y": "10500",
          "z": "8",
          "name": "Fila"
        }, {
          "x": "43",
          "y": "8750",
          "z": "5",
          "name": "Lotto"
        }, {
          "x": "32",
          "y": "22000",
          "z": "10",
          "name": "Reebok"
        }, {
          "x": "44",
          "y": "13000",
          "z": "9",
          "name": "Woodland"
        }]
      }],
      "trendlines": [{
        "line": [{
          "startValue": "20000",
          "endValue": "30000",
          "isTrendZone": "1",
          "color": "#aaaaaa",
          "alpha": "14"
        }, {
          "startValue": "10000",
          "endValue": "20000",
          "isTrendZone": "1",
          "color": "#aaaaaa",
          "alpha": "7"
        }]
      }]
    
                    

                                }"""
                                )
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output': angularGauge.render(), 'chartTitle': 'Update data at runtime'})
