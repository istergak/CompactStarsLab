# Python Script: 2a
# Filename: general_page.py

# Description:
# Module for the page with general info of Compact Stars

# Required by: home_page.py, main_script.py

from dash import html, dcc, callback, Input, Output, State, callback_context
import dash
import numpy as np
import sympy as smp
from translations import translations_generalpage, translations_general_widgets
from general_widgets import *

def layout(lang):
    tr = translations_generalpage[lang]
    tr_widg = translations_general_widgets[lang]

    return html.Div([
        # Return back button
        html.Div([
            dcc.Link("← " + tr["back_to_home"], href="/home_page", className="back-link")
        ], style={"position": "absolute", "top": "15px", "left": "15px"}),
        
        # Title and intro
        html.H1(tr["general_title"], style={"textAlign": "center", "color": "white"}),
        html.P(tr["general_intro"], style={"textAlign": "center", "color": "white"}),

        # Section 1: Microcosm
        html.H2(tr["sec1_title"], style={"textAlign": "left", "color": "white"}),
        html.Div([
            html.Img(id="microcosm-img", style={"height": "60%", "width": "60%", "aligncontent": "center"}),
            html.Div([
                dcc.Markdown(tr["atom"],style={"textAlign":"left","color":"white","font-size":15}),
                dcc.Markdown(tr["atom_text"],mathjax=True,style={"textAlign":"justify","color":"white","font-size":14,"margin":"5px"}),
                dcc.Markdown(tr["nucleus"],style={"textAlign":"left","color":"white","font-size":15}),
                dcc.Markdown(tr["nucleus_text"],mathjax=True,style={"textAlign":"justify","color":"white","font-size":14,"margin":"5px"}),
                dcc.Markdown(tr["proton"],style={"textAlign":"left","color":"white","font-size":15}),
                dcc.Markdown(tr["proton_text"],mathjax=True,style={"textAlign":"justify","color":"white","font-size":14,"margin":"5px"}),
                dcc.Markdown(tr["neutron"],style={"textAlign":"left","color":"white","font-size":15}),
                dcc.Markdown(tr["neutron_text"],mathjax=True,style={"textAlign":"justify","color":"white","font-size":14,"margin":"5px"}),
                dcc.Markdown(tr["quarks"],style={"textAlign":"left","color":"white","font-size":15}),
                dcc.Markdown(tr["quarks_text"],mathjax=True,style={"textAlign":"justify","color":"white","font-size":14,"margin":"5px"}),
            ], style={"border":"2px solid red", "borderRadius":"10px"})
        ], style={'display': 'flex', 'justifyContent': 'justify'}),

        # Section 2: Quarks, the building blocks of nature
        html.H2(tr["sec2_title"], style={"textAlign": "left", "color": "white"}),
        html.Div([
            html.Div([
                html.Div(dcc.Markdown(tr["sec2_subtitle"],style={"textAlign":"justify","color":"white","font-size":15,"margin":"5px"}),style={"border":"2px solid red", "borderRadius":"10px","width":"450px"}),
                # Choice 1
                html.Div([
                    html.Div([
                    dcc.Markdown(tr_widg["wdg1"]["choice"]+" **1**",style={"textAlign":"justify","color":"white","font-size":15,"margin":"5px"}),
                    html.Div(dcc.RadioItems(id="wdg1-choice-1",options=[{"label":"None","value":"None"},{"label":"\"Down\" quark","value":0},{"label":"\"Up\" quark","value":1}],value="None",inline=True,style={"textAlign":"center","color":"white","font-size":15,"marginTop":"15px"}),style={"border":"2px solid orange", "borderRadius":"10px","height":"50px"})
                    ],style={"marginTop":"10px","marginRight":"5px","width":"300px"}),
                    html.Div([
                        dcc.Markdown(tr_widg["wdg1"]["charge"],style={"textAlign":"justify","color":"white","font-size":15}),
                        dcc.Markdown(id="wdg1-choice-1-charge",mathjax=True,style={"textAlign":"center","color":"white","font-size":16,"border":"2px dashed orange", "borderRadius":"10px","height":"50px"})
                    ],style={"marginTop":"10px","marginRight":"5px","width":"150px"})
                ],style={'display': 'flex', 'justifyContent': 'justify'}),
                # Choice 2
                html.Div([
                    html.Div([
                    dcc.Markdown(tr_widg["wdg1"]["choice"]+" **2**",style={"textAlign":"justify","color":"white","font-size":15,"margin":"5px"}),
                    html.Div(dcc.RadioItems(id="wdg1-choice-2",options=[{"label":"None","value":"None"},{"label":"\"Down\" quark","value":0},{"label":"\"Up\" quark","value":1}],value="None",inline=True,style={"textAlign":"center","color":"white","font-size":15,"marginTop":"15px"}),style={"border":"2px solid orange", "borderRadius":"10px","height":"50px"})
                    ],style={"marginTop":"10px","marginRight":"5px","width":"300px"}),
                    html.Div([
                        dcc.Markdown(tr_widg["wdg1"]["charge"],style={"textAlign":"justify","color":"white","font-size":15}),
                        dcc.Markdown(id="wdg1-choice-2-charge",mathjax=True,style={"textAlign":"center","color":"white","font-size":16,"border":"2px dashed orange", "borderRadius":"10px","height":"50px"})
                    ],style={"marginTop":"10px","marginRight":"5px","width":"150px"})
                ],style={'display': 'flex', 'justifyContent': 'justify'}),
                # Choice 3
                html.Div([
                    html.Div([
                    dcc.Markdown(tr_widg["wdg1"]["choice"]+" **3**",style={"textAlign":"justify","color":"white","font-size":15,"margin":"5px"}),
                    html.Div(dcc.RadioItems(id="wdg1-choice-3",options=[{"label":"None","value":"None"},{"label":"\"Down\" quark","value":0},{"label":"\"Up\" quark","value":1}],value="None",inline=True,style={"textAlign":"center","color":"white","font-size":15,"marginTop":"15px"}),style={"border":"2px solid orange", "borderRadius":"10px","height":"50px"})
                    ],style={"marginTop":"10px","marginRight":"5px","width":"300px"}),
                    html.Div([
                        dcc.Markdown(tr_widg["wdg1"]["charge"],style={"textAlign":"justify","color":"white","font-size":15}),
                        dcc.Markdown(id="wdg1-choice-3-charge",mathjax=True,style={"textAlign":"center","color":"white","font-size":16,"border":"2px dashed orange", "borderRadius":"10px","height":"50px"})
                    ],style={"marginTop":"10px","marginRight":"5px","width":"150px"})
                ],style={'display': 'flex', 'justifyContent': 'justify'}),
                # Result
                html.Div([
                    html.Div([
                    dcc.Markdown(tr_widg["wdg1"]["result"],style={"textAlign":"justify","color":"white","font-size":15,"margin":"5px"}),
                    dcc.Markdown(id="wdg1-result",mathjax=True,style={"textAlign":"center","color":"white","font-size":15,"marginTop":"15px","border":"2px solid gray", "borderRadius":"10px","height":"50px"})
                    ],style={"marginTop":"10px","marginRight":"5px","width":"300px"}),
                    html.Div([
                        dcc.Markdown(tr_widg["wdg1"]["charge"],style={"textAlign":"justify","color":"white","font-size":15}),
                        dcc.Markdown(id="wdg1-result-charge",mathjax=True,style={"textAlign":"center","color":"white","font-size":16,"border":"2px dashed gray", "borderRadius":"10px","height":"50px"})
                    ],style={"marginTop":"10px","marginRight":"5px","width":"150px"}),
                    html.Div([
                        dcc.Markdown(tr_widg["wdg1"]["state"],style={"textAlign":"justify","color":"white","font-size":15}),
                        dcc.Markdown(id="wdg1-result-state",mathjax=True,style={"textAlign":"center","color":"white","font-size":16,"border":"2px dashed gray", "borderRadius":"10px","height":"50px"})
                    ],style={"marginTop":"10px","marginRight":"5px","width":"150px"})
                ],style={'display': 'flex', 'justifyContent': 'justify'})
            ]),
            dcc.Graph(id="wdg1-baryon",figure=wdg1_baryon_build(["None","None","None"],lang),style={"marginLeft":"100px","border":"2px dashed green", "borderRadius":"10px",})
        ],style={'display': 'flex', 'justifyContent': 'justify'})
    ], className="dark-page")

