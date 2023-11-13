#!/usr/bin/env python3

import pandas as pd
import dash
from dash import html, dash_table, dcc
import plotly.graph_objects as go

# Create Dash app instance
app = dash.Dash(__name__)

####################### LOAD DATASET #############################

erosion_df = pd.read_csv("erosion.csv")

####################### PAGE LAYOUT #############################

app.layout = html.Div(children=[
    html.Br(),
    dash_table.DataTable(data=erosion_df.to_dict('records'),
        page_size=20,
        style_cell={"background-color": "lightgrey", "border": "solid 1px white", "color": "black", "font-size": "11px", "text-align": "left"},
        style_header={"background-color": "dodgerblue", "font-weight": "bold", "color": "white", "padding": "10px", "font-size": "18px"},
    ),
])




