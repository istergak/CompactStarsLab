# Python Script: 3a
# Filename: composition_page.py

# Description:
# Module for the page with info for the composition of matter inside Compact Stars

from dash import html, dcc
from translations import translations_compositionpage

def layout(lang):
    tr = translations_compositionpage[lang]

    return html.Div([
        # Return back button
        html.Div([
            dcc.Link("← " + tr["back_to_home"], href="/home_page", className="back-link")
        ], style={"position": "absolute", "top": "15px", "left": "15px"}),

        html.H1(tr["composition_title"], style={"textAlign": "center", "color": "white"}),

        html.Div([
            html.P(tr["composition_intro"], style={"color": "white", "textAlign": "center"})
        ], style={"marginTop": "50px"})
    ], className="dark-page")