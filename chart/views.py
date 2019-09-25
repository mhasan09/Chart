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
      "displayValue" : "abc"
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
                    "color" : "333333",
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

def bubblechart3(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor




    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'test4.html')

def bubblechart4(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor




    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'test_bubble.html')




def ledChart(request):
    angularGauge = FusionCharts("hled", "ex1", "25%", "170", "chart-1", "json",
                                """{
     "chart": {
            "caption": "SUCCESS RATE OF PREVIOUS SMILE PROMOTION",
            "subcaption" : "Buy 1 get 1",
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
            "plotTooltext": "$value%",
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
            "plotTooltext": "$value%",
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
            "plotTooltext": "$value%",
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


def ledChart2(request):
    angularGauge = FusionCharts("hled", "ex1", "85%", "155", "chart-1", "json",
                                """{
     "chart": {
        
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
            "plotTooltext": "$value%",
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
    angularGauge2 = FusionCharts("hled", "ex2", "85%", "155", "chart-2", "json",
                                 """{
      "chart": {
             
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
             "plotTooltext": "$value%",
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
    angularGauge3 = FusionCharts("hled", "ex3", "85%", "155", "chart-3", "json",
                                 """{
      "chart": {
             
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
             "plotTooltext": "$value%",
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
    return render(request, 'led2.html', {'output': angularGauge.render(),
                                              'output2': angularGauge2.render(),
                                              'output3': angularGauge3.render(),

                                              })


def chart2(request):

  # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
  dataSource = OrderedDict()

  # The `mapConfig` dict contains key-value pairs data for chart attribute
  mapConfig = OrderedDict()
  mapConfig["caption"] = "Average Promotion Statistics"
  mapConfig["subcaption"] = "2019"
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
    ["BA", "0.82", "1"],
    ["CG", "2.04", "1"],
    ["DA", "1.78", "1"],
    ["KH", "0.40", "1"],
    ["RS", "2.58", "1"],
    ["RP", "1.30", "1"],
    ["SY", "1.30", "1"],

  ]




  # Create an object for the world map using the FusionCharts class constructor
  # The chart data is passed to the `dataSource` parameter.
  fusionMap = FusionCharts("maps/bangladesh", "ex1" , "80%", "950", "chart-1", "json", dataSource)

  # returning complete JavaScript and HTML code, which is used to generate map in the browsers.
  return  render(request, 'index.html', {'output' : fusionMap.render(), 'chartTitle': 'Simple Map Using Array'})

def chart3(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = FusionCharts("maps/world", "ex1", "70%", "950", "chart-1", "json",
                                """{
     
    "chart": {
        "caption": "World Population Density",
        "subcaption": "Number of people per Square Mile",
        "theme": "fusion",
        "formatNumberScale": "0",
        "showLabels": "1",
        "nullEntityColor": "#C2C2D6",
        "nullEntityAlpha": "50",
        "hoverOnNull": "0",
        "useSNameInLabels": "0",
        "entityFillColor": "#A8A8A8",
        "entityFillHoverColor": "#E5E5E9"
    },
    "colorrange": {
        "startlabel": "Low",
        "endlabel": "High",
        "code": "#e44a00",
        "minvalue": "0",
        "gradient": "1",
        "color": [{
            "maxvalue": "60",
            "displayvalue": "Average",
            "code": "#f8bd19"
        },
        {
            "maxvalue": "300",
            "code": "#6baa01"
        }]
    },
    "data": [{
        "id": "NA",
        "displayValue": "North America",
        "value": "57.2",
        "link": "newchart-json-NA"
    },
    {
        "id": "SA",
        "value": "57.1",
        "showLabel": "1"
    },
    {
        "id": "AS",
        "value": "247",
        "showLabel": "1"
    },
    {
        "id": "EU",
        "value": "188.5",
        "showLabel": "1"
    },
    {
        "id": "AF",
        "value": "87.2",
        "showLabel": "1"
    },
    {
        "id": "AU",
        "value": "8.32",
        "showLabel": "1"
    }],
    "linkeddata": [{
        "id": "NA",
        "linkedchart": {
            "chart": {
                "caption": "US Population Density by State",
                "subcaption": "Number of people per Square Mile",
                "entityFillHoverColor": "#E5E5E9",
                "showLabels": "1",
                "entityFillColor": "#A8A8A8",
                "theme": "fusion",
                "showBorder": "1",
                "bordercolor": "#FFFFFF",
                "entityborderThickness": "3"
            },
            "colorrange": {
                "startlabel": "Low",
                "endlabel": "High",
                "code": "#e44a00",
                "minvalue": "0",
                "gradient": "1",
                "color": [{
                    "maxvalue": "150",
                    "displayvalue": "Average",
                    "code": "#f8bd19"
                }, {
                    "maxvalue": "600",
                    "code": "#6baa01"
                }]
            },
            "data": [{
                "id": "HI",
                "value": "99"
            },
            {
                "id": "DC",
                "value": "99"
            },
            {
                "id": "MD",
                "value": "90"
            },
            {
                "id": "DE",
                "value": "96"
            },
            {
                "id": "RI",
                "value": "90"
            },
            {
                "id": "WA",
                "value": "228"
            },
            {
                "id": "OR",
                "value": "105"
            },
            {
                "id": "CA",
                "value": "221"
            },
            {
                "id": "AK",
                "value": "260"
            },
            {
                "id": "ID",
                "value": "396"
            },
            {
                "id": "NV",
                "value": "169"
            },
            {
                "id": "AZ",
                "value": "435"
            },
            {
                "id": "MT",
                "value": "445"
            },
            {
                "id": "WY",
                "value": "455"
            },
            {
                "id": "UT",
                "value": "227"
            },
            {
                "id": "CO",
                "value": "214"
            },
            {
                "id": "NM",
                "value": "196"
            },
            {
                "id": "ND",
                "value": "331"
            },
            {
                "id": "SD",
                "value": "374"
            },
            {
                "id": "NE",
                "value": "329"
            },
            {
                "id": "KS",
                "value": "231"
            },
            {
                "id": "OK",
                "value": "150"
            },
            {
                "id": "TX",
                "value": "202"
            },
            {
                "id": "MN",
                "value": "137"
            },
            {
                "id": "IA",
                "value": "143"
            },
            {
                "id": "MO",
                "value": "424"
            },
            {
                "id": "AR",
                "value": "485"
            },
            {
                "id": "LA",
                "value": "124"
            },
            {
                "id": "WI",
                "value": "181"
            },
            {
                "id": "IL",
                "value": "120"
            },
            {
                "id": "KY",
                "value": "309"
            },
            {
                "id": "TN",
                "value": "250"
            },
            {
                "id": "MS",
                "value": "351"
            },
            {
                "id": "AL",
                "value": "271"
            },
            {
                "id": "GA",
                "value": "124"
            },
            {
                "id": "MI",
                "value": "120"
            },
            {
                "id": "IN",
                "value": "205"
            },
            {
                "id": "OH",
                "value": "476"
            },
            {
                "id": "PA",
                "value": "445"
            },
            {
                "id": "NY",
                "value": "369"
            },
            {
                "id": "VT",
                "value": "322"
            },
            {
                "id": "NH",
                "value": "216"
            },
            {
                "id": "ME",
                "value": "404"
            },
            {
                "id": "MA",
                "value": "165"
            },
            {
                "id": "CT",
                "value": "316"
            },
            {
                "id": "NJ",
                "value": "553"
            },
            {
                "id": "WV",
                "value": "560"
            },
            {
                "id": "VA",
                "value": "565"
            },
            {
                "id": "NC",
                "value": "534"
            },
            {
                "id": "SC",
                "value": "503"
            },
            {
                "id": "FL",
                "value": "503"
            }]
        }
    }]

    
                                }"""
                                )

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output': angularGauge.render()  ,'chartTitle': 'Update data at runtime'})


def chart4(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = FusionCharts("maps/bangladesh", "ex1", "70%", "950", "chart-1", "json",
                                """{

    "chart": {
        "caption": "Promotion Campaign",
        "theme": "fusion",
        "formatNumberScale": "0",
        "showLabels": "1",
        "nullEntityColor": "#C2C2D6",
        "nullEntityAlpha": "50",
        "hoverOnNull": "0",
        "useSNameInLabels": "0",
        "entityFillColor": "#A8A8A8",
        "entityFillHoverColor": "#E5E5E9"
    },
    "colorrange": {
        "startlabel": "Low",
        "endlabel": "High",
        "code": "#e44a00",
        "minvalue": "0",
        "gradient": "1",
        "color": [{
            "maxvalue": "60",
            "displayvalue": "Average",
            "code": "#f8bd19"
        },
        {
            "maxvalue": "300",
            "code": "#6baa01"
        }]
    },
    "data": [{
        "id": "BD.SY",
        "displayValue": "Sylhet",
        "value": "57.2",
        "link": "newchart-json-BD.SY"
    },
    {
        "id": "BD.DA",
        "value": "57.1",
        "showLabel": "1"
    },
    {
        "id": "BD.KH",
        "value": "247",
        "showLabel": "1"
    },
    {
        "id": "BD.RS",
        "value": "188.5",
        "showLabel": "1"
    },
    {
        "id": "BD.BA",
        "value": "87.2",
        "showLabel": "1"
    },
     {
        "id": "BD.CG",
        "value": "87.2",
        "showLabel": "1"
    },
    {
        "id": "BD.RP",
        "value": "8.32",
        "showLabel": "1"
    }],
    "linkeddata": [{
        "id": "BD.SY",
        "linkedchart": {
            "chart": {
                "caption": "SYLHET",
                "entityFillHoverColor": "#E5E5E9",
                "showLabels": "1",
                "entityFillColor": "#A8A8A8",
                "theme": "fusion",
                "showBorder": "1",
                "bordercolor": "#FFFFFF",
                "entityborderThickness": "3"
            },
            "colorrange": {
                "startlabel": "Low",
                "endlabel": "High",
                "code": "#e44a00",
                "minvalue": "0",
                "gradient": "1",
                "color": [{
                    "maxvalue": "150",
                    "displayvalue": "Average",
                    "code": "#f8bd19"
                }, {
                    "maxvalue": "600",
                    "code": "#6baa01"
                }]
            },
            "data": [{
                "id": "BD.SY.HA",
                "value": "99"
            },
            {
                "id": "BD.SY.MB",
                "value": "99"
            },
            {
                "id": "BD.SY.SN",
                "value": "90"
            },
            {
                "id": "BD.SY.SL",
                "value": "96"
            },
            
            ]
        }
    }]


                                }"""
                                )

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output': angularGauge.render(), 'chartTitle': 'Update data at runtime'})

def chart5(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = FusionCharts("maps/bangladesh", "ex1", "70%", "950", "chart-1", "json",
                                """{
                                "chart": {
        "caption": "Promotion Campaign",
        "theme": "fusion",
        "showLabels": "1",
        "nullEntityColor": "#C2C2D6",
        "nullEntityAlpha": "50",
        "hoverOnNull": "0",
        "useSNameInLabels": "0",
        "entityFillColor": "#A8A8A8",
        "entityFillHoverColor": "#E5E5E9",
        "showLegend" : "0"
    },
    "colorrange": {
        "startlabel": "Low",
        "endlabel": "High",
        "code": "#e44a00",
        "minvalue": "0",
        "gradient": "0",
        "color": [{
            "maxvalue": "60",
            "displayvalue": "Average",
            "code": "#f8bd19"
        },
        {
            "maxvalue": "300",
            "code": "#6baa01"
        }]
    },
    "data": [{
        "id": "BD.SY",
        "displayValue": "Sylhet",
        "value": "57.2",
        "link": "http://127.0.0.1:7000/sylhet"
    },
    {
        "id": "BD.DA",
        "value": "57.1",
        "showLabel": "1",
         "link": "http://127.0.0.1:7000/dhaka"
    },
       {
        "id": "BD.DA.FR",
        "value": "57.1",
        "showLabel": "1",
    },
    {
        "id": "BD.KH",
        "value": "247",
        "showLabel": "1",
         "link": "http://127.0.0.1:7000/khulna"
    },
    {
        "id": "BD.RS",
        "value": "188.5",
        "showLabel": "1",
         "link": "http://127.0.0.1:7000/rajshahi"
    },
    {
        "id": "BD.BA",
        "value": "87.2",
        "showLabel": "1",
         "link": "http://127.0.0.1:7000/barisal"
    },
     {
        "id": "BD.CG",
        "value": "87.2",
        "showLabel": "1",
         "link": "http://127.0.0.1:7000/chittagong"
    },
    {
        "id": "BD.RP",
        "value": "8.32",
        "showLabel": "1",
         "link": "http://127.0.0.1:7000/rangpur"
    },
      {
        "id": "BD.MM",
        "value": "8.32",
        "showLabel": "1",
         "link": "http://127.0.0.1:7000/mymensingh"
    }
    ]
     

                                }"""
                                )

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output': angularGauge.render(), 'chartTitle': 'Update data at runtime'})





def barisal(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = FusionCharts("maps/barisal", "ex1", "70%", "950", "chart-1", "json",
                                """{
     "chart": {
         "caption": "Barisal",
            "subcaption": " 2019",
            "numbersuffix": "%",
            "includevalueinlabels": "1",
            "labelsepchar": ": ",
            "entityFillHoverColor": "#FFF9C4",
            "theme": "fusion"
      },
      "colorrange": {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "0",
        "color": [{
            "minvalue": "0.5",
            "maxvalue": "1.0",
            "color": "#FFD74D"
        }, {
            "minvalue": "1.0",
            "maxvalue": "2.0",
            "color": "#FB8C00"
        }, {
            "minvalue": "2.0",
            "maxvalue": "3.0",
            "color": "#E65100"
        }]
    },
    "data": [{
        "id": "NA",
        "value": ".82",
        "showLabel": "1"
    }, {
        "id": "SA",
        "value": "2.04",
        "showLabel": "1"
    }, {
        "id": "AS",
        "value": "1.78",
        "showLabel": "1"
    }, {
        "id": "EU",
        "value": ".40",
        "showLabel": "1"
    }, {
        "id": "AF",
        "value": "2.58",
        "showLabel": "1"
    }, {
        "id": "AU",
        "value": "1.30",
        "showLabel": "1"
    }]

                                }"""
                                )

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output': angularGauge.render(), 'chartTitle': 'Update data at runtime'})

def mymensingh(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = FusionCharts("maps/mymensingh", "ex1", "70%", "950", "chart-1", "json",
                                """{
     "chart": {
         "caption": "Mymensingh",
            "subcaption": " 2019",
            "numbersuffix": "%",
            "includevalueinlabels": "1",
            "labelsepchar": ": ",
            "entityFillHoverColor": "#FFF9C4",
            "theme": "fusion"
      },
      "colorrange": {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "0",
        "color": [{
            "minvalue": "0.5",
            "maxvalue": "1.0",
            "color": "#FFD74D"
        }, {
            "minvalue": "1.0",
            "maxvalue": "2.0",
            "color": "#FB8C00"
        }, {
            "minvalue": "2.0",
            "maxvalue": "3.0",
            "color": "#E65100"
        }]
    },
    "data": [{
        "id": "NA",
        "value": ".82",
        "showLabel": "1"
    }, {
        "id": "SA",
        "value": "2.04",
        "showLabel": "1"
    }, {
        "id": "AS",
        "value": "1.78",
        "showLabel": "1"
    }, {
        "id": "EU",
        "value": ".40",
        "showLabel": "1"
    }, {
        "id": "AF",
        "value": "2.58",
        "showLabel": "1"
    }, {
        "id": "AU",
        "value": "1.30",
        "showLabel": "1"
    }]

                                }"""
                                )

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output': angularGauge.render(), 'chartTitle': 'Update data at runtime'})


def dhaka(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = FusionCharts("maps/dhaka", "ex1", "70%", "950", "chart-1", "json",
                                """{
     "chart": {
         "caption": "Dhaka",
            "subcaption": " 2019",
            "numbersuffix": "%",
            "includevalueinlabels": "1",
            "labelsepchar": ": ",
            "entityFillHoverColor": "#FFF9C4",
            "theme": "fusion",
            "showLegend" : "0"

      },
      "colorrange": {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "0",
        "color": [{
            "minvalue": "0.5",
            "maxvalue": "1.0",
            "color": "#FFD74D"
        }, {
            "minvalue": "1.0",
            "maxvalue": "2.0",
            "color": "#FB8C00"
        }, {
            "minvalue": "2.0",
            "maxvalue": "3.0",
            "color": "#E65100"
        }]
    },
    "data": [{
        "id": "NA",
        "value": ".82",
        "showLabel": "1"
    }, {
        "id": "SA",
        "value": "2.04",
        "showLabel": "1"
    }, {
        "id": "AS",
        "value": "1.78",
        "showLabel": "1"
    }, {
        "id": "EU",
        "value": ".40",
        "showLabel": "1"
    }, {
        "id": "AF",
        "value": "2.58",
        "showLabel": "1"
    }, {
        "id": "AU",
        "value": "1.30",
        "showLabel": "1"
    }]

                                }"""
                                )

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output': angularGauge.render(), 'chartTitle': 'Update data at runtime'})

def rajshahi(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = FusionCharts("maps/rajshahi", "ex1", "70%", "950", "chart-1", "json",
                                """{
     "chart": {
         "caption": "Rajshahi",
            "subcaption": " 2019",
            "numbersuffix": "%",
            "includevalueinlabels": "1",
            "labelsepchar": ": ",
            "entityFillHoverColor": "#FFF9C4",
            "theme": "fusion",
            "showLegend" : "0"

      },
      "colorrange": {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "0",
        "color": [{
            "minvalue": "0.5",
            "maxvalue": "1.0",
            "color": "#FFD74D"
        }, {
            "minvalue": "1.0",
            "maxvalue": "2.0",
            "color": "#FB8C00"
        }, {
            "minvalue": "2.0",
            "maxvalue": "3.0",
            "color": "#E65100"
        }]
    },
    "data": [{
        "id": "NA",
        "value": ".82",
        "showLabel": "1"
    }, {
        "id": "SA",
        "value": "2.04",
        "showLabel": "1"
    }, {
        "id": "AS",
        "value": "1.78",
        "showLabel": "1"
    }, {
        "id": "EU",
        "value": ".40",
        "showLabel": "1"
    }, {
        "id": "AF",
        "value": "2.58",
        "showLabel": "1"
    }, {
        "id": "AU",
        "value": "1.30",
        "showLabel": "1"
    }]

                                }"""
                                )

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output': angularGauge.render(), 'chartTitle': 'Update data at runtime'})

def khulna(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = FusionCharts("maps/khulna", "ex1", "70%", "950", "chart-1", "json",
                                """{
     "chart": {
         "caption": "Khulna",
            "subcaption": " 2019",
            "numbersuffix": "%",
            "includevalueinlabels": "1",
            "labelsepchar": ": ",
            "entityFillHoverColor": "#FFF9C4",
            "theme": "fusion",
            "showLegend" : "0"

      },
      "colorrange": {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "0",
        "color": [{
            "minvalue": "0.5",
            "maxvalue": "1.0",
            "color": "#FFD74D"
        }, {
            "minvalue": "1.0",
            "maxvalue": "2.0",
            "color": "#FB8C00"
        }, {
            "minvalue": "2.0",
            "maxvalue": "3.0",
            "color": "#E65100"
        }]
    },
    "data": [{
        "id": "NA",
        "value": ".82",
        "showLabel": "1"
    }, {
        "id": "SA",
        "value": "2.04",
        "showLabel": "1"
    }, {
        "id": "AS",
        "value": "1.78",
        "showLabel": "1"
    }, {
        "id": "EU",
        "value": ".40",
        "showLabel": "1"
    }, {
        "id": "AF",
        "value": "2.58",
        "showLabel": "1"
    }, {
        "id": "AU",
        "value": "1.30",
        "showLabel": "1"
    }]

                                }"""
                                )

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output': angularGauge.render(), 'chartTitle': 'Update data at runtime'})

def sylhet(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = FusionCharts("maps/sylhet", "ex1", "70%", "950", "chart-1", "json",
                                """{
     "chart": {
         "caption": "Sylhet",
            "subcaption": " 2019",
            "numbersuffix": "%",
            "includevalueinlabels": "1",
            "labelsepchar": ": ",
            "entityFillHoverColor": "#FFF9C4",
            "theme": "fusion",
            "showLegend" : "0"

      },
      "colorrange": {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "0",
        "color": [{
            "minvalue": "0.5",
            "maxvalue": "1.0",
            "color": "#FFD74D"
        }, {
            "minvalue": "1.0",
            "maxvalue": "2.0",
            "color": "#FB8C00"
        }, {
            "minvalue": "2.0",
            "maxvalue": "3.0",
            "color": "#E65100"
        }]
    },
    "data": [{
        "id": "NA",
        "value": ".82",
        "showLabel": "1"
    }, {
        "id": "SA",
        "value": "2.04",
        "showLabel": "1"
    }, {
        "id": "AS",
        "value": "1.78",
        "showLabel": "1"
    }, {
        "id": "EU",
        "value": ".40",
        "showLabel": "1"
    }, {
        "id": "AF",
        "value": "2.58",
        "showLabel": "1"
    }, {
        "id": "AU",
        "value": "1.30",
        "showLabel": "1"
    }]

                                }"""
                                )

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output': angularGauge.render(), 'chartTitle': 'Update data at runtime'})

def mymensingh(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = FusionCharts("maps/mymensingh", "ex1", "70%", "950", "chart-1", "json",
                                """{
     "chart": {
         "caption": "Mymensingh",
            "subcaption": " 2019",
            "numbersuffix": "%",
            "includevalueinlabels": "1",
            "labelsepchar": ": ",
            "entityFillHoverColor": "#FFF9C4",
            "theme": "fusion",
            "showLegend" : "0"

      },
      "colorrange": {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "0",
        "color": [{
            "minvalue": "0.5",
            "maxvalue": "1.0",
            "color": "#FFD74D"
        }, {
            "minvalue": "1.0",
            "maxvalue": "2.0",
            "color": "#FB8C00"
        }, {
            "minvalue": "2.0",
            "maxvalue": "3.0",
            "color": "#E65100"
        }]
    },
    "data": [{
        "id": "NA",
        "value": ".82",
        "showLabel": "1"
    }, {
        "id": "SA",
        "value": "2.04",
        "showLabel": "1"
    }, {
        "id": "AS",
        "value": "1.78",
        "showLabel": "1"
    }, {
        "id": "EU",
        "value": ".40",
        "showLabel": "1"
    }, {
        "id": "AF",
        "value": "2.58",
        "showLabel": "1"
    }, {
        "id": "AU",
        "value": "1.30",
        "showLabel": "1"
    }]

                                }"""
                                )

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output': angularGauge.render(), 'chartTitle': 'Update data at runtime'})

def rangpur(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = FusionCharts("maps/rangpur", "ex1", "70%", "950", "chart-1", "json",
                                """{
     "chart": {
         "caption": "Rangpur",
            "subcaption": " 2019",
            "numbersuffix": "%",
            "includevalueinlabels": "1",
            "labelsepchar": ": ",
            "entityFillHoverColor": "#FFF9C4",
            "theme": "fusion",
            "showLegend" : "0"

      },
      "colorrange": {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "0",
        "color": [{
            "minvalue": "0.5",
            "maxvalue": "1.0",
            "color": "#FFD74D"
        }, {
            "minvalue": "1.0",
            "maxvalue": "2.0",
            "color": "#FB8C00"
        }, {
            "minvalue": "2.0",
            "maxvalue": "3.0",
            "color": "#E65100"
        }]
    },
    "data": [{
        "id": "NA",
        "value": ".82",
        "showLabel": "1"
    }, {
        "id": "SA",
        "value": "2.04",
        "showLabel": "1"
    }, {
        "id": "AS",
        "value": "1.78",
        "showLabel": "1"
    }, {
        "id": "EU",
        "value": ".40",
        "showLabel": "1"
    }, {
        "id": "AF",
        "value": "2.58",
        "showLabel": "1"
    }, {
        "id": "AU",
        "value": "1.30",
        "showLabel": "1"
    }]

                                }"""
                                )

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output': angularGauge.render(), 'chartTitle': 'Update data at runtime'})

def chittagong(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = FusionCharts("maps/chittagong", "ex1", "70%", "950", "chart-1", "json",
                                """{
     "chart": {
         "caption": "Chittagong",
            "subcaption": " 2019",
            "numbersuffix": "%",
            "includevalueinlabels": "1",
            "labelsepchar": ": ",
            "entityFillHoverColor": "#FFF9C4",
            "theme": "fusion",
            "showLegend" : "0",
            "showLegend" : "0"


      },
      "colorrange": {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "0",
        "color": [{
            "minvalue": "0.5",
            "maxvalue": "1.0",
            "color": "#FFD74D"
        }, {
            "minvalue": "1.0",
            "maxvalue": "2.0",
            "color": "#FB8C00"
        }, {
            "minvalue": "2.0",
            "maxvalue": "3.0",
            "color": "#E65100"
        }]
    },
    "data": [{
        "id": "NA",
        "value": ".82",
        "showLabel": "1",
    
    }, {
        "id": "SA",
        "value": "2.04",
        "showLabel": "1"
    }, {
        "id": "AS",
        "value": "1.78",
        "showLabel": "1"
    }, {
        "id": "EU",
        "value": ".40",
        "showLabel": "1"
    }, {
        "id": "AF",
        "value": "2.58",
        "showLabel": "1"
    }, {
        "id": "AU",
        "value": "1.30",
        "showLabel": "1"
    }]

                                }"""
                                )

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output': angularGauge.render(), 'chartTitle': 'Update data at runtime'})

def linkedchart(request):
    return render(request,"bdmap.html")

def bubble_slide(request):
    return render(request,"slider_bubbles.html")

def svg_map(request):
    return render(request,"map_svg.html")

def table(request):
    return render(request,"table2.html")


def svgid(request):
    return render(request,"svg_id.html")

def fetch_svg(request):
    return render(request,"fetchfrommap.html")

def drillDown(request):
    return render(request,'drill-down.html')