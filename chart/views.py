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
        "showLegend": "0",
        "formatnumberscale": "0",
        "divLineColor" : "#ffffff"


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
        "theme": "fusion",
        "caption": "Top 5 Products",
        "xAxisMinValue": "0",
        "xAxisMaxValue": "100",
        "yAxisMinValue": "0",
        "yAxisMaxValue": "30000",
        "plotFillAlpha": "70",
        "plotFillHoverColor": "#6baa01",
        "showPlotBorder": "0",
        "xAxisName": "Month",
        "yAxisName": "Total Sales",
        "showValues": "1",
        "showCanvasBorder": "0",
        "showTrendlineLabels": "0",
        "plotTooltext": "$name : Tk $zvalue",
        "adjustVDiv": "1",
        "showXAxisValues": "1",
        "numVDivlines": "5",
        "xAxisValuesStep": "1",
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
        },
        {
          "label": "Jan",
          "x": "10",
          "showverticalline": "1"
        },
        {
          "label": "Feb",
          "x": "30",
          "showverticalline": "1"
        },
        {
          "label": "Mar",
          "x": "50",
          "showverticalline": "1"
        },
        {
          "label": "Apr",
          "x": "70",
          "showverticalline": "1"
        },
        {
          "label": "May",
          "x": "90",
          "showverticalline": "1"
        }]
      }],
      "dataset": [{
        "color": "#00aee4",
        "data": [ {
          "x": "50",
          "y": "19450",
          "z": "19",
          "name": "Lux"
        }, {
          "x": "65",
          "y": "10500",
          "z": "8",
          "name": "Cool Shaving Cream",
           "color" : "ffbf00"

        }, {
          "x": "43",
          "y": "8750",
          "z": "5",
          "name": "Teer Ata",
          "color" : "333333"

        }, {
          "x": "32",
          "y": "22000",
          "z": "10",
          "name": "Coca Cola",
           "color" : "ff6b5e"

        }, {
          "x": "44",
          "y": "13000",
          "z": "9",
          "name": "Pepsi",
          "color" : "96e0ff"
        }]
      }],

                                }"""
                                )

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output': angularGauge.render(), 'chartTitle': 'Update data at runtime'})


def bubblechart2(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor


    global_bubblechart = dict()
    chart_dict= dict()
    chart_dict['theme'] = "fusion"
    chart_dict['caption'] = "Top 5 Products"
    chart_dict['xAxisMinValue'] = "0"
    chart_dict['xAxisMaxValue'] = "100"
    chart_dict['yAxisMinValue'] = "0"
    chart_dict['yAxisMaxValue'] = "30000"
    chart_dict['plotFillAlpha'] = "70"
    chart_dict['plotFillHoverColor'] = "6baa01"
    chart_dict['showPlotBorder'] = "0"
    chart_dict['xAxisName'] = "Month"
    chart_dict['yAxisName'] = "Total Sales"
    chart_dict['showValues'] = "1"
    chart_dict['showCanvasBorder'] = "0"
    chart_dict['showTrendlineLabels'] = "0"
    chart_dict['plotTooltext'] = "$name : Tk $zvalue"
    chart_dict['adjustVDiv'] = "1"
    chart_dict['showXAxisValues'] = "1"
    chart_dict['numVDivlines'] = "5"
    chart_dict['vDivlineThickness'] = "5"
    chart_dict['vDivlineAlpha'] = "70"
    chart_dict['vDivlineIsDashed'] = "1"
    chart_dict['vDivlineDashLen'] = "4"
    chart_dict['vDivlineDashGap'] = "3"
    chart_dict['showAlternateVGridColor'] = "1"
    chart_dict['alternateVGridColor'] = "0ffff0"
    chart_dict['alternateVGridAlpha'] = "40"
    chart_dict['valueFontSize'] = "10"
    global_bubblechart['chart'] = chart_dict

    categories_list = list()
    categories_dict = dict()
    category_list = list()
    category_dict = dict()
    category_dict['label'] = "0"
    category_dict['x'] = "0"
    category_list.append(category_dict)
    category_dict['label'] = "Jan"
    category_dict['x'] = "10"
    category_list.append(category_dict)
    category_dict = dict()
    category_dict['label'] = "Feb"
    category_dict['x'] = "30"
    category_dict['showverticalline'] = "1"
    category_list.append(category_dict)
    category_dict = dict()
    category_dict['label'] = "Mar"
    category_dict['x'] = "50"
    category_dict['showverticalline'] = "1"
    category_list.append(category_dict)
    category_dict = dict()
    category_dict['label'] = "Apr"
    category_dict['x'] = "70"
    category_dict['showverticalline'] = "1"
    category_list.append(category_dict)
    category_dict = dict()
    category_dict['label'] = "May"
    category_dict['x'] = "90"
    category_dict['showverticalline'] = "1"
    category_list.append(category_dict)

    categories_dict['category'] = category_list
    category_list.append(categories_dict)
    global_bubblechart['categories'] = categories_list


    dataset_list = list()
    dataset_dict = dict()
    dataset_dict["x"] = ["50"]
    dataset_dict["y"] = ["19450"]
    dataset_dict["z"] = ["19"]
    dataset_dict["name"] = ["Lux"]
    dataset_list.append(dataset_dict)

    dataset_dict = dict()
    dataset_dict["x"] = ["65"]
    dataset_dict["y"] = ["10500"]
    dataset_dict["z"] = ["8"]
    dataset_dict["name"] = ["Cool Shaving Cream"]
    dataset_dict["color"] = ["ffbf00"]
    dataset_list.append(dataset_dict)


    dataset_dict = dict()
    dataset_dict["x"] = ["43"]
    dataset_dict["y"] = ["8750"]
    dataset_dict["z"] = ["5"]
    dataset_dict["name"] = ["Teer ata"]
    dataset_dict["color"] = ["333333"]
    dataset_list.append(dataset_dict)


    dataset_dict = dict()
    dataset_dict["x"] = ["32"]
    dataset_dict["y"] = ["22000"]
    dataset_dict["z"] = ["10"]
    dataset_dict["name"] = ["Coca Cola"]
    dataset_dict["color"] = ["ff6b5e"]
    dataset_list.append(dataset_dict)



    dataset_dict = dict()
    dataset_dict["x"] = ["44"]
    dataset_dict["y"] = ["13000"]
    dataset_dict["z"] = ["9"]
    dataset_dict["name"] = ["Pepsi"]
    dataset_dict["color"] = ["ffbf00"]
    dataset_list.append(dataset_dict)
    global_bubblechart['dataset'] = dataset_list


    print(global_bubblechart)
    a= FusionCharts("bubble","ex1","70%","400","chart-1","json",global_bubblechart)


    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output': a.render(), 'chartTitle': 'Update data at runtime'})


def ledChart(request):
    angularGauge = FusionCharts("hled", "ex1", "50%", "125", "chart-1", "json",
                                """{
     "chart": {
            "caption": "SUCCESS RATE OF PREVIOUS SMILE PROMOTION",
            "lowerLimit": "0",
            "upperLimit": "100",
            "lowerLimitDisplay": "Empty",
            "upperLimitDisplay": "Full",
            "numberSuffix": "%",
            "valueFontSize": "12",
            "showhovereffect": "1",
            "origW": "400",
            "origH": "150",
            "ledSize": "3",
            "ledGap": "2",
            "manageResize": "1",
            "theme": "fusion"
      },
         "annotations": {
        "showbelow": "1",
        "groups": [
            {
                "id": "indicator",
                "items": [
                    {
                        "id": "bgRectAngle",
                        "type": "rectangle",
                        "alpha": "90",
                        "radius": "1",
                        "fillColor": "#6baa01",
                        "x": "$gaugeCenterX - 20",
                        "tox": "$gaugeCenterX + 20",
                        "y": "$gaugeEndY + 25",
                        "toy": "$gaugeEndY + 45"
                    }
                ]
            }
        ]
    },
    "colorRange": {
        "color": [
            {
                "minValue": "0",
                "maxValue": "45",
                "code": "#e44a00"
            },
            {
                "minValue": "45",
                "maxValue": "75",
                "code": "#f8bd19"
            },
            {
                "minValue": "75",
                "maxValue": "100",
                "code": "#6baa01"
            }
        ]
    },
    "value": "92"

    
                                }"""
                                )
    angularGauge2 = FusionCharts("hled", "ex2", "50%", "100", "chart-2", "json",
                                """{
     "chart": {
            "lowerLimit": "0",
            "upperLimit": "100",
            "lowerLimitDisplay": "Empty",
            "upperLimitDisplay": "Full",
            "numberSuffix": "%",
            "valueFontSize": "12",
            "showhovereffect": "1",
            "origW": "400",
            "origH": "150",
            "ledSize": "3",
            "ledGap": "2",
            "manageResize": "1",
            "theme": "fusion"
      },
         "annotations": {
        "showbelow": "1",
        "groups": [
            {
                "id": "indicator",
                "items": [
                    {
                        "id": "bgRectAngle",
                        "type": "rectangle",
                        "alpha": "90",
                        "radius": "1",
                        "fillColor": "#6baa01",
                        "x": "$gaugeCenterX - 20",
                        "tox": "$gaugeCenterX + 20",
                        "y": "$gaugeEndY + 25",
                        "toy": "$gaugeEndY + 45"
                    }
                ]
            }
        ]
    },
    "colorRange": {
        "color": [
            {
                "minValue": "0",
                "maxValue": "45",
                "code": "#e44a00"
            },
            {
                "minValue": "45",
                "maxValue": "75",
                "code": "#f8bd19"
            },
            {
                "minValue": "75",
                "maxValue": "100",
                "code": "#6baa01"
            }
        ]
    },
    "value": "92"


                                }"""
                                )


    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'led_chart.html', {'output': angularGauge.render(),
                                              'output2':angularGauge2.render(),
                                              })


def ledChart2(request):
    angularGauge = FusionCharts("hled", "ex1", "25%", "170", "chart-1", "json",
                                """{
     "chart": {
            "caption": "SUCCESS RATE OF PREVIOUS SMILE PROMOTION",
            "subcaption" : "Buy 1 get 1 ",
            "gaugeFillColor": "#ffffff",

            "lowerLimit": "0",
            "upperLimit": "100",
            "numberSuffix": "%",
            "showhovereffect": "1",
            "origW": "400",
            "origH": "150",
            "ledSize": "5",
            "ledGap": "0",
            "theme": "fusion",
            "plotTooltext": "Buy 1 get 1 ",
            "showTickMarks": "0",
            "showTickValues": "0",
            "showGaugeBorder": "0",
            "showValue": "0",
            "showHoverEffect":"1",
      
      },
         "annotations": {
        "showbelow": "1",
     
     
    },
    "colorRange": {
        "color": [
            {
                "minValue": "0",
                "maxValue": "10",
                "code": "#1589B9"
            },
            {
                "minValue": "10",
                "maxValue": "15",
                "code": "#ffffff"
            },
            {
                "minValue": "15",
                "maxValue": "25",
                "code": "#1589B9"
            },
             {
                "minValue": "25",
                "maxValue": "30",
                "code": "#ffffff"
            },
             {
                "minValue": "30",
                "maxValue": "40",
                "code": "#1589B9"
            },
             {
                "minValue": "40",
                "maxValue": "45",
                "code": "#ffffff"
            },
             {
                "minValue": "45",
                "maxValue": "55",
                "code": "#1589B9"
            },
             {
                "minValue": "55",
                "maxValue": "60",
                "code": "#ffffff"
            },
             {
                "minValue": "60",
                "maxValue": "70",
                "code": "#1589B9"
            },    {
                "minValue": "70",
                "maxValue": "75",
                "code": "#ffffff"
            },
             {
                "minValue": "75",
                "maxValue": "85",
                "code": "#1589B9"
            },
             {
                "minValue": "85",
                "maxValue": "90",
                "code": "#ffffff"
            },
             {
                "minValue": "90",
                "maxValue": "100",
                "code": "#1589B9"
            },
      
           
           
            
         
        ]
    },
    "value": "70"


                                }"""
                                )
    angularGauge2 = FusionCharts("hled", "ex2", "25%", "155", "chart-2", "json",
                                """{
     "chart": {
            "subcaption" : "Free Product     ",
            "lowerLimit": "0",
            "upperLimit": "100",
            "numberSuffix": "%",
            "gaugeFillColor": "#ffffff",
            "showhovereffect": "1",
            "origW": "400",
            "origH": "150",
            "ledSize": "5",
            "ledGap": "0",
            "theme": "fusion",
            "plotTooltext": "Free Product",
            "showTickMarks": "0",
            "showTickValues": "0",
            "showGaugeBorder": "0",
            "showValue": "0",
            "showHoverEffect":"1",

      },
         "annotations": {
        "showbelow": "1",


    },
    "colorRange": {
        "color": [
            {
                "minValue": "0",
                "maxValue": "10",
                "code": "#1589B9"
            },
            {
                "minValue": "10",
                "maxValue": "15",
                "code": "#ffffff"
            },
            {
                "minValue": "15",
                "maxValue": "25",
                "code": "#1589B9"
            },
             {
                "minValue": "25",
                "maxValue": "30",
                "code": "#ffffff"
            },
             {
                "minValue": "30",
                "maxValue": "40",
                "code": "#1589B9"
            },
             {
                "minValue": "40",
                "maxValue": "45",
                "code": "#ffffff"
            },
             {
                "minValue": "45",
                "maxValue": "55",
                "code": "#1589B9"
            },
             {
                "minValue": "55",
                "maxValue": "60",
                "code": "#ffffff"
            },
             {
                "minValue": "60",
                "maxValue": "70",
                "code": "#1589B9"
            },    {
                "minValue": "70",
                "maxValue": "75",
                "code": "#ffffff"
            },
             {
                "minValue": "75",
                "maxValue": "85",
                "code": "#1589B9"
            },
             {
                "minValue": "85",
                "maxValue": "90",
                "code": "#ffffff"
            },
             {
                "minValue": "90",
                "maxValue": "100",
                "code": "#1589B9"
            },




        ]
    },
    "value": "81",
    


                                }"""
                                )
    angularGauge3 = FusionCharts("hled", "ex3", "25%", "155", "chart-3", "json",
                                """{
     "chart": {
            "subcaption" : "Tk 5 Off",
            "subcaption" : "Tk 5 Off",
            "subcaptionAlignment" : "left",
            "gaugeFillColor": "#ffffff",
          
            "lowerLimit": "0",
            "upperLimit": "100",
            "numberSuffix": "%",
            "showhovereffect": "1",
            "origW": "400",
            "origH": "150",
            "ledSize": "3",
            "ledGap": "0",
            "theme": "fusion",
            "plotTooltext": "Tk 5 Off",
            "showTickMarks": "0",
            "showTickValues": "0",
            "showGaugeBorder": "0",
            "showValue": "0",
            "showHoverEffect":"1",

      },
      
         "annotations": {
        "showbelow": "1",
       


    },
    "colorRange": {
        "color": [
            {
                "minValue": "0",
                "maxValue": "10",
                "code": "#1589B9"
            },
            {
                "minValue": "10",
                "maxValue": "15",
                "code": "#ffffff"
            },
            {
                "minValue": "15",
                "maxValue": "25",
                "code": "#1589B9"
            },
             {
                "minValue": "25",
                "maxValue": "30",
                "code": "#ffffff"
            },
             {
                "minValue": "30",
                "maxValue": "40",
                "code": "#1589B9"
            },
             {
                "minValue": "40",
                "maxValue": "45",
                "code": "#ffffff"
            },
             {
                "minValue": "45",
                "maxValue": "55",
                "code": "#1589B9"
            },
             {
                "minValue": "55",
                "maxValue": "60",
                "code": "#ffffff"
            },
             {
                "minValue": "60",
                "maxValue": "70",
                "code": "#1589B9"
            },    {
                "minValue": "70",
                "maxValue": "75",
                "code": "#ffffff"
            },
             {
                "minValue": "75",
                "maxValue": "85",
                "code": "#1589B9"
            },
             {
                "minValue": "85",
                "maxValue": "90",
                "code": "#ffffff"
            },
             {
                "minValue": "90",
                "maxValue": "100",
                "code": "#1589B9"
            },




        ]
    },
    "value": "34"


                                }"""
                                )

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'led_chart.html', {'output': angularGauge.render(),
                                              'output2': angularGauge2.render(),
                                              'output3': angularGauge3.render(),


                                              })

def chart2(request):

  # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
  dataSource = OrderedDict()

  # The `mapConfig` dict contains key-value pairs data for chart attribute
  mapConfig = OrderedDict()
  mapConfig["caption"] = "Average Statistics"
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
  # dataSource["colorrange"] = colorDataObj
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


  # Create an object for the world map using the FusionCharts class constructor
  # The chart data is passed to the `dataSource` parameter.
  fusionMap = FusionCharts("maps/bangladesh", "ex1" , "80%", "950", "chart-1", "json", dataSource)

  # returning complete JavaScript and HTML code, which is used to generate map in the browsers.
  return  render(request, 'index.html', {'output' : fusionMap.render(), 'chartTitle': 'Simple Map Using Array'})
