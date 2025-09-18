# Python Script: 4b
# Filename: eos_widgets_NS.py

# Description:
# Module with interactive widgets for the EOSs of Neutron Stars

# Required by: eos_page.py

import numpy as np
import sympy as smp
#import pandas as pd
from dash import html, dcc, callback, Input, Output, State, callback_context
import dash
import plotly.graph_objs as go
import plotly.express as px
from translations import translations_eos_widgets_NS
from ExoticStarsDataHandling import *

# =============================================================================================
# PRELIMINARIES

# Numerical definition of the EoSs (CRUST)
# The following EoSs for the 4 layers of the NS
# OUTER-CRUST are being defined:

# eos_crust1 -> EoS for pressure P : 9.34375*10^-5 < P < 0.184 [MeV/fm^3] 
# (for the PS EoS the upper bound, i.e. the crust/core bound, is 0.696 [MeV/fm^3])

# eos_crust2 -> EoS for pressure P : 4.1725*10^-8 < P < 9.34375*10^-5 [MeV/fm^3]

# eos_crust3 -> EoS for pressure P : 1.44875*10^-11 < P < 4.1725*10^-8 [MeV/fm^3]

# eos_crust4 -> EoS for pressure P : P < 1.44875*10^-11 [MeV/fm^3]

def eos_crust1(p):
    return 0.00873 + 103.17338*(1-np.exp(-p/0.38527))+7.34979*(1-np.exp(-p/0.01211))
def eos_crust2(p):
    return 0.00015 + 0.00203*(1-np.exp(-p*344827.5))+0.10851*(1-np.exp(-p*7692.3076))
def eos_crust3(p):
    return 0.0000051*(1-np.exp(-p*0.2373*1e10))+0.00014*(1-np.exp(-p*0.4020*1e8))
def eos_crust4(p):
    c0 = 31.93753
    c1 = 10.82611*np.log10(p)
    c2 = 1.29312 * (np.log10(p)**2)
    c3 = 0.08014*(np.log10(p)**3)
    c4 = 0.00242*(np.log10(p)**4)
    c5 = 0.000028*(np.log10(p)**5)
    return 10**(c0 + c1 + c2 + c3 + c4 + c5)

# Symbolic definition of the EoSs (CRUST)
# The following EoSs for the 4 layers of the NS
# OUTER-CRUST are being defined:

# eos_crust1 -> EoS for pressure P : 9.34375*10^-5 < P < 0.184 [MeV/fm^3] 
# (for the PS EoS the upper bound, i.e. the crust/core bound, is 0.696 [MeV/fm^3])

# eos_crust2 -> EoS for pressure P : 4.1725*10^-8 < P < 9.34375*10^-5 [MeV/fm^3]

# eos_crust3 -> EoS for pressure P : 1.44875*10^-11 < P < 4.1725*10^-8 [MeV/fm^3]

# eos_crust4 -> EoS for pressure P : P < 1.44875*10^-11 [MeV/fm^3]

def eos_crust1_sym(p):
    return 0.00873 + 103.17338*(1-smp.exp(-p/0.38527))+7.34979*(1-smp.exp(-p/0.01211))
def eos_crust2_sym(p):
    return 0.00015 + 0.00203*(1-smp.exp(-p*344827.5))+0.10851*(1-smp.exp(-p*7692.3076))
def eos_crust3_sym(p):
    return 0.0000051*(1-smp.exp(-p*0.2373*1e10))+0.00014*(1-smp.exp(-p*0.4020*1e8))
def eos_crust4_sym(p):
    c0 = 31.93753
    c1 = 10.82611*smp.log(p,10)
    c2 = 1.29312 * (smp.log(p,10)**2)
    c3 = 0.08014*(smp.log(p,10)**3)
    c4 = 0.00242*(smp.log(p,10)**4)
    c5 = 0.000028*(smp.log(p,10)**5)
    return 10**(c0 + c1 + c2 + c3 + c4 + c5)

# Defining a list to store the info for the EoSs of the CRUST of the Neutron Star

eos_list_crust = [{"name": "LAYER 1","num_formula": eos_crust1,"sym_formula": eos_crust1_sym, "color": "#FFAD5A"},
                  {"name": "LAYER 2","num_formula": eos_crust2,"sym_formula": eos_crust2_sym,"color": "#FF7E3D"},
                  {"name": "LAYER 3","num_formula": eos_crust3,"sym_formula": eos_crust3_sym, "color": "#D26036"},
                  {"name": "LAYER 4","num_formula": eos_crust4,"sym_formula": eos_crust4_sym, "color": "#FD0000"}
                  ]

# Defining a list with the pressure boundaries of the CRUST layers
p_bounds = [0.184,9.34375*10**(-5),4.1725*10**(-8),1.44875*10**(-11)]
p_bounds_PS = [0.696,9.34375*10**(-5),4.1725*10**(-8),1.44875*10**(-11)]

