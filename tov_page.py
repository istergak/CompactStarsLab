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
        ], style={"marginTop": "50px"}),

        # Copyright
        html.Footer([
        html.Span("© 2025 CompactStarsLab by "),
        html.A("Ioannis Stergakis", href="https://github.com/istergak", target="_blank", style={"color":"white"}),
        html.Span(" – Licensed under "),
        html.A("CC BY-NC-SA 4.0", href="https://creativecommons.org/licenses/by-nc-sa/4.0/", target="_blank",style={"color":"white"})
        ], style={"color":"white","textAlign": "center", "marginTop": "20px", "fontSize": "12px"})
    ], className="dark-page")