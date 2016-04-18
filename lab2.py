from spyre import server
import pandas as pd
import  urllib.request
import  urllib.error
import json
from matplotlib import pyplot as plt
import numpy as np

class RegionsApp(server.App):
    title = "Стан рослинного покрову в Україні"

    inputs = [{"type": 'dropdown',
               "label": "Індекс",
               "options": [{"label": 'VCI', "value": "VCI"},
                           {"label": 'TCI', "value": "TCI"},
                           {"label": 'VHI', "value": "VHI"}],
               "key": 'index',
               "action_id": "update_data"
               },
              {"type": 'dropdown',
               "label": 'Регіон',
               "options":[{"label": "Вінницька обл.", "value": '24'},
                          {"label": "Волинська обл.", "value": '25'},
                          {"label": "Дніпропетровська обл.", "value": '5'},
                          {"label": "Донецька обл.", "value": '6'},
                          {"label": "Житомирська обл.", "value": '27'},
                          {"label": "Закарпатська обл.", "value": '23'},
                          {"label": "Запорізька обл.", "value": '26'},
                          {"label": "Івано-Франківська обл.", "value": '7'},
                          {"label": "Київська обл.", "value": '11'},
                          {"label": "Кіровоградська обл.", "value": '13'},
                          {"label": "Луганська обл.", "value": '14'},
                          {"label": "Львівська обл.", "value": '15'},
                          {"label": "Миколаївська обл.", "value": '16'},
                          {"label": "Одеська обл.", "value": '17'},
                          {"label": "Полтавська обл.", "value": '18'},
                          {"label": "Рівенська обл.", "value": '19'},
                          {"label": "Сумська обл.", "value": '21'},
                          {"label": "Тернопільська обл.", "value": '22'},
                          {"label": "Харківська обл.", "value": '8'},
                          {"label": "Херсонська обл.", "value": '9'},
                          {"label": "Хмельницька обл.", "value": '10'},
                          {"label": "Черкаська обл.", "value": '1'},
                          {"label": "Чернівецька обл.", "value": '3'},
                          {"label": "Чернігівська обл.", "value": '2'},
                          {"label": "АР Крим", "value": '4'},
                          {"label": "м.Київ", "value": '12'},
                          {"label": "м.Севастополь", "value": '20'},
                          ],
               "key": 'region',
               "action_id": "update_data"
              },
              {"type":'slider',
               "label": 'Рік початку досліджень',
               "key": 'fir_year',
               "value" : 1990,
               "min" : 1981,
               "max" : 2016,
               "action_id" : "update_data",
               "linked_key": 'title',
               "linked_type": 'text',
               },
              {"type":'slider',
               "label": 'Кінцевий рік',
               "key": 'sec_year',
               "value" : 2000,
               "min" : 1981,
               "max" : 2016,
               "action_id" : "update_data",
               "linked_key": 'title',
               "linked_type": 'text',
               },
              {"type":'slider',
               "label": 'Початковий тиждень',
               "key": 'fir_week',
               "value" : 20,
               "min" : 1,
               "max" : 52,
               "action_id" : "update_data",
               "linked_key": 'title',
               "linked_type": 'text',
               },
              {"type":'slider',
               "label": 'Кінцевий тиждень',
               "key": 'sec_week',
               "value" : 40,
               "min" : 1,
               "max" : 52,
               "action_id" : "update_data",
               "linked_key": 'title',
               "linked_type": 'text',
               }
    ]

    controls = [{"control_type" : "button",
                "label" : "Отримати дані",
                "control_id" : "update_data"}]

    tabs = ["Графік", "Таблиця"]

    outputs = [{ "type" : "plot",
                    "id" : "plot",
                    "control_id" : "update_data",
                    "tab" : "Графік"},
                { "type" : "table",
                    "id" : "table_id",
                    "control_id" : "update_data",
                    "tab" : "Таблиця",
                    "on_page_load" : True }]

    def getPlot(self,params):
        path="vhi_id_"+str(params['region'])+".csv"
        df = pd.read_csv(path, index_col=False, header=1)
        df = df[(df['VHI']>=0)&(df['TCI']>=0)&(df['VCI']>=0)&(df['SMN']>=0)&(df['SMT']>=0)]
        x=df[(df['year']>=int(params['fir_year']))]
        x=x[(x['year']<=int(params['sec_year']))]
        x=x[(x['week']>=int(params['fir_week']))]
        x=x[(x['week']<=int(params['sec_week'])+1)]
        y_axis=x[params['index']]
        x_axis=x.index
        if params['fir_year']==params['sec_year']:
            x_axis=x_axis-x.index[0]
        plt.plot(x_axis, y_axis)
        return plt.gcf()

    def getData(self, params):
        path="vhi_id_"+str(params['region'])+".csv"
        df = pd.read_csv(path, index_col=False, header=1)
        df = df[(df['VHI']>=0)&(df['TCI']>=0)&(df['VCI']>=0)&(df['SMN']>=0)&(df['SMT']>=0)]
        x=df[(df['year']>=int(params['fir_year']))]
        x=x[(x['year']<=int(params['sec_year']))]
        x=x[(x['week']>=int(params['fir_week']))]
        x=x[(x['week']<=int(params['sec_week']))]
        x=x.rename(columns={'%Area_VHI_LESS_15':'AED'})
        x=x.rename(columns={'%Area_VHI_LESS_35':'AMD'})
        return x


app = RegionsApp()
app.launch(port=9093)