# Numerical definition of the EoSs (CORE)
# The following 21 models are being defined:

# APR-1
# BGP
# BL-1, BL-2
# DH
# HHJ-1, HHJ-2
# HLPS-2, HLPS-3
# MDI-1, MDI-2, MDI-3, MDI-4, 
# NLD
# PS
# SCVBB
# Ska
# SkI4
# W
# WFF-1, WFF-2

def APR_1(p):
    return 0.000719964*pow(p,1.85898)+108.975*pow(p,0.340074)
def BGP(p):
    return 0.0112475*pow(p,1.59689)+102.302*pow(p,0.335526)
def BL_1(p):
    return 0.488686*pow(p,1.01457)+102.26*pow(p,0.355095)
def BL_2(p):
    return 1.34241*pow(p,0.910079)+100.756*pow(p,0.354129)
def DH(p):
    return 39.5021*pow(p,0.541485)+96.0528*pow(p,0.00401285)
def HHJ_1(p):
    return 1.78429*pow(p,0.93761)+106.93652*pow(p,0.31715)
def HHJ_2(p):
    return 1.18961*pow(p,0.96539)+108.40302*pow(p,0.31264)                    
def HLPS_2(p):
    return 161.553+172.858*(1-np.exp(-p/22.8644))+2777.75*(1-np.exp(-p/1909.97))
def HLPS_3(p):
    return 81.5682+131.811*(1-np.exp(-p/4.41577))+924.143*(1-np.exp(-p/523.736))
def MDI_1(p):
    return 4.1844*pow(p,0.81449) + 95.00135*pow(p,0.31736)
def MDI_2(p):
    return 5.97365*pow(p,0.77374) + 89.24*pow(p,0.30993)
def MDI_3(p):
    return 15.55*pow(p,0.666)+76.71*pow(p,0.247)
def MDI_4(p):
    return 25.99587*pow(p,0.61209)+65.62193*pow(p,0.15512)
def NLD(p):
    return 119.05736+304.80445*(1-np.exp(-p/48.61465))+33722.34448*(1-np.exp(-p/17499.47411))
def PS(p):
    return 1.69483+9805.95*(1-np.exp(-0.000193624*p))+212.072*(1-np.exp(-0.401508*p))
def SCVBB(p):
    return 0.371414*pow(p,1.08004)+109.258*pow(p,0.351019)    
def Ska(p):
    return 0.53928*pow(p,1.01394)+94.31452*pow(p,0.35135)
def SkI4(p):
    return 4.75668*pow(p,0.76537)+105.722*pow(p,0.2745)
def W(p):
    return 0.261822*pow(p,1.16851)+92.4893*pow(p,0.307728)
def WFF_1(p):
    return 0.00127717*pow(p,1.69617)+135.233*pow(p,0.331471)
def WFF_2(p):
    return 0.00244523*pow(p,1.62692)+122.076*pow(p,0.340401)

# Symbolic definition of the EoSs (CORE)
# The same 21 models are being defined:

# APR-1
# BGP
# BL-1, BL-2
# DH
# HHJ-1, HHJ-2
# HLPS-2, HLPS-3
# MDI-1, MDI-2, MDI-3, MDI-4, 
# NLD
# PS
# SCVBB
# Ska
# SkI4
# W
# WFF-1, WFF-2

def APR_1_sym(p):
    return 0.000719964*pow(p,1.85898)+108.975*pow(p,0.340074)
def BGP_sym(p):
    return 0.0112475*pow(p,1.59689)+102.302*pow(p,0.335526)
def BL_1_sym(p):
    return 0.488686*pow(p,1.01457)+102.26*pow(p,0.355095)
def BL_2_sym(p):
    return 1.34241*pow(p,0.910079)+100.756*pow(p,0.354129)
def DH_sym(p):
    return 39.5021*pow(p,0.541485)+96.0528*pow(p,0.00401285)
def HHJ_1_sym(p):
    return 1.78429*pow(p,0.93761)+106.93652*pow(p,0.31715)
def HHJ_2_sym(p):
    return 1.18961*pow(p,0.96539)+108.40302*pow(p,0.31264)                    
def HLPS_2_sym(p):
    return 161.553+172.858*(1-smp.exp(-p/22.8644))+2777.75*(1-smp.exp(-p/1909.97))
def HLPS_3_sym(p):
    return 81.5682+131.811*(1-smp.exp(-p/4.41577))+924.143*(1-smp.exp(-p/523.736))
def MDI_1_sym(p):
    return 4.1844*pow(p,0.81449) + 95.00135*pow(p,0.31736)
def MDI_2_sym(p):
    return 5.97365*pow(p,0.77374) + 89.24*pow(p,0.30993)
