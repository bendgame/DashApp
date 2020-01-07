import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_table
from app import app
from database import transforms

df = transforms.df

layout = html.Div(
            id='table-paging-with-graph-container',
            className="five columns"
        )

@app.callback(Output('table-paging-with-graph-container', "children"),
[Input('rating-95', 'value')
, Input('price-slider', 'value')
])

def update_graph(ratingcheck, prices):
    dff = df

    low = prices[0]
    high = prices[1]

    dff = dff.loc[(dff['price'] >= low) & (dff['price'] <= high)]
    
    if ratingcheck == ['Y']:
       dff = dff.loc[dff['rating'] >= 95]
    else:
        dff

    trace1 = go.Scattergl(x = dff['rating']
                        , y = dff['price']
                        , mode='markers'
                        , opacity=0.7
                        , marker={
                                'size': 8
                                , 'line': {'width': 0.5, 'color': 'white'}
                                }
                        , name='Price v Rating'
                    )
    return html.Div([
        dcc.Graph(
            id='rating-price'
            , figure={
                'data': [trace1
                    # dict(
                    #     x=df['price'],
                    #     y=df['rating'],
                    #     #text=df[df['continent'] == i]['country'],
                    #     mode='markers',
                    #     opacity=0.7,
                    #     marker={
                    #         'size': 8,
                    #         'line': {'width': 0.5, 'color': 'white'}
                    #     },
                    #     name='Price v Rating'
                    #) 
                ],
                'layout': dict(
                    xaxis={'type': 'log', 'title': 'Rating'},
                    yaxis={'title': 'Price'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        )
    ])