# Python Script: 2c
# Filename: eos_page.py

# Description:
# Module for the page with interactive widgets for the solution process of TOV equations for Compact Stars

from dash import html, dcc
from translations import translations_tovpage

def layout(lang):
    tr = translations_tovpage[lang]

    return html.Div([
        # Return back button
        html.Div([
            dcc.Link("← " + tr["back_to_home"], href="/home_page", className="back-link")
        ], style={"position": "absolute", "top": "15px", "left": "15px"}),

        html.H1(tr["tov_title"], style={"textAlign": "center", "color": "white"}),

        html.Div([
            html.P(tr["tov_intro"], style={"color": "white", "textAlign": "center"})
        ], style={"marginTop": "50px"})
    ], className="dark-page")