def MDI_3_sym(p):
    return 15.55*pow(p,0.666)+76.71*pow(p,0.247)
def MDI_4_sym(p):
    return 25.99587*pow(p,0.61209)+65.62193*pow(p,0.15512)
def NLD_sym(p):
    return 119.05736+304.80445*(1-smp.exp(-p/48.61465))+33722.34448*(1-smp.exp(-p/17499.47411))
def PS_sym(p):
    return 1.69483+9805.95*(1-smp.exp(-0.000193624*p))+212.072*(1-smp.exp(-0.401508*p))
def SCVBB_sym(p):
    return 0.371414*pow(p,1.08004)+109.258*pow(p,0.351019)    
def Ska_sym(p):
    return 0.53928*pow(p,1.01394)+94.31452*pow(p,0.35135)
def SkI4_sym(p):
    return 4.75668*pow(p,0.76537)+105.722*pow(p,0.2745)
def W_sym(p):
    return 0.261822*pow(p,1.16851)+92.4893*pow(p,0.307728)
def WFF_1_sym(p):
    return 0.00127717*pow(p,1.69617)+135.233*pow(p,0.331471)
def WFF_2_sym(p):
    return 0.00244523*pow(p,1.62692)+122.076*pow(p,0.340401)

# Markdown definition of the EoSs (CORE) formulas
# The same 21 models are being defined:

# APR-1
# BGP
# BL-1, BL-2
# DH
# HHJ-1, HHJ-2
# HLPS-2, HLPS-3
# MDI-1, MDI-2, MDI-3, MDI-4, 
# NLD
# PS
# SCVBB
# Ska
# SkI4
# W
# WFF-1, WFF-2

APR_1_mark=r"$\epsilon_{APR-1}(P)=0.000719964\cdot P^{1.85898}+108.975\cdot P^{0.340074}$"
BGP_mark=r"$\epsilon_{BGP}(P)=0.0112475\cdot P^{1.59689}+102.302\cdot P^{0.335526}$"
BL_1_mark=r"$\epsilon_{BL-1}(P)=0.488686\cdot P^{1.01457}+102.26\cdot P^{0.355095}$"
BL_2_mark=r"$\epsilon_{BL-2}(P)=1.34241\cdot P^{0.910079}+100.756\cdot P^{0.354129}$"
DH_mark=r"$\epsilon_{DH}(P)=39.5021\cdot P^{0.541485}+96.0528\cdot P^{0.00401285}$"
HHJ_1_mark=r"$\epsilon_{HHJ-1}(P)=1.78429\cdot P^{0.93761}+106.93652\cdot P^{0.31715}$"
HHJ_2_mark=r"$\epsilon_{HHJ-2}(P)=1.18961\cdot P^{0.96539}+108.40302\cdot P^{0.31264}$"                    
HLPS_2_mark=r"$\epsilon_{HLPS-2}(P)=161.553+172.858\left(1-e^{-\frac{P}{22.8644}}\right)+2777.75\left(1-e^{-\frac{P}{1909.97}}\right)$"
HLPS_3_mark=r"$\epsilon_{HLPS-3}(P)=81.5682+131.811\left(1-e^{-\frac{P}{4.41577}}\right)+924.143\left(1-e^{-\frac{P}{523.736}}\right)$"
MDI_1_mark=r"$\epsilon_{MDI-1}(P)=4.1844\cdot P^{0.81449} + 95.00135\cdot P^{0.31736}$"
MDI_2_mark=r"$\epsilon_{MDI-2}(P)=5.97365\cdot P^{0.77374} + 89.24*\cdot P^{0.30993}$"
MDI_3_mark=r"$\epsilon_{MDI-3}(P)=15.55\cdot P^{0.666}+76.71\cdot P^{0.247}$"
MDI_4_mark=r"$\epsilon_{MDI-4}(P)=25.99587\cdot P^{0.61209}+65.62193\cdot P^{0.15512}$"
NLD_mark=r"$\epsilon_{NLD}(P)=119.05736+304.80445\left(1-e^{-\frac{P}{48.61465}}\right)+33722.34448\left(1-e^{-\frac{P}{17499.47411}}\right)$"
PS_mark=r"$\epsilon_{PS}(P)=1.69483+9805.95\left(1-e^{-0.000193624\cdot P}\right)+212.072\left(1-e^{-0.401508\cdot P}\right)$"
SCVBB_mark=r"$\epsilon_{SCVBB}(P)=0.371414\cdot P^{1.08004}+109.258\cdot P^{0.351019}$"    
Ska_mark=r"$\epsilon_{Ska}(P)=0.53928\cdot P^{1.01394}+94.31452\cdot P^{0.35135}$"
SkI4_mark=r"$\epsilon_{SkI4}(P)=4.75668\cdot P^{0.76537}+105.722\cdot P^{0.2745}$"
W_mark=r"$\epsilon_{W}(P)=0.261822\cdot P^{1.16851}+92.4893\cdot P^{0.307728}$"
WFF_1_mark=r"$\epsilon_{WFF-1}(P)=0.00127717\cdot P^{1.69617}+135.233\cdot P^{0.331471}$"
WFF_2_mark=r"$\epsilon_{WFF-2}(P)=0.00244523\cdot P^{1.62692}+122.076\cdot P^{0.340401}$"


