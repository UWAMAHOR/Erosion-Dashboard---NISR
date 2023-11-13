#!/usr/bin/env python3

from dash import Dash, html, dcc

import dash
import plotly.express as px

px.defaults.template = "ggplot2"

external_css = ["https://www.statistics.gov.rw/datasources/surveys"]

app = dash.Dash(__name__, pages_folder='pages', use_pages=True, external_stylesheets=external_css)

app.layout = html.Div([
    html.Br(),
    html.P('Erosion Dash-Plotly Web App', className="text-dark text-center fw-bold fs-1"),
    html.Div(children=[
        dcc.Link(page['name'], href=page["relative_path"], className="btn btn-dark m-2 fs-5")\
                      for page in dash.page_registry.values()
    ]),
    dash.page_container
], className="col-4 mx-auto")

if __name__ == '__main__':
    app.run(debug=True, port=8052)

