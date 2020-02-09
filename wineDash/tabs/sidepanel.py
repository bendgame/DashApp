import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
import dash_table
import pandas
from dash.dependencies import Input, Output

from app import app

from tabs import tab1, tab2
from database import transforms

df = transforms.df
min_p=df.price.min()
max_p=df.price.max()

layout = html.Div([
    html.H1('Wine Dash')
    ,dbc.Row([dbc.Col(
        html.Div([
         html.H2('Filters')
        , dcc.Checklist(id='rating-95'
        , options = [
            {'label':'Only rating >= 95 ', 'value':'Y'}
        ])
        ,html.Div([html.P()
                ,html.H5('Price Slider')
                ,dcc.RangeSlider(id='price-slider'
                            ,min = min_p
                            ,max= max_p
                            , marks = {0: '$0',
                                        500: '$500',
                                        1000: '$1000',
                                        1500: '$1500',
                                        2000: '$2000',
                                        2500: '$2500',
                                        3000: '$3000',
                                       }
                            , value = [0,3300]
                            )
                        
                            ])
        ,html.Div([html.P()
            ,html.H5('Country')
            , dcc.Dropdown(id = 'country-drop'
                        ,options=[
                             {'label': i, 'value': i} for i in df.country.unique()
                        ],
                        value=['US'],
                        multi=True
                    )  
        ])

        ,html.Div([html.P()
            ,html.H5('Province')
            , dcc.Dropdown(id = 'province-drop',
                            value=[],
                            multi=True
                        )  
        ])

        ,html.Div([html.P()
            ,html.H5('Variety')
            , dcc.Dropdown(id = 'variety-drop',
                            value=[],
                            multi=True
                        )  
        ])

        ], style={'marginBottom': 50, 'marginTop': 25, 'marginLeft':15, 'marginRight':15}
        )#end div
    , width=3) # End col

    ,dbc.Col(html.Div([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                    dcc.Tab(label='Data Table', value='tab-1'),
                    dcc.Tab(label='Scatter Plot', value='tab-2'),
                    dcc.Tab(label='Heatmap Plot', value='tab-3'),
                ])
            , html.Div(id='tabs-content')
        ]), width=9)
        ]) #end row
    
    ])#end div

@app.callback(Output('province-drop', 'options'),
[Input('country-drop', 'value')])
def set_province_options(country):
    
    if len(country)> 0:
        countries = country
        return [{'label': i, 'value': i} for i in sorted(set(df['province'].loc[df['country'].isin(countries)]))]
       
    else:
        countries = []
        return [{'label': i, 'value': i} for i in sorted(set(df['province'].loc[df['country'].isin(countries)]))]

@app.callback(Output('variety-drop', 'options'),
[Input('province-drop', 'value')])
def set_variety_options(province):

    # if province is None:
    #     provinces = []
    
    if len(province)> 0:
        provinces = province
        return [{'label': i, 'value': i} for i in sorted(set(df['variety'].loc[df['province'].isin(provinces)]))]
       
    else:
        provinces = []
        return [{'label': i, 'value': i} for i in sorted(set(df['variety'].loc[df['province'].isin(provinces)]))]
        