# Defining a list to store the info for the EoSs of the CORE of the Neutron Star
eos_list_core = [{"name": "APR-1", "fullname":  "Akmal-Pandharipande-Ravenhall", "num_formula": APR_1, "sym_formula": APR_1_sym, "markdown_formula": APR_1_mark,"color": '#1f77b4'},
            {"name": "BGP", "fullname":  "Bowers-Gleeson-Pedigo", "num_formula": BGP, "sym_formula": BGP_sym, "markdown_formula": BGP_mark, "color":  '#ff7f0e'},
            {"name": "BL-1", "fullname":  "Bombaci-Logoteta", "num_formula": BL_1, "sym_formula": BL_1_sym, "markdown_formula": BL_1_mark, "color": '#2ca02c'},
            {"name": "BL-2", "fullname":  "Bombaci-Logoteta", "num_formula": BL_2, "sym_formula": BL_2_sym, "markdown_formula": BL_2_mark, "color": '#d62728'},
            {"name": "DH", "fullname":  "Douchin-Haensel", "num_formula": DH, "sym_formula": DH, "markdown_formula": DH_mark, "color": '#9467bd'},
            {"name": "HHJ-1", "fullname":  "Heiselberg and Hjorth-Jensen", "num_formula": HHJ_1, "sym_formula": HHJ_1_sym, "markdown_formula": HHJ_1_mark, "color":  '#8c564b'},
            {"name": "HHJ-2", "fullname":  "Heiselberg and Hjorth-Jensen", "num_formula": HHJ_2, "sym_formula": HHJ_2_sym, "markdown_formula": HHJ_2_mark, "color": '#e377c2'},
            {"name": "HLPS-2", "fullname":  "Hebeler-Lattimer-Pethick-Schwenk", "num_formula": HLPS_2, "sym_formula": HLPS_2_sym, "markdown_formula": HLPS_2_mark, "color":  "#094D31"},
            {"name": "HLPS-3", "fullname":  "Hebeler-Lattimer-Pethick-Schwenk", "num_formula": HLPS_3, "sym_formula": HLPS_3_sym, "markdown_formula": HLPS_3_mark, "color": '#bcbd22'},
            {"name": "MDI-1", "fullname":  "Momentum-Dependent Interaction", "num_formula": MDI_1, "sym_formula": MDI_1_sym, "markdown_formula": MDI_1_mark, "color": '#17becf'},
            {"name": "MDI-2", "fullname":  "Momentum-Dependent Interaction", "num_formula": MDI_2, "sym_formula": MDI_2_sym, "markdown_formula": MDI_2_mark, "color": "#000000"},
            {"name": "MDI-3", "fullname":  "Momentum-Dependent Interaction", "num_formula": MDI_3, "sym_formula": MDI_3_sym, "markdown_formula": MDI_3_mark, "color": '#1f77b4'},
            {"name": "MDI-4", "fullname":  "Momentum-Dependent Interaction", "num_formula": MDI_4, "sym_formula": MDI_4_sym, "markdown_formula": MDI_4_mark, "color":  '#ff7f0e'},
            {"name": "NLD", "fullname":  "Non Linear Derivative", "num_formula": NLD, "sym_formula": NLD_sym, "markdown_formula": NLD_mark, "color": '#2ca02c'},
            {"name": "PS", "fullname":  "Pethick-Schwenk", "num_formula": PS, "sym_formula": PS_sym, "markdown_formula": PS_mark, "color": '#d62728'},
            {"name": "SCVBB", "fullname":  "Sharma-Centelles-Vinas-Baldo-Burgio", "num_formula": SCVBB, "sym_formula": SCVBB_sym, "markdown_formula": SCVBB_mark, "color": '#9467bd'},
            {"name": "Ska", "fullname":  "Skyrme", "num_formula": Ska, "sym_formula": Ska_sym, "markdown_formula": Ska_mark, "color":  '#8c564b' },
            {"name": "SkI4", "fullname":  "Skyrme", "num_formula": SkI4, "sym_formula": SkI4_sym, "markdown_formula": SkI4_mark, "color": '#e377c2'},
            {"name": "W", "fullname":  "Walecka", "num_formula": W, "sym_formula": W_sym, "markdown_formula": W_mark, "color":  "#094D31"},
            {"name": "WFF-1", "fullname":  "Wiringa-Fiks-Fabrocini", "num_formula": WFF_1, "sym_formula": WFF_1_sym, "markdown_formula": WFF_1_mark, "color": '#bcbd22'},
            {"name": "WFF-2", "fullname":  "Wiringa-Fiks-Fabrocini", "num_formula": WFF_2, "sym_formula": WFF_2_sym, "markdown_formula": WFF_2_mark, "color": '#17becf'}
            ]


