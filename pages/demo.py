#!/usr/bin/env python3

import dash
from dash import html

# Create Dash app instance
app = dash.Dash(__name__)

####################### PAGE LAYOUT #############################
app.layout = html.Div(children=[
    html.Div(children=[
        html.H2("Erosion Dataset Overview"),
        "NISR has conducted the Seasonal Agriculture Survey to provide more comprehensive data on the Rwandan agriculture sector. During 2023 Season A.",
        html.Br(), html.Br(),
        " the data collection activities started from 4th December 2022 and ended on 16th February 2023 covering 1,200 segments and 345 large scale farmers’ holdings across the country."
    ]),
    html.Div(children=[
        html.Br(),
        html.H2("Data Variables"),
        html.B("District: "), "District name",
        html.Br(),
        html.B("Severe (Rill erosion, Gully erosion, Mass movement/Landslides): "),
        "Severe (Rill erosion, Gully erosion, Mass movement/Landslides) A_Percentage of plots by degree of erosion per district",
        html.Br(),
        html.B("Moderate (Diffuse overland flow erosion, overland flow erosion): "),
        "Moderate (Diffuse overland flow erosion, overland flow erosion)A_Percentage of plots by degree of erosion per district",
        html.Br(),
        html.B("Low (wind erosion): "),
        "Low (wind erosion) A_Percentage of plots by degree of erosion per district",
        html.Br(),
        html.B("Very Low (splash erosion)): "),
        "Very Low (splash erosion) A_Percentage of plots by degree of erosion per district",
    ])
], className="bg-light p-4 m-2")  
