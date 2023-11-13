#!/usr/bin/env python3

import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

app = dash.Dash(__name__, url_base_pathname='/division/', title="Division 📊 ")

####################### LOAD DATASET #############################
erosion_df = pd.read_csv("erosion.csv")

####################### HISTOGRAM ###############################
def create_division(col_name="Severe (Rill erosion, Gully erosion, Mass movement/Landslides)"):
    return px.histogram(data_frame=erosion_df, x=col_name, height=600)

####################### WIDGETS ################################
columns = ("Severe (Rill erosion, Gully erosion, Mass movement/Landslides)",
           "Moderate (Diffuse overland flow erosion, overland flow erosion)",
           "Low (wind erosion)", "Very Low (splash erosion)")
dd = dcc.Dropdown(id="dist_column", options=[{'label': col, 'value': col} for col in columns],
                  value="Severe (Rill erosion, Gully erosion, Mass movement/Landslides)", clearable=False)

####################### PAGE LAYOUT #############################
app.layout = html.Div(children=[
    html.Br(),
    html.P("Select Column:"),
    dd,
    dcc.Graph(id="histogram")
])

####################### CALLBACKS ################################
@app.callback(Output("histogram", "figure"), [Input("dist_column", "value"), ])
def update_histogram(dist_column):
    return create_division(dist_column)

if __name__ == '__main__':
    app.run_server(debug=True)