# Definition of useful constants for polytropic grids
ρ_sat = 2.7*10**14 # nuclear saturation density [g/cm^3]
c = 3e8 # vaccuum speed of light in m/s
MeV_to_J = 1.60218e-13 # 1MeV value in Joules
# Pessures at nuclear saturation density ρ_sat
P_sat_HLPS_2 = 1.722
P_sat_HLPS_3 = 2.816  

# Converter of mass density from units g/cm^3 to MeV/fm^3 units
def conv_to_MeV(value):
    # Multiply by 10^3 to convert to SI units (kg/m^3)
    result = value*10**3
    # Multiply by c^2 to convert to J/m^3
    result = result*c**2
    # Divide by the MeV_to_J constant to convert to MeV/m^3
    result = result/MeV_to_J
    # Convert m to fm, for the units to be MeV/fm^3
    result = result*10**(-45)

    return result

# Getting the nuclear saturation density to MeV/fm^3
ρ_sat_MeV = conv_to_MeV(ρ_sat)

# Defining the polytrope relation between pressure P and mass density ρ as a function
def P_poly(ρ,K,Γ):
    return K*np.array(ρ)**Γ

# Defining the K constant parameter as a function of pressure P and and mass density
def K_calc(P,ρ,Γ):
    return P/ρ**Γ

# Function that returns all the numerical combinations of the parameter Γ
# given the available choices for Γ and the number of mass density segments
def Γ_total_combos_num(Γ_choices,num_segments):

        # Count the given number of choices for Γ
        n = len(Γ_choices)
    
        # Find all the possible combinations of Γ
        total_combos = n**num_segments # number of total combinations
        i = 1 # counter
        Γ_selections = [] # storage list for the combinations

        # Random selection of a Γ value per each of the given mass density segments
        Γ_selection = random.choices(Γ_choices,k=num_segments)

        # Storaging the combination of Γ values
        Γ_selections.append(Γ_selection)
        i=i+1

        # Iterative process to find all combinations
        while i<=total_combos:
            # Random selection of a Γ value per each of the given mass density segments
            Γ_selection = random.choices(Γ_choices,k=num_segments)

            # Checking if the current combination has already been created   
            if Γ_selections.count(Γ_selection)!=0:
                continue
            else:
                Γ_selections.append(Γ_selection)
                i=i+1

        return Γ_selections

# Function to return the values of K_i, P_i and E_i given a
# starting pressure P_0, the bounds of the segments of 
# mass density ρ and the selected values of Γ for the segments of ρ
def poly_param_calc(P_0,ρ_bounds,Γ_combo):
    # Definition of storage lists
    results = []
    Pi_vals = []
    Pi_vals.append(P_0)
    Ki_values = []
    
    # Number of segments
    n = len(Γ_combo)

    # For loop to calculate the values of Pi,Γi and Ki
    for i in range(0,n):
        Γi = Γ_combo[i]
        
        Ki = K_calc(Pi_vals[i],ρ_bounds[i],Γi)
        Ki_values.append(Ki)

        Pi = P_poly(ρ_bounds[i+1],Ki,Γi)
        Pi_vals.append(Pi)

    results = [Pi_vals,Ki_values]
    return results

# Definition of the piecewise polytrope function of pressure vs mass density
def P_poly_piecewise(ρ,ρ_bounds,Ki_vals,Γi_vals):
    points = len(ρ_bounds)
    n = points-1

    conditions = []
    functions = []

    for i in range(0,n):
        conditions.append((ρ>=ρ_bounds[i])*(ρ<ρ_bounds[i+1]))
        functions.append(P_poly(ρ,Ki_vals[i],Γi_vals[i]))

    return np.piecewise(ρ,conditions,functions)


# =============================================================================================
# WIDGET 1: DESCRIBING THE STRUCTURE OF A NEUTRON STAR I (CRUST)

