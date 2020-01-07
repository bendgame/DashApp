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
        ,html.Div([html.H5('Price Slider')
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
    
        ], style={'marginBottom': 50, 'marginTop': 25, 'marginLeft':15, 'marginRight':15})
    , width=3)

    ,dbc.Col(html.Div([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                    dcc.Tab(label='Data Table', value='tab-1'),
                    dcc.Tab(label='Scatter Plot', value='tab-2'),
                ])
            , html.Div(id='tabs-content')
        ]), width=9)])
    
    ])