# Updating "microcosm-img" content based on selected language
@callback(
    Output("microcosm-img","src"),
    Input("lang-store","data")
)

def update_microcosm_img(lang):
    if lang=="en":
        return "/assets/microcosm_en.png"
    elif lang=="el":
        return "/assets/microcosm_el.png"
    
# Updating "wdg1-choice-1-charge", "wdg1-choice-2-charge" and "wdg1-choice-3-charge" based on "wdg1-choice-1", "wdg1-choice-2" and "wdg1-choice-3" choices
@callback(
    Output("wdg1-choice-1-charge","children"),
    Output("wdg1-choice-2-charge","children"),
    Output("wdg1-choice-3-charge","children"),
    Output("wdg1-result","children"),
    Output("wdg1-result-charge","children"),
    Output("wdg1-result-state","children"),
    Output("wdg1-result-state","style"),
    Output("wdg1-baryon","figure"),
    Input("wdg1-choice-1","value"),
    Input("wdg1-choice-2","value"),
    Input("wdg1-choice-3","value"),
    State("lang-store","data")
)

def wdg1_update(*args):
    lang = args[-1]
    tr = translations_general_widgets[lang]

    qrk_choices = args[:3]
    qrk_charges = []
    qrk_charges_markdown = []
    for qrk in qrk_choices:
        if qrk=="None":
            qrk_charges.append(0)
            qrk_charges_markdown.append("-")
        elif qrk==0:
            qrk_charges.append(-1/3)
            qrk_charges_markdown.append(r"$-\frac{1}{3}e$")
        elif qrk==1:
            qrk_charges.append(2/3)
            qrk_charges_markdown.append(r"$+\frac{2}{3}e$")
    

    if qrk_choices.count("None")>0:
        result_name = "-"
        result_charge = f"${np.sum(qrk_charges):.2f}e$"
        result_state = "-"
        results_color = "gray"
    elif qrk_choices.count(0)==2 and qrk_choices.count(1)==1:
        result_name = tr["wdg1"]["neutron"]
        result_charge = f"${np.sum(qrk_charges):.2f}e$"
        result_state = tr["wdg1"]['stable']
        results_color = "green"
    elif qrk_choices.count(0)==1 and qrk_choices.count(1)==2:
        result_name = tr["wdg1"]["proton"]
        result_charge = f"${np.sum(qrk_charges):.2f}e$"
        result_state = tr["wdg1"]['stable']
        results_color = "green"
    elif qrk_choices.count(0)==3:
        result_name = tr["wdg1"]["delta_minus"]
        result_charge = f"${np.sum(qrk_charges):.2f}e$"
        result_state = tr["wdg1"]['unstable']
        results_color = "red"
    elif qrk_choices.count(1)==3:
        result_name = tr["wdg1"]["delta_plus"]
        result_charge = f"${np.sum(qrk_charges):.2f}e$"
        result_state = tr["wdg1"]['unstable']
        results_color = "red"    

    results_style = {"textAlign":"center","font-size":16,"border":"2px dashed gray", "borderRadius":"10px","height":"50px","color":results_color}


    return qrk_charges_markdown[0],qrk_charges_markdown[1],qrk_charges_markdown[2],result_name,result_charge, result_state, results_style, wdg1_baryon_build(qrk_choices,lang)     