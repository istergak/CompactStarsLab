# Aristotle University of Thessaloniki
# Physics Department
# Division of Nuclear and Elementary Particle Physics

# Nuclear Theory Group

# INTERACTIVE APP (for Researcher's Evening 2025 by PICO Project)
# APP NAME: CompactStarLab

# Python Script: 0
# Filename: main_script.py

# Description:
# The main script of the app, setting the opening/home layout of the app and the navigation buttons

from dash import Dash, dcc, html, Input, Output, State, callback_context
import home_page
import general_page
import composition_page
import eos_page
import tov_page
from translations import *

app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    dcc.Location(id="url"),
    dcc.Store(id="lang-store", data="en"),

    # Button for language selection
    html.Div([
        html.Button("English", id="lang-toggle-btn", n_clicks=0)
    ], style={
    'position': 'relative',
    'float': 'right',
    'marginTop': '-55px',
    'marginRight': '10px',
    'background': 'transparent',
    'color': 'white'
}),

    html.Div(id="page-content", style={"marginTop": "70px"})
])

# Language change when the respective button is pressed
@app.callback(
    Output("lang-store", "data"),
    Input("lang-toggle-btn", "n_clicks"),
    State("lang-store", "data"),
    prevent_initial_call=True
)
def toggle_language(n_clicks, current_lang):
    return "en" if current_lang == "el" else "el"

# Changing the label of the button
@app.callback(
    Output("lang-toggle-btn", "children"),
    Input("lang-store", "data")
)
def update_toggle_label(current_lang):
    return "English" if current_lang == "el" else "Ελληνικά"

# Loading the page based on URL and language selection
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname"), Input("lang-store", "data")]
)
def display_page(pathname, lang):
    if pathname == "/general_page":
        return general_page.layout(lang)
    elif pathname == "/composition_page":
        return composition_page.layout(lang)
    elif pathname == "/eos_page":
        return eos_page.layout(lang)
    elif pathname == "/tov_page":
        return tov_page.layout(lang)
    else:
        return home_page.layout(lang)


if __name__ == "__main__":
    app.run(debug=True)