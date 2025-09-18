# Python Script: 2a
# Filename: general_page.py

# Description:
# Module for the page with general info of Compact Stars

from dash import html, dcc
from translations import translations_generalpage

def layout(lang):
    tr = translations_generalpage[lang]

    return html.Div([
        # Return back button
        html.Div([
            dcc.Link("← " + tr["back_to_home"], href="/home_page", className="back-link")
        ], style={"position": "absolute", "top": "15px", "left": "15px"}),

        html.H1(tr["general_title"], style={"textAlign": "center", "color": "white"}),

        html.Div([
            html.P(tr["general_intro"], style={"color": "white", "textAlign": "center"})
        ], style={"marginTop": "50px"})
    ], className="dark-page")