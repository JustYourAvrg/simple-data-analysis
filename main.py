import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import sys
import os

from dash import Dash, html, dash_table, dcc, callback, Output, Input
from flask import Flask, flash, redirect, render_template, request, session, send_file
from flask_session import Session


# Flask server
server = Flask(__name__)
server.config["SECRET_KEY"] = "4c4c3f7dc3c75d345485e793a382f0c6c39a5f895b99c99e"


# Setting up the flask session
server.config["SESSION_PERMANENT"] = True
server.config["SESSION_TYPE"] = "filesystem"

Session(server)


# Add Dash Graph to Flask server
app = Dash(__name__, server=server, url_base_pathname='/dash/', external_stylesheets=[dbc.themes.SKETCHY])
app.config.suppress_callback_exceptions = True

data_path = "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

# Get the keys from the data set
key_list = df.columns.unique()

keys = []

# Get the numeric keys from the data set
for key in key_list:
    if pd.api.types.is_numeric_dtype(df[key]):
        keys.append(key)

# Get the name of the data set
data_set_name = os.path.basename(data_path).split('.')[0]


# Initialize the app 
app.layout = dbc.Container([
    dbc.Row([
        html.Div(f'{data_set_name}', className="text-primary text-center fs-3")
    ]),

    
    dbc.Row([
        dbc.RadioItems(options=[{"label": x, "value": x} for x in keys],
            value=keys[0],
            inline=True,
            id='y-value-final',
            className="text-primary text-center fs-3")
    ]),
    
    dbc.Row([
        dcc.Dropdown(
            id='graph-type-final',
            options=[
                {'label': 'heatmap', 'value': 'heatmap'},
                {'label': 'Bar Graph', 'value': 'bar'},
                {'label': 'Scatter Plot', 'value': 'scatter'},
                {'label': 'Line Graph', 'value': 'line'},
                {'label': 'Box Plot', 'value': 'box'},
                {'label': 'Violin Plot', 'value': 'violin'},
                {'label': 'Strip Plot', 'value': 'strip'},
                {'label': 'Histogram', 'value': 'histogram'},
                {'label': 'Pie Chart', 'value': 'pie'},
                {'label': 'Treemap', 'value': 'treemap'},
                
            ],
            value='line',
            className="text-primary text-center fs-3",
            multi=False
        )
    ]),
    
    dbc.Row([
        dcc.Dropdown(
            id='x-value-final',
            options=[{'label': x, 'value': x} for x in key_list],
            value=key_list[0],
            className="text-primary text-center fs-3",
            multi=False
        )
    ]),
    
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
        ], width=6, style={'color': 'black'}, className="text-primary text-center fs-3"),
        
        dbc.Col([
            dcc.Graph(figure={}, id='my-first-graph-final', config={'scrollZoom': True})
        ], width=6, style={'color': 'black'}, className="text-primary text-center fs-3"),
        
])
        
        
], fluid=True, className="text-primary text-center fs-3")


# Callback for the graph
@app.callback(
    Output(component_id='my-first-graph-final', component_property='figure'),
    Input(component_id='y-value-final', component_property='value'),
    Input(component_id='graph-type-final', component_property='value'),
    Input(component_id='x-value-final', component_property='value')
)

# Update the graph
def update_graph_final(selected_y_value, selected_graph_type, selected_x_value):
    try:
        x_value = selected_x_value
        
        if selected_graph_type == 'heatmap':
            fig = px.density_heatmap(df, x=x_value, y=selected_y_value, title=f'{data_set_name}')
            return fig
        
        elif selected_graph_type == 'bar':
            fig = px.bar(df, x=x_value, y=selected_y_value, title=f'{data_set_name}')
            return fig
        
        elif selected_graph_type == 'scatter':
            fig = px.scatter(df, x=x_value, y=selected_y_value, title=f'{data_set_name}')
            return fig
        
        elif selected_graph_type == 'line':
            fig = px.line(df, x=x_value, y=selected_y_value, title=f'{data_set_name}')
            return fig
        
        elif selected_graph_type == 'box':
            fig = px.box(df, x=x_value, y=selected_y_value, title=f'{data_set_name}')
            return fig
        
        elif selected_graph_type == 'violin':
            fig = px.violin(df, x=x_value, y=selected_y_value, title=f'{data_set_name}')
            return fig
        
        elif selected_graph_type == 'strip':
            fig = px.strip(df, x=x_value, y=selected_y_value, title=f'{data_set_name}')
            return fig
        
        elif selected_graph_type == 'histogram':
            fig = px.histogram(df, x=x_value, y=selected_y_value, title=f'{data_set_name}')
            return fig
        
        elif selected_graph_type == 'pie':
            fig = px.pie(df, values=selected_y_value, names=x_value, title=f'{data_set_name}')
            return fig
        
        else:
            fig = px.density_heatmap(df, x=x_value, y=selected_y_value, title=f'{data_set_name}')
            return fig
    
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    app.run_server(debug=True)
