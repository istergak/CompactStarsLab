# Python Script: 1a
# Filename: home_page.py

# Description:
# Module for building the home page of the app

from dash import html, dcc, Input, Output, State, callback
from translations import translations_homepage

def layout(lang):
    tr = translations_homepage[lang]  # local dictionary

    return html.Div([
        html.H1(tr["title"], style={"textAlign": "center", "color": "white"}),
        html.P(tr["subtitle"], style={"marginBottom": "50px", "textAlign": "center", "color": "white"}),

        html.Div([
                dcc.Link([
                    html.Div([
                        html.Img(src="/assets/options/General_Option.png"),
                        html.Div(tr["explore_general"], className="button-label")
                    ], className="button-card")
                ], href="/general_page")
            ], style={"margin": "30px"}),

        html.Div([
            html.Div([
                dcc.Link([
                    html.Div([
                        html.Img(src="/assets/options/Composition_Option.png"),
                        html.Div(tr["explore_composition"], className="button-label")
                    ], className="button-card")
                ], href="/composition_page")
            ], style={"display": "inline-block", "margin": "30px"}),

            html.Div([
                dcc.Link([
                    html.Div([
                        html.Img(src="/assets/options/EOS_Option.png"),
                        html.Div(tr["explore_eos"], className="button-label")
                    ], className="button-card")
                ], href="/eos_page")
            ], style={"display": "inline-block", "margin": "30px"}),

            html.Div([
                dcc.Link([
                    html.Div([
                        html.Img(src="/assets/options/TOV_Option.png"),
                        html.Div(tr["explore_tov"], className="button-label")
                    ], className="button-card")
                ], href="/tov_page")
            ], style={"display": "inline-block", "margin": "30px"}),
        ], style={"textAlign": "center"}),

        # Copyright
        html.Footer([
        html.Span("© 2025 CompactStarsLab by "),
        html.A("Ioannis Stergakis", href="https://github.com/istergak", target="_blank", style={"color":"white"}),
        html.Span(" – Licensed under "),
        html.A("CC BY-NC-SA 4.0", href="https://creativecommons.org/licenses/by-nc-sa/4.0/", target="_blank",style={"color":"white"})
        ], style={"color":"white","textAlign": "center", "marginTop": "20px", "fontSize": "12px"})
    ])