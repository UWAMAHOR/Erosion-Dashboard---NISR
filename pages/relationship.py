#!/usr/bin/env python3

import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

# Create Dash app
app = dash.Dash(__name__)

####################### LOAD DATASET #############################
erosion_df = pd.read_csv("erosion.csv")

####################### SCATTER CHART #############################
def create_scatter_chart(x_axis="Severe (Rill erosion, Gully erosion, Mass movement/Landslides)", y_axis="Very Low (splash erosion)"):
    return px.scatter(data_frame=erosion_df, x=x_axis, y=y_axis, height=600)

####################### WIDGETS #############################
columns = ["Severe (Rill erosion, Gully erosion, Mass movement/Landslides)", "Moderate (Diffuse overland flow erosion, overland flow erosion)", "Low (wind erosion)", "Very Low (splash erosion)"]

x_axis = dcc.Dropdown(id="x_axis", options=[{'label': col, 'value': col} for col in columns], value="Severe (Rill erosion, Gully erosion, Mass movement/Landslides)", clearable=False)
y_axis = dcc.Dropdown(id="y_axis", options=[{'label': col, 'value': col} for col in columns], value="Very Low (splash erosion)", clearable=False)

####################### PAGE LAYOUT #############################
app.layout = html.Div(children=[
    html.Br(),
    "X-Axis", x_axis,
    "Y-Axis", y_axis,
    dcc.Graph(id="scatter")
])

####################### CALLBACKS ###############################
@app.callback(Output("scatter", "figure"), [Input("x_axis", "value"), Input("y_axis", "value")])
def update_scatter_chart(x_axis, y_axis):
    return create_scatter_chart(x_axis, y_axis)


