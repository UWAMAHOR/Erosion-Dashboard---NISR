#!/usr/bin/env python3
import pandas as pd
from dash import Dash, dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

# Instantiate Dash app
app = Dash(__name__)

####################### LOAD DATASET #############################
erosion_df = pd.read_csv("erosion.csv")

####################### BAR CHART #############################
def create_bar_chart(col_name="Moderate (Diffuse overland flow erosion, overland flow erosion)"):
    fig =  px.histogram(data_frame=erosion_df, x="District", color=col_name,
                        histfunc="count", barmode='group', height=600)
    fig = fig.update_layout(bargap=0.5)
    return fig

####################### WIDGETS ################################
columns = ["Severe (Rill erosion, Gully erosion, Mass movement/Landslides)", "Moderate (Diffuse overland flow erosion, overland flow erosion)", "Very Low (splash erosion)"]
dd = dcc.Dropdown(id="sel_col", options=[{'label': col, 'value': col} for col in columns], value=columns[1], clearable=False)

####################### PAGE LAYOUT #############################
app.layout = html.Div(children=[
    html.Br(),
    dd,
    dcc.Graph(id="bar_chart")
])

####################### CALLBACKS ################################
@app.callback(Output("bar_chart", "figure"), [Input("sel_col", "value"), ])
def update_bar_chart(sel_col):
    return create_bar_chart(sel_col)
