# Python Script: 2b
# Filename: general_page.py

# Description:
# Module with interactive widgets for the page with general info of Compact Stars

# Required by: general_page.py

import numpy as np
import sympy as smp
#import pandas as pd
from pathlib import Path
from dash import html, dcc, callback, Input, Output, State, callback_context
import dash
import plotly.graph_objs as go
import plotly.express as px
from translations import translations_general_widgets

# =============================================================================================
# WIDGET 1: BUILDING A BARYON

def wdg1_baryon_build(qrks,lang):
    fig = go.Figure()
    tr = translations_general_widgets[lang]

    if qrks.count("None")>0:
        baryon_color = "#C5C3C3"
    elif qrks.count(0)==2 and qrks.count(1)==1:
        baryon_color = "#4D4A4A"
    elif qrks.count(0)==1 and qrks.count(1)==2:
        baryon_color = "#8A1515"
    elif qrks.count(0)==3:
        baryon_color = "#482379"
    elif qrks.count(1)==3:
        baryon_color = "#087151"

    # cycle coordinates
    theta = np.linspace(0, 2*np.pi, 200)
    x = 2*np.cos(theta)
    y = 2*np.sin(theta)

    # big circle -> baryon
    fig.add_trace(go.Scatter(
    x=x, y=y,
    mode="lines",
    line=dict(color="black", width=3),
    fill="toself",
    fillcolor=baryon_color,
    name="baryon",
    showlegend=False
    ))

    # quark positions (triangle)
    positions = [(0,1), (-0.9,-0.5), (0.9,-0.5)]
    colors = {"None": "gray", 0: "green", 1: "blue"}  # None=gray, down=green, up=blue
    names = {"None": "-", 0:"\"Down\"", 1: "\"Up\""}

    # quarks
    for i, ((x,y), val) in enumerate(zip(positions, qrks), start=1):
            fig.add_shape(type="circle",
                          x0=x-0.5, y0=y-0.5, x1=x+0.5, y1=y+0.5,
                          fillcolor=colors[val], line=dict(color="black"))
            fig.add_annotation(x=x, y=y, text=names[val], showarrow=False,
                               font=dict(size=16, color="white"))

    # springs (interactions)
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            (x1, y1), (x2, y2) = positions[i], positions[j]

            # making sinusoidal "spring"
            t = np.linspace(0, 1, 50)
            X = x1 + (x2 - x1) * t
            Y = y1 + (y2 - y1) * t + 0.1 * np.sin(15 * np.pi * t)

            fig.add_trace(go.Scatter(
                x=X, y=Y, mode="lines",
                line=dict(color="#F1AC58", width=2),
                showlegend=False,
                hoverinfo=None
            ))

    # axis
    fig.update_xaxes(range=[-2.5,2.5], visible=False)
    fig.update_yaxes(range=[-2.5,2.5], visible=False)
    fig.update_layout(
        margin=dict(l=0, r=0, t=30, b=0),
        title=tr["wdg1"]["graph_title"],
        font=dict(color="white",size=12,family="Arial"),
        plot_bgcolor="black",
        paper_bgcolor="black",
        height=550,
        width=550,
    )

    return fig