# Defining the crust EoS info as a dictionary
def eos_info_wdg1(lang):
    tr = translations_eos_widgets_NS[lang]

    dictionary = [{"name": tr["core"] +" (Ska)", "radius_weight": 0, "range": np.linspace(p_bounds[0]+p_bounds[0]/1e4,1000,500),"formula": eos_list_core[16]["num_formula"], "color": "#253D32"},
                 {"name": tr["layer"] + " 1", "radius_weight": 0.4, "range": np.linspace(p_bounds[1]+p_bounds[1]/1e4,p_bounds[0],500), "formula": eos_list_crust[0]["num_formula"], "color": eos_list_crust[0]["color"]},
                 {"name": tr["layer"] + " 2", "radius_weight": 0.65, "range": np.linspace(p_bounds[2]+p_bounds[2]/1e4,p_bounds[1],500), "formula": eos_list_crust[1]["num_formula"], "color": eos_list_crust[1]["color"]},
                 {"name": tr["layer"] + " 3", "radius_weight": 0.85, "range": np.linspace(p_bounds[3]+p_bounds[3]/1e4,p_bounds[2],500), "formula": eos_list_crust[2]["num_formula"], "color": eos_list_crust[2]["color"]},
                 {"name": tr["layer"] + " 4", "radius_weight": 1., "range": np.linspace(10**-12,p_bounds[3],500), "formula": eos_list_crust[3]["num_formula"], "color": eos_list_crust[3]["color"]}
                 ]
    
    return dictionary

# Plotting the crust EoS graph
def wdg1_crust_eos_fig(lang,highlight_index=None):
    tr = translations_eos_widgets_NS[lang]
    fig = go.Figure()

    for i in range(0,len(eos_info_wdg1(lang))):
        P = eos_info_wdg1(lang)[i]["range"]
        eos_form = eos_info_wdg1(lang)[i]["formula"]
        eos_width = 4 if i==highlight_index else 2
        e = eos_form(P)
        fig.add_trace(go.Scatter(
            x=P, y=e,
            mode='lines',
            name=eos_info_wdg1(lang)[i]["name"],
            line=dict(
                color=eos_info_wdg1(lang)[i]["color"],
                width=eos_width,
                dash="solid"
            ),
            hovertemplate=f'{eos_info_wdg1(lang)[i]["name"]}<br>P: %{{x:.5e}}<br>ε(P): %{{y:.5e}}<extra></extra>',
            customdata=np.full_like(P, i)
        ))

    fig.update_layout(
        title=tr["widget_1"]["graph1_title"],
        xaxis=dict(tickmode = 'linear'),
        xaxis_title="P [MeV&#183;fm<sup>-3</sup>]",
        yaxis_title="ε(P) [MeV&#183;fm<sup>-3</sup>]",
        xaxis_type="log",
        yaxis_type="log",
        plot_bgcolor="gray",
        paper_bgcolor="black",
        font=dict(color="white",size=11,family="Arial"),
        height=400,
        margin=dict(t=40, b=40, l=40, r=40),
        #showlegend=True,
    )
    
    return fig

# Plotting the Neutron Star Structure
def wdg1_star_structure_figure(lang,layers_perc_factor=0,highlight_index=None):
    tr = translations_eos_widgets_NS[lang]
    fig = go.Figure()
    radius_star = 0.45
    center = (0.5, 0.55)

    

    for i in range(len(eos_info_wdg1(lang))-1,-1,-1):
        radius_layer = radius_star - (0.5-layers_perc_factor)*radius_star + eos_info_wdg1(lang)[i]["radius_weight"]*(0.5-layers_perc_factor)*radius_star
        edge_color = "white" if type(highlight_index)==int and (i == highlight_index or i == highlight_index-1) else eos_info_wdg1(lang)[i]["color"]
        edge_width = 1.5 if type(highlight_index)==int and (i == highlight_index or i == highlight_index-1) else 1
        fig.add_shape(dict(
            type="circle",
            xref="paper", yref="paper",
            x0=center[0] - radius_layer, y0=center[1] - radius_layer,
            x1=center[0] + radius_layer, y1=center[1] + radius_layer,
            line=dict(color=edge_color, width=edge_width),
            fillcolor=eos_info_wdg1(lang)[i]["color"],
            opacity=0.75,
            layer="between"
        ))
    # Showing the percentage of the CORE as text in the center    
    fig.add_trace(go.Scatter(
    x=[center[0]], y=[center[1]],
    mode='text',
    name="None",
    text=f"<b>{100*(0.5+layers_perc_factor):.1f}%</b>",
    textfont=dict(
        size=20,   
        color="white",   
        family="Arial"
    ),
    showlegend=False,
    ))

    fig.update_layout(
        title=tr["widget_1"]["graph2_title"],
        font=dict(color="white",size=11,family="Arial"),
        plot_bgcolor="black",
        paper_bgcolor="black",
        margin=dict(t=40, b=10, l=10, r=10),
        xaxis=dict(visible=False, range=[0, 1]),
        yaxis=dict(visible=False, range=[0, 1]),
        yaxis_scaleanchor="x",
        yaxis_scaleratio=1,
        xaxis_scaleratio=1,
        height=450,
        width=450
    )

    return fig

# =============================================================================================
# WIDGET 2: DESCRIBING THE STRUCTURE OF A NEUTRON STAR II (CORE)

# Plotting the selecetd core EoS model
def wdg2_core_eos_fig(lang,model=None,color="black"):
    tr = translations_eos_widgets_NS[lang]
    fig = go.Figure()
    
    # Default case (no model is selected)
    if model==None:
        fig.add_trace(go.Scatter(
            x=[1], y=[1],
            mode='lines',
            name="None",
            line=dict(
                color=color,
                width=1,
                dash="solid"
            ),
            hovertemplate=f'None<br>P: %{{x:.5e}}<br>ε(P): %{{y:.5e}}<extra></extra>',
        ))

        fig.update_layout(title=tr["widget_2"]["graph2_title"]+"None")

    else:
        filename = "data\main_NS\"+model+"_sol.csv"
        eos_data = file_read(filename,EOS_type="main")
        P_data = eos_data[0]
        Ec_data = eos_data[1]
        eos_width=3
        
        # Plotting the data that do not violate causality
        fig.add_trace(go.Scatter(
            x=P_data[0], y=Ec_data[0],
            mode='lines',
            name=model+" no caus. viol.",
            line=dict(
                color=color,
                width=eos_width,
                dash="solid"
            ),
            hovertemplate=f'{model}<br>P: %{{x:.5e}}<br>ε(P): %{{y:.5e}}<br>no caus. violation<extra></extra>',
        ))
        
        # Plotting the data that violate causality
        fig.add_trace(go.Scatter(
            x=P_data[1], y=Ec_data[1],
            mode='lines',
            name=model+" caus. viol.",
            line=dict(
                color="white",
                width=0.5*eos_width,
                dash="dash"
            ),
            hovertemplate=f'{model}<br>P: %{{x:.5e}}<br>ε(P): %{{y:.5e}}<br>caus. violation<extra></extra>',
        ))

        fig.update_layout(title=tr["widget_2"]["graph2_title"]+f"ε<sub>{model}</sub>(P)")
        
    fig.update_layout(
        #xaxis=dict(tickmode = 'linear'),
        xaxis_title="P [MeV&#183;fm<sup>-3</sup>]",
        yaxis_title="ε(P) [MeV&#183;fm<sup>-3</sup>]",
        # xaxis_type="log",
        # yaxis_type="log",
        plot_bgcolor="gray",
        paper_bgcolor="#CCC8C8",
        font=dict(color="black",size=11,family="Arial"),
        height=475,
        width=675,
        margin=dict(t=40, b=40, l=40, r=40),
        #showlegend=True,
    )

    return fig

# =============================================================================================
# WIDGET 3: POLYTROPIC AND LINEAR EQUATIONS OF STATE


# Section 1: Polytropic Grid
def wdg3_plot_poly(Γ_combo,ρ_segs_bounds,P_sat,clr_grid,width_grid,main_eos,show_leg,figure):
    n = len(Γ_combo)
    ρi = ρ_segs_bounds[0]
    Pi = P_sat
    
    # Iterating over segments
    for i in range(0,n):
        Ki = K_calc(Pi,ρi,Γ_combo[i])
        ρ_range=np.linspace(ρ_segs_bounds[i],ρ_segs_bounds[i+1],200)
        if show_leg==True:
            j=0
            Γ_combo_label = "Γ:"
            Γ_combo_label = Γ_combo_label+str(Γ_combo[j])
            j=j+1
            while j<len(Γ_combo):
                Γ_combo_label=Γ_combo_label+">"+str(Γ_combo[j])
                j=j+1
        else:
            Γ_combo_label = " "        
        show_memo = True if i==0 and show_leg else False    
        # Plotting the data that violate causality
        figure.add_trace(go.Scatter(
            x=ρ_range/ρ_sat_MeV, y=P_poly(ρ_range,Ki,Γ_combo[i]),
            mode='lines',
            name=Γ_combo_label,
            line=dict(
                color=clr_grid,
                width=width_grid,
                dash="solid",
            ),
            showlegend=show_memo,
            hovertemplate=f'ρ: %{{x:.5e}} (x ρ<sub>sat</sub>)<br>P(ρ): %{{y:.5e}}<br>Segment: {i+1:d}<br>Γ value: {Γ_combo[i]:.1f}<br>Main EoS: {main_eos}<extra></extra>',
        ))
        ρi = ρ_segs_bounds[i+1]
        Pi = P_poly(ρ_segs_bounds[i+1],Ki,Γ_combo[i])    

    

# Getting the Γ combos and plotting the respective grids for HLPS-2 and HLPS-3 
def wdg3_poly_grid(Γ_vals_num,num_segs,rho_n_factor,main_eos_choice,HLPS_2_grid_choice,HLPS_3_grid_choice,lang):
    tr = translations_eos_widgets_NS[lang]
    fig = go.Figure()

    # Getting the available choices for the Γ values
    if Γ_vals_num==2:
        Γ_choices=[1,4]
    elif Γ_vals_num==4:
        Γ_choices=[1,2,3,4]

    # Getting all the combos of Γ values
    Γ_combos = Γ_total_combos_num(Γ_choices=Γ_choices,num_segments=num_segs)
    Γ_combos_sorted = sorted(Γ_combos)

    # Calculating the bounds of the entire polytropic mass density region
    ρ_0 = ρ_sat_MeV
    ρ_n = rho_n_factor*ρ_sat_MeV
    log_ρ0 = np.log(ρ_0)
    log_ρn = np.log(ρ_n)
    
    # Getting the bounds of all mass density segments
    ρ_seg_bounds = np.exp(np.linspace(log_ρ0,log_ρn,num_segs+1))

    
             
    if main_eos_choice=="None":
        fig.add_trace(go.Scatter(
                x=[1], y=[1],
                mode='lines',
                name="n",
                line=dict(
                    color="white",
                    width=0.5,
                    dash="dash"
                ),
                hovertemplate=f'P: %{{x:.5e}}<br>ε(P): %{{y:.5e}}<br><extra></extra>',
            ))
        fig.update_layout(title=tr["widget_3"]["sec1_poly_grid_graph"]+": None")
    elif main_eos_choice=="HLPS-2":
        clr_grid_eos = "darkgreen"
        clr_grid_eos_select = "#570C0C"
        m = len(Γ_combos)
        for i in range(0,m):
            wdg3_plot_poly(Γ_combos[i],ρ_seg_bounds,P_sat_HLPS_2,clr_grid_eos,2,"HLPS-2",show_leg=False,figure=fig)    
        wdg3_plot_poly(Γ_combos_sorted[HLPS_2_grid_choice],ρ_seg_bounds,P_sat_HLPS_2,clr_grid_eos_select,4,"HLPS-2",show_leg=True,figure=fig)
        fig.update_layout(title=tr["widget_3"]["sec1_poly_grid_graph"]+f": HLPS-2 ({m} EoSs)")    
    elif main_eos_choice=="HLPS-3":
        clr_grid_eos = "gold"
        clr_grid_eos_select = "#164088"
        m = len(Γ_combos)
        for i in range(0,m):
            wdg3_plot_poly(Γ_combos[i],ρ_seg_bounds,P_sat_HLPS_3,clr_grid_eos,2,"HLPS-3",show_leg=False,figure=fig)
        wdg3_plot_poly(Γ_combos_sorted[HLPS_3_grid_choice],ρ_seg_bounds,P_sat_HLPS_3,clr_grid_eos_select,4,"HLPS-3",show_leg=True,figure=fig) 
        fig.update_layout(title=tr["widget_3"]["sec1_poly_grid_graph"]+f": HLPS-3 ({m} EoSs)")
    elif main_eos_choice=="Both":
        clr_grid_eos_1 = "darkgreen"
        clr_grid_eos_select_1 = "#570C0C"
        clr_grid_eos_2 = "gold"
        clr_grid_eos_select_2 = "#164088"
        m = len(Γ_combos)
        for i in range(0,m):
            wdg3_plot_poly(Γ_combos[i],ρ_seg_bounds,P_sat_HLPS_2,clr_grid_eos_1,2,"HLPS-2",show_leg=False,figure=fig)
        for i in range(0,m):
            wdg3_plot_poly(Γ_combos[i],ρ_seg_bounds,P_sat_HLPS_3,clr_grid_eos_2,2,"HLPS-3",show_leg=False,figure=fig)
        wdg3_plot_poly(Γ_combos_sorted[HLPS_2_grid_choice],ρ_seg_bounds,P_sat_HLPS_2,clr_grid_eos_select_1,4,"HLPS-2",show_leg=True,figure=fig)
        wdg3_plot_poly(Γ_combos_sorted[HLPS_3_grid_choice],ρ_seg_bounds,P_sat_HLPS_3,clr_grid_eos_select_2,4,"HLPS-3",show_leg=True,figure=fig)      
        fig.update_layout(title=tr["widget_3"]["sec1_poly_grid_graph"]+f": HLPS-2 + HLPS-3 ({m}+{m}={2*m} EoSs)")            

    
    fig.update_layout(
        #xaxis=dict(tickmode = 'linear'),
        xaxis_title=tr["widget_3"]["mass_density"]+" ρ/ρ<sub>sat</sub>",
        yaxis_title="P [MeV&#183;fm<sup>-3</sup>]",
        xaxis_type="log",
        yaxis_type="log",
        plot_bgcolor="#807F7F",
        paper_bgcolor="#CCC8C8",
        font=dict(color="black",size=11,family="Arial"),
        height=500,
        width=675,
        margin=dict(t=40, b=40, l=40, r=40),
        showlegend=True,
    )
    return fig

