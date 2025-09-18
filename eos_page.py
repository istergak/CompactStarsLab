# Python Script: 4a
# Filename: eos_page.py

# Description:
# Module for the page with interactive widgets for the EOSs of Compact Stars

# Required by: home_page.py, main_script.py


from dash import html, dcc, callback, Input, Output, State, callback_context
import dash
from translations import translations_eospage, translations_eos_widgets_NS
from eos_widgets_NS import *

# Forming the layout of the eos page of the app
def layout(lang):
    tr = translations_eospage[lang]


    return html.Div([
        # Return back button
        html.Div([
            dcc.Link("← " + tr["back_to_home"], href="/home_page", className="back-link")
        ], style={"position": "absolute", "top": "15px", "left": "15px"}),

        html.H1(tr["eos_title"], style={"textAlign": "center", "color": "white"}),
        
        # Introduction 
        html.Div([
            dcc.Markdown(tr["eos_intro_1"], style={"color": "white", "textAlign": "justify"}),
            dcc.Markdown(tr["eos_intro_2"],mathjax=True,style={"color": "white","textAlign": "center"}),
            dcc.Markdown(tr["eos_intro_3"], style={"color": "white", "textAlign": "justify"})
        ], style={"marginTop": "50px"}),

        # Two buttons for choosing the type of star
        html.Div([
            html.Button(tr["NS_button_1"], id="neutron-btn-1", n_clicks=0, className="eoswidget-toggle-btn"),
            html.Span(" | ", style={"color": "white", "padding": "0 10px"}),
            html.Button(tr["NS_button_2"], id="neutron-btn-2", n_clicks=0, className="eoswidget-toggle-btn"),
            html.Span(" | ", style={"color": "white", "padding": "0 10px"}),
             html.Button(tr["NS_button_3"], id="neutron-btn-3", n_clicks=0, className="eoswidget-toggle-btn"),
            html.Span(" | ", style={"color": "white", "padding": "0 10px"}),
            html.Button(tr["QS_button"], id="quark-btn", n_clicks=0, className="eoswidget-toggle-btn"),
        ], style={"textAlign": "center", "marginTop": "30px"}),

        # Showing widgets based on the selected type of star 
        html.Div(id="star-content", style={"marginTop": "40px"})
    ], className="dark-page")


# Saving and updating the shown interactive widgets based on the selected star type
@callback(
    Output("star-content", "children"),
    [Input("neutron-btn-1", "n_clicks"),
     Input("neutron-btn-2", "n_clicks"),
     Input("neutron-btn-3", "n_clicks"),
     Input("quark-btn", "n_clicks")],
    State("lang-store", "data")
)
def update_star_content(neutron_clicks_1,neutron_clicks_2, neutron_clicks_3,quark_clicks,lang):
    tr = translations_eos_widgets_NS[lang]

    ctx = callback_context

    if not ctx.triggered:
        return html.Div([
            html.P(tr["Default_widget_message"], style={"color": "gray", "textAlign": "center"})
        ])

    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    # NEUTRON STAR WIDGETS
    
    # =============================================================================================
    # WIDGET 1
    if triggered_id == "neutron-btn-1":
        mass_ticks = [0.5,1,1.5,2,2.5]
        marks_star_mass = {i:{"label": f"{i:.1f}","style": {"fontSize": "13px", "color": "white"}} for i in mass_ticks}
        
        return html.Div([
            
            # Title and basic info
            html.H2(tr["widget_1"]["title"], style={"color": "white"}),
            html.P(tr["widget_1"]["subtitle"], style={"color": "white","textAlign": "justify"}),
            html.H3(tr["widget_1"]["section"], style={"color": "white"}),
            dcc.Markdown(tr["widget_1"]["text"], style={"color": "white","textAlign": "justify"}),

            # Figures
            html.Div([
            dcc.Graph(id="wdg1-fig-crust-eos", figure=wdg1_crust_eos_fig(lang)),
            dcc.Graph(id="wdg1-fig-NS-2D-struct", figure=wdg1_star_structure_figure(lang))
            ], style={'display': 'flex', 'justifyContent': 'space-between',"marginBottom": "-50px"}),
 
            html.Div([
                # Hover Info
                html.Div([
                dcc.Markdown(id="wdg1-hover-info-title",style={"font-size": 15, "color": "white","marginLeft":"5px"}),
                dcc.Markdown(id="wdg1-hover-info",mathjax=True,style={"font-size": 15, "color": "white","marginLeft":"5px"})
                ],style={"border": "2px solid red", "borderRadius": "12px", "width": "835px"}),
                # Mass of the Star slider
                html.Div([
                dcc.Markdown(tr["widget_1"]["star_mass_slider"],mathjax=True,style={"font-size": 15, "color": "white","marginLeft":"5px"}),
                html.Div(dcc.Slider(id="wdg1-star-mass-slider",min=0.5,max=2.5,step=0.05,value=0.5,marks=marks_star_mass,tooltip={"style": {"always_visible": True,"color": "Black", "fontSize": "14px","placement": "bottom"}}),style={"width":"300px","height":"40px","border":"2.5px solid gray","borderRadius":"12px","background":"darkgreen","marginLeft":"10px","marginTop":"40px"})
                ],style={"border": "2px solid darkgreen", "borderRadius": "12px", "width": "350px","height":"130px","marginTop": "50px","marginLeft":"50px"}),
            ], style={'display': 'flex', 'justifyContent': 'justify'})    
            
        ],style={"marginBottom":"-5px"})
    # =============================================================================================
    # WIDGET 2
    elif triggered_id == "neutron-btn-2":
        # General info of the NS Core EoS models
        models_type1 = "*APR-1, BGP, BL-n, DH, HHJ-n, MDI-n, SCVBB, Ska, SkI4, W, WFF-n*"
        models_type2 = "*HLPS-n, NLD, PS*"
        genform_type1 = r"$\epsilon_{core}=g_1(P)=A\cdot P^{c_1} + B\cdot P^{c_2}$"
        genform_type2 = r"$\epsilon_{core}=g_2(P)=A\cdot (1-e^{-c_1P}) + B\cdot (1-e^{-c_2P}) + C$"
        memo_type1 = fr"""
        {tr["widget_2"]["graph1_memo_text_genformula"]}  
        {genform_type1}  
        {tr["widget_2"]["graph1_memo_text_models"]}  
        {models_type1}"""
        memo_type2 = fr"""
        {tr["widget_2"]["graph1_memo_text_genformula"]}  
        {genform_type2}  
        {tr["widget_2"]["graph1_memo_text_models"]}  
        {models_type2}"""

        # Name list of the core EoSs
        eos_core_name_list = []
        for i in range(len(eos_list_core)):
            eos_core_name_list.append(eos_list_core[i]["name"])
        eos_core_name_list.append("None")    
        
        return html.Div([
            
            # Title and basic info
            html.H2(tr["widget_2"]["title"], style={"color": "white"}),
            html.P(tr["widget_2"]["subtitle"], style={"color": "white","textAlign": "justify"}),
            html.H3(tr["widget_2"]["section"], style={"color": "white"}),
            dcc.Markdown(tr["widget_2"]["text"], style={"color": "white","textAlign": "justify"}),

            # Section 1: All 21 core EOS models
            html.Div([
                # Image
                html.Div([
                    html.P([tr["widget_2"]["graph1_title"],"ε",html.Sub("core"),"(P)"],style={"font-size": 15,"color": "white","textAlign": "left"}),
                    html.Img(id="wdg2-21-models-img",src="/assets/main_NS/mainNS_EOSs_fig.png", style={"height": 475, "width": 800, 'display': 'flex', "justify-content": "center"})
                ], style={'marginRight': "40px"}),
                # Memo
                html.Div([
                    html.P(tr["widget_2"]["graph1_memo"], style={"font-size": 15, "color": "white","textAlign": "left"}),
                     # Colored solid lines explanation
                    html.Div([
                        html.Div([
                            html.P([html.Span(" ",  style={"display": "inline-block", "width": "20px","border-bottom": "2px solid red", "vertical-align": "middle"}),tr["widget_2"]["graph1_memo_text_caus"]],style={"color": "white"}),
                            dcc.Markdown(r"$\frac{c_s}{c}\leq 1$",mathjax=True,style={"color": "white"})
                            ],style={"font-size": 15,'display': 'flex','justifyContent': 'normal',"marginLeft":"5px"}),
                        # Button to make causality parts bolder
                        dcc.Checklist(id='wdg2-bolder-caus',options=[{'label': tr["widget_2"]["graph1_memo_checklist"], 'value': 1}], value=[], inline=True,style={"font-size": 13, "color": "white","marginBottom":"5px"})
                    ],style={"border": "1.5px solid red", "borderRadius": "12px","width":"375px","marginBottom":"10px"}),    
                    # Gray dashed lines explanation
                    html.Div([
                        html.Div([
                            html.P([html.Span(" ",  style={"display": "inline-block", "width": "20px","border-bottom": "2px dashed grey", "vertical-align": "middle"}),tr["widget_2"]["graph1_memo_text_no_caus"]],style={"color": "white"}),
                            dcc.Markdown(r"$\frac{c_s}{c}> 1$",mathjax=True,style={"color": "white"})
                            ],style={"font-size": 15,'display': 'flex','justifyContent': 'normal',"marginLeft":"5px","marginBottom":"5px"}),
                        # Button to make none causality parts bolder
                        dcc.Checklist(id='wdg2-bolder-no-caus',options=[{'label': tr["widget_2"]["graph1_memo_checklist"], 'value': 1}], value=[], inline=True,style={"font-size": 13, "color": "white","marginBottom":"5px"}),
                    ],style={"border": "1.5px dashed gray", "borderRadius": "12px","width":"375px","marginBottom":"10px"}),
                    # Type 1 of core EOSs summary
                    html.Div([
                        dcc.Markdown(tr["widget_2"]["graph1_memo_text_eostype1"],style={"font-size": 14, "color": "white","marginLeft":"5px"}),
                        dcc.Markdown(memo_type1,mathjax=True,style={"font-size": 14,"color": "white","marginLeft":"5px"})
                    ],style={"border": "1.5px solid #4A7762", "borderRadius": "12px","width":"375px","marginBottom":"10px"}),       
                    # Type 2 of core EOSs summary
                    html.Div([
                        dcc.Markdown(tr["widget_2"]["graph1_memo_text_eostype2"],style={"font-size": 14, "color": "white","marginLeft":"5px"}),
                        dcc.Markdown(memo_type2,mathjax=True,style={"font-size": 14,"color": "white","marginLeft":"5px"})
                    ],style={"border": "1.5px solid #4A7762", "borderRadius": "12px","width":"375px"})                      
                ])
        ], style={'display': 'flex', 'justifyContent': 'normal',"marginBottom":"20px"}),

        # Section 2: Selection of a core EoS model
        html.Div([
            # Selection and info of the selected core EoS model
            html.Div([
                html.P([tr["widget_2"]["model_select_title"],"ε",html.Sub("core"),"(P)"],style={"font-size": 15,"color": "white","textAlign": "left"}),
                # Choosing the model
                dcc.Markdown(tr["widget_2"]["model_select_choice"],style={"font-size": 15,"color": "white","textAlign": "left"}),
                dcc.RadioItems(id='wdg2-core-eos-radio',options=eos_core_name_list,value="None",inline=True,style={"font-size": 15,"color": "black","width":"600px","background":"#4A7762","border":"2.5px solid orange", "borderRadius": "12px"}),
                # Fullname of the model
                dcc.Markdown(tr["widget_2"]["model_select_fullname"],style={"font-size": 15,"color": "white","textAlign": "left"}),
                dcc.Markdown(id="wdg2-eos-core-fullname",style={"font-size": 15,"color": "white","textAlign": "center", "border":"2.5px dashed orange", "borderRadius": "12px"}),
                # General type of the model
                dcc.Markdown(tr["widget_2"]["model_select_type"],style={"font-size": 15,"color": "white","textAlign": "left"}),
                dcc.Markdown(id="wdg2-eos-core-type",style={"font-size": 15,"color": "white", "textAlign": "center","border":"2.5px dashed orange", "borderRadius": "12px"}),
                # Formula of the model's equation of state
                dcc.Markdown(tr["widget_2"]["model_select_formula"],style={"font-size": 15,"color": "white","textAlign": "left"}),
                dcc.Markdown(id="wdg2-eos-core-formula",mathjax=True,style={"font-size": 15,"color": "white", "textAlign": "center","border":"2.5px dashed orange", "borderRadius": "12px"})
            ]),
            # Graph of the selected core EoS model
            dcc.Graph(id="wdg2-selected-model-graph",figure=wdg2_core_eos_fig(lang),style={"marginTop": "30px","marginLeft": "30px","marginTop": "10px"})
        ],style={'display': 'flex', 'justifyContent': 'normal',"marginTop":"20px"})
            
        ])
    # =============================================================================================
    # WIDGET 3
    elif triggered_id == "neutron-btn-3":
    
        
        return html.Div([

            # Title and basic info
            html.H2(tr["widget_3"]["title"], style={"color": "white"}),
            html.P(tr["widget_3"]["subtitle"],style={"color": "white","textAlign": "justify"}),
            dcc.Markdown(tr["widget_3"]["total_eos_form"],mathjax=True,style={"color": "white","textAlign": "center"}),
            html.P(tr["widget_3"]["subtitle_2"],style={"color": "white","textAlign": "justify"}),
            dcc.Markdown(tr["widget_3"]["core_eos_form_main"],mathjax=True,style={"color": "white","textAlign": "center"}),
            dcc.Markdown(tr["widget_3"]["subtitle_3"],mathjax=True,style={"color": "white","textAlign": "justify"}),

            # Section 1: Polytropic Grid
            # Text
            html.H3(tr["widget_3"]["section_1"], style={"color": "white"}),
            dcc.Markdown(tr["widget_3"]["sec1_text_poly1"],mathjax=True,style={"color": "white","textAlign": "justify"}),
            dcc.Checklist(id='wdg3-show-poly-method',options=[{'label': tr["widget_3"]["sec1_show_method_btn"], 'value': 1}], value=[], inline=True,style={"font-size": 15, "color": "white","textAlign": "center"}),
            
            html.Div(id="wdg3-poly-method",children=[#dcc.Markdown("<"+116*"="+">",style={"color": "white","textAlign": "center"}),
                dcc.Markdown(tr["widget_3"]["sec1_text_poly2"],mathjax=True,style={"color": "white","textAlign": "justify","margin":"10px"}),
                dcc.Markdown(tr["widget_3"]["sec1_text_poly3a"],mathjax=True,style={"color": "white","textAlign": "justify","margin":"10px"}),
                # P-ρ relation
                dcc.Markdown(r"$P=K_i\rho^{\Gamma_i}$",mathjax=True,style={"color": "white","textAlign": "center"}), 
                dcc.Markdown(tr["widget_3"]["sec1_text_poly3b"],mathjax=True,style={"color": "white","textAlign": "justify","margin":"10px"}),
                # K_i constant calculation
                dcc.Markdown(r"$K_i=\frac{P_{i-1}}{\rho^{\Gamma_i}_{i-1}}=\frac{P_i}{\rho^{\Gamma_i}_i}$",mathjax=True,style={"color": "white","textAlign": "center"}), 
                dcc.Markdown(tr["widget_3"]["sec1_text_poly3c"],mathjax=True,style={"color": "white","textAlign": "justify","margin":"10px"}),
                # Γ_i parameter calculation
                dcc.Markdown(r"$\Gamma_i=\frac{\log_{10}(P_i/P_{i-1})}{\log_{10}(\rho_i/\rho_{i-1})}$.",mathjax=True,style={"color": "white","textAlign": "center"}), 
                dcc.Markdown(tr["widget_3"]["sec1_text_poly3d"],mathjax=True,style={"color": "white","textAlign": "justify","margin":"10px"}),
                # ε(P) (Γ!=1)
                dcc.Markdown(r"$\epsilon(P)=\left[\frac{\epsilon(\rho_{i-1})}{\rho_{i-1}}-\frac{P_{i-1}}{\rho_{i-1}(\Gamma_i -1)}\right]\left(\frac{P}{K_i}\right)^{\Gamma_i^{-1}}+\frac{P}{\Gamma_i-1}$",mathjax=True,style={"color": "white","textAlign": "center"}), 
                dcc.Markdown(tr["widget_3"]["sec1_text_poly3e"],mathjax=True,style={"color": "white","textAlign": "justify","margin":"10px"}),
                # ε(P) (Γ=1)
                dcc.Markdown(r"$\epsilon(P)=\frac{\epsilon(\rho_{i-1})}{\rho_{i-1}}\frac{P}{K_i}+\ln\left(\frac{1}{\rho_{i-1}}\right)P-\ln\left(\frac{K_i}{P}\right)P$",mathjax=True,style={"color": "white","textAlign": "center"}), 
                dcc.Markdown(tr["widget_3"]["sec1_text_poly4a"],mathjax=True,style={"color": "white","textAlign": "justify","margin":"10px"}),
                # EoS NS (total)
                dcc.Markdown(r"$\epsilon(P) = \begin{cases} \epsilon_{crust}(P), &P<P_{crust-core} \\ \epsilon_{main}(P), &P_{crust-core}\leq P<P_0 \\ \epsilon_{poly}(P), & P_0\leq P\leq P_{n} \end{cases}$",mathjax=True,style={"color": "white","textAlign": "center"}), 
                dcc.Markdown(tr["widget_3"]["sec1_text_poly4b"],mathjax=True,style={"color": "white","textAlign": "justify","margin":"10px"}),
                # EoS NS (core)
                dcc.Markdown(r"$\epsilon_{core}(P) =\begin{cases} \epsilon_{main}(P), &P_{crust-core}\leq P<P_0 \\ \epsilon_{poly}(P), & P_0\leq P\leq P_{n} \end{cases}$",mathjax=True,style={"color": "white","textAlign": "center"}), 
                dcc.Markdown(tr["widget_3"]["sec1_text_poly4c"],mathjax=True,style={"color": "white","textAlign": "justify","margin":"10px"}),
                # Γ combos
                dcc.Markdown(r"$f=l^n$",mathjax=True,style={"color": "white","textAlign": "center"}), 
                dcc.Markdown(tr["widget_3"]["sec1_text_poly4d"],mathjax=True,style={"color": "white","textAlign": "justify","margin":"10px"}),
                ],
            style={"display": "none"}),
            #dcc.Markdown("<"+116*"="+">",style={"color": "white","textAlign": "center"}),

            # Interactive widget
            html.Div([
                # Selection of grid parameters
                html.Div([
                    html.P(tr["widget_3"]["sec1_gridpar_title"],style={"font-size": 15,"color": "white","textAlign": "left"}),
                    html.Div([
                        # Gamma values selection
                        html.Div([
                            dcc.Markdown(tr["widget_3"]["sec1_Gamma_vals_select"],mathjax=True,style={"font-size": 15,"color": "white","textAlign": "left"}),
                            dcc.RadioItems(id='wdg3-poly-grids-gamma',options=[{"label":tr["widget_3"]["sec1_Gamma_vals_choice1"],"value":2},{"label":tr["widget_3"]["sec1_Gamma_vals_choice2"],"value":4}],value=2,style={"font-size": 16,"color": "black","background":"#CA6E54","border":"3px solid gray","borderRadius":"12px","width":"150px","margin":"20px"}),
                        ],style={"width":"300px","background":"#3B3B3B","border":"2px dashed gray","borderRadius":"12px","marginRight":"10px"}),
                        # Number of polytropic segments selection
                        html.Div([
                            dcc.Markdown(tr["widget_3"]["sec1_segments_select"],mathjax=True,style={"font-size": 15,"color": "white","textAlign": "left"}),
                            dcc.RadioItems(id='wdg3-poly-grids-segs',options=[1,2,4],value=1,inline=True,style={"font-size": 16,"color": "black","width":"250px","border":"3px solid gray","borderRadius":"12px","background":"#CA6E54","margin":"20px"},labelStyle={"display": "inline-block","marginLeft": "30px","marginRight": "10px","marginTop":"10px","marginBottom":"10px"}),
                        ],style={"width":"300px","background":"#3B3B3B","border":"2px dashed gray","borderRadius":"12px"}),
                    ],style={'display': 'flex','justifyContent': 'justify',"marginBottom":"10px","width":"600px"}),
                    # Value of final mass density ρ_n selection
                    html.Div([
                        dcc.Markdown(tr["widget_3"]["sec1_final_dens_select"],mathjax=True,style={"font-size": 15,"color": "white","textAlign": "left"}),
                        html.Div([html.Div(dcc.Slider(id='wdg3-poly-grids-final-dens',min=7.5,max=15,value=7.5,tooltip={"style": {"always_visible": True,"color": "Black", "fontSize": "14px","placement": "bottom"}}),style={"width":"500px","borderRadius":"12px","background":"#3D5C1E","marginLeft":"10px"}),
                            dcc.Markdown(r"($\times \rho_{sat}$)",mathjax=True,style={"font-size": 13,"color": "white","borderRadius":"12px","background":"#3D5C1E","marginLeft":"-25px","width":"75px","textAlign":"center"})],
                            style={"marginTop":"45px",'display': 'flex','justifyContent': 'normal',"marginBottom":"10px"}),
                    ],style={"width":"600px","background":"#3B3B3B","border":"2px dashed gray","borderRadius":"12px","marginBottom":"10px"}),
                    html.Div([
                        # "Main" EoS selection
                        html.Div([        
                            dcc.Markdown(tr["widget_3"]["sec1_main_eos_select"],style={"font-size": 15,"color": "white","textAlign": "left"}),
                            dcc.RadioItems(id='wdg3-poly-grids-main-eos',options=["None","HLPS-2","HLPS-3","Both"],value="None",inline=True,style={"font-size": 16,"color": "black","width":"100px","border":"3px solid gray","borderRadius":"12px","background":"#977829","margin":"10px"}),
                        ],style={"width":"250px","background":"#3B3B3B","border":"2px dashed gray","borderRadius":"12px","marginRight":"10px"}),
                        # Sliding over mock polytropic EoSs
                        html.Div([        
                            dcc.Markdown(tr["widget_3"]["sec1_poly_grid_scan"],style={"font-size": 15,"color": "white","textAlign": "left"}),
                            html.Div([
                                html.Div(dcc.Slider(id='wdg3-poly-grids-slider-HLPS-2',step=1,value=0,marks={0: {"label": "None", "style": {"fontSize": "13px", "color": "white"}}},tooltip={"style": {"always_visible": True,"color": "Black", "fontSize": "14px","placement": "bottom"}}),style={"width":"200px","height":"35px","border":"2.5px solid gray","borderRadius":"12px","background":"#6A0F0F","marginLeft":"10px","marginBottom":"10px"}),
                                dcc.Markdown("**HLPS-2**",style={"font-size": 15,"color": "#D33131","textAlign": "left","marginLeft":"5px"})
                            ],style={'display': 'flex','justifyContent': 'justify'}),
                            html.Div([
                                html.Div(dcc.Slider(id='wdg3-poly-grids-slider-HLPS-3',step=1,value=0,marks={0: {"label": "None", "style": {"fontSize": "13px", "color": "white"}}},tooltip={"style": {"always_visible": True,"color": "Black", "fontSize": "14px","placement": "bottom"}}),style={"width":"200px","height":"35px","border":"2.5px solid gray","borderRadius":"12px","background":"#4077D7","marginLeft":"10px"}),  
                                dcc.Markdown("**HLPS-3**",style={"font-size": 15,"color": "#3774DD","textAlign": "left","marginLeft":"5px"}),
                            ],style={'display': 'flex','justifyContent': 'justify'})    
                        ],style={"width":"350px","background":"#3B3B3B","border":"2px dashed gray","borderRadius":"12px"}),
                    ],style={'display': 'flex','justifyContent': 'justify',"marginBottom":"10px","width":"600px"})
                ]),

                # Polytropic Grid Graph
                dcc.Graph(id="wdg3-poly-grid-graph",figure=wdg3_poly_grid(Γ_vals_num=2,num_segs=1,rho_n_factor=7.5,main_eos_choice="None",HLPS_2_grid_choice=0,HLPS_3_grid_choice=0,lang=lang),style={"marginLeft":"20px"})
            ],style={'display': 'flex', 'justifyContent': 'normal',"marginTop":"20px"}),



            # Section 2: Maxwell transition
            html.H3(tr["widget_3"]["section_2"], style={"color": "white"}),
            
        ])
    # =============================================================================================
    # QUARK STARS WIDGETS

    # WIDGET 4
    elif triggered_id == "quark-btn":
        mit_btn_label = html.Div(tr["widget_4"]["mit_model_btn"],style={"color":"#D33131"})
        cfl_btn_label = html.Div(tr["widget_4"]["cfl_model_btn"],style={"color":"#3774DD"})

        return html.Div([
            html.H2(tr["widget_4"]["title"], style={"color": "white"}),
            dcc.Markdown(tr["widget_4"]["subtitle"],style={"color": "white","textAlign": "justify"}),
            dcc.Markdown(tr["widget_4"]["definition"],style={"color": "white","textAlign": "center"}),
            dcc.Markdown(tr["widget_4"]["subtitle_2"],style={"color": "white","textAlign": "justify"}),
            dcc.Markdown("$M\propto R^3$",mathjax=True,style={"color": "white","textAlign": "center"}),
            dcc.Markdown(tr["widget_4"]["subtitle_3"],style={"color": "white","textAlign": "justify"}),
            dcc.RadioItems(id='wdg4-model-info-btn',options=[{"label":mit_btn_label,"value":0},{"label":cfl_btn_label,"value":1}],value=0,inline=True,style={"font-size": 16,"color": "white","width":"300px","border":"2px solid gray","borderRadius":"12px","marginLeft":"500px","textAlign": "center"},labelStyle={"margin": "10px"}),
            html.Div(id='wdg4-model-info'),
        ])

# WIDGET 1: Updating the "wg1-fig-crust-eos", "wdg1-fig-NS-2D-struct" and "wdg1-hover-info" based on hover over "wdg1-fig-crust-eos"
@callback(
    Output('wdg1-hover-info-title', 'children'),
    Output('wdg1-hover-info', 'children'),
    Output('wdg1-fig-crust-eos','figure'),
    Output('wdg1-fig-NS-2D-struct','figure'),
    Input('wdg1-fig-crust-eos', 'hoverData'),
    Input("wdg1-star-mass-slider","value"),
    State("lang-store", "data")
)

# Syncing the eos plot with the 2D Neutron Star structure via hovering data
def wdg1_show_hover_data(hoverData,star_mass,lang):
    p = smp.symbols("P",positive=True)
    tr = translations_eos_widgets_NS[lang]

    # Calculating the analogy of crust and core based on star's mass
    if star_mass<=1: # from 0.5*M_sun to 1*M_sun the core percentage increases from 50% to 75% (the crust decreases from 50% to 25%)
        crust_core_perc_adj = (star_mass-0.5)*(0.75-0.5)/(1-0.5)
    elif 1<star_mass<=1.5: # from 1*M_sun to 1.5*M_sun the core percentage increases from 75% to 85% (the crust decreases from 25% to 15%)
        crust_core_perc_adj = 0.25 + (star_mass-1)*(0.85-0.75)/(1.5-1)
    elif 1.5<star_mass<=2: # from 1.5*M_sun to 2*M_sun the core percentage increases from 85% to 90% (the crust decreases from 15% to 10%)
        crust_core_perc_adj = 0.25 + 0.1 + (star_mass-1.5)*(0.9-0.85)/(2-1.5)
    elif star_mass>2:
        crust_core_perc_adj = 0.25 + 0.1 + 0.05 + (star_mass-2)*(0.95-0.9)/(2.5-2)     
    
    if hoverData and 'points' in hoverData and hoverData['points']:
        point = hoverData['points'][0]
        layer_id = point.get("curveNumber")
        # Hover over CORE region
        if layer_id==0:
            info_title = tr["widget_1"]["message_title"]
            region = tr["core"]
            region_info = tr["widget_1"]["message_region"]
            eos = r"$\epsilon_{Ska}(P)=0.53928\cdot P^{1.01394}+94.31452\cdot P^{0.35135}$"
            eos_info = tr["widget_1"]["message_region_eos"]
            p_range = [eos_info_wdg1(lang)[0]["range"][0],eos_info_wdg1(lang)[0]["range"][-1]]
            p_range = fr"$[{p_range[0]},{p_range[1]}]$"+r" $MeV\cdot fm^{-3}$"
            p_range_info = tr["widget_1"]["message_p_range"]

            hover_update = fr"""  
            {region_info}  
            **{region}**  
            {eos_info}  
            {eos}  
            {p_range_info}  
            {p_range}"""
            return info_title,hover_update,wdg1_crust_eos_fig(lang,highlight_index=layer_id),wdg1_star_structure_figure(lang,layers_perc_factor=crust_core_perc_adj,highlight_index=layer_id)
        # Hover over a CRUST LAYER region
        else:
            info_title = tr["widget_1"]["message_title"]
            region = tr["layer"]+f" {layer_id}"
            region_info = tr["widget_1"]["message_region"]
            if layer_id==1:
                eos = r"$\epsilon_{crust-layer_1}(P)=0.00873 + 103.17338\cdot(1-e^{-P/0.38527})+7.34979\cdot(1-e^{-P/0.01211})$"
            elif layer_id==2:
                eos = r"$\epsilon_{crust-layer_2}(P)=0.00015 + 0.00203\cdot(1-e^{-344827.5\cdot P})+0.10851\cdot(1-e^{7692.3076\cdot P})$"
            elif layer_id==3:
                eos = r"$\epsilon_{crust-layer_3}(P)=0.0000051\cdot(1-e^{-0.2373\cdot 10^{10}\cdot P})+0.00014\cdot(1-e^{-0.4020\cdot 10^8 \cdot P})$"
            elif layer_id==4:
                eos = r"""$\epsilon_{crust-layer_4}(P)=10^{31.93753 + 10.82611\cdot \log_{10}{(P)} + 1.29312\cdot [\log_{10}{(P)}]^2 + 0.08014\cdot [\log_{10}{(P)}]^3 + 0.00242\cdot [\log_{10}{(P)}]^4 + 0.000028\cdot [\log_{10}{(P)}]^5}$"""         
            eos_info = tr["widget_1"]["message_region_eos"]

            p_range = [eos_info_wdg1(lang)[layer_id]["range"][0],eos_info_wdg1(lang)[layer_id]["range"][-1]]
            p_range = fr"$[{p_range[0]:.5e},{p_range[1]:.5e}]$"+r" $MeV\cdot fm^{-3}$"

            p_range_info = tr["widget_1"]["message_p_range"]

            hover_update = fr"""  
            {region_info}  
            **{region}**  
            {eos_info}  
            {eos}  
            {p_range_info}  
            {p_range}"""
            return info_title,hover_update,wdg1_crust_eos_fig(lang,highlight_index=layer_id), wdg1_star_structure_figure(lang,layers_perc_factor=crust_core_perc_adj,highlight_index=layer_id)
    
    # Default case    
    else:
        info_title = tr["widget_1"]["message_title"]
        region = "none"
        region_info = tr["widget_1"]["message_region"]
        eos = "none"
        eos_info = tr["widget_1"]["message_region_eos"]
        p_range = "none"
        p_range_info = tr["widget_1"]["message_p_range"]
            
        hover_update = f""" 
            {region_info}  
            {region}  
            {eos_info}  
            {eos}  
            {p_range_info}  
            {p_range}"""
        return info_title,hover_update,wdg1_crust_eos_fig(lang),wdg1_star_structure_figure(lang,layers_perc_factor=crust_core_perc_adj)

    # If a click was made at some point, keep the plots as they are.
    raise dash.exceptions.PreventUpdate

# WIDGET 2: Updating the "wdg2-21-models-img" based on the selections in checklists 'wdg2-bolder-caus' and 'wdg2-bolder-no-caus'
@callback(
    Output("wdg2-21-models-img", 'src'),
    Input("wdg2-bolder-caus","value"),
    Input("wdg2-bolder-no-caus","value")
)

# WIDGET 2: Syncing the 21 core eos models image with the checklists in memo
def wdg2_update_img(selected_caus, selected_no_caus):
    # Both buttons are checked
    if 1 in selected_caus and 1 in selected_no_caus:
        return "/assets/main_NS/mainNS_EOSs_fig_bold_both.png"
    # "Make causality part bolder" button is checked
    elif 1 in selected_caus:
        return "/assets/main_NS/mainNS_EOSs_fig_bold_caus.png"
    # "Make none causality part bolder" button is checked
    elif 1 in selected_no_caus:
        return "/assets/main_NS/mainNS_EOSs_fig_bold_no_caus.png"
    # no button is selected checked
    else:
        return "/assets/main_NS/mainNS_EOSs_fig.png"
    
# WIDGET 2: Updating the "wdg2-eos-core-fullname", "wdg2-eos-core-type" and "wdg2-eos-core-formula" based on the model choice for the core EoS in "wdg2-eos-core-radio" 
@callback(
    Output("wdg2-eos-core-fullname", 'children'),
    Output("wdg2-eos-core-type", 'children'),
    Output("wdg2-eos-core-formula", 'children'),
    Output("wdg2-selected-model-graph", "figure"),
    Input("wdg2-core-eos-radio","value"),
    State("lang-store", "data")
)    

# WIDGET 2: Syncing the choice for the model of core EoS with its info
def wdg2_update_model_info(model,lang):
    # Default case (no model is selected)
    if model=="None":
        model_fullname="-"
        model_formula="-"
        model_type="-"
        model_figure=wdg2_core_eos_fig(lang)
    else:    
        # Getting info for the core EoS models and storaging them in lists
        eos_core_model = []
        eos_core_fullname = []
        eos_core_formula_mark = []
        eos_core_color = []
        for i in range(len(eos_list_core)):
            eos_core_model.append(eos_list_core[i]["name"])
            eos_core_fullname.append(eos_list_core[i]["fullname"])
            eos_core_formula_mark.append(eos_list_core[i]["markdown_formula"])
            eos_core_color.append(eos_list_core[i]["color"])

        # Locating the selected model
        idx_model =  eos_core_model.index(model)

        # Getting the fullname of the model
        model_fullname = f"*{eos_core_fullname[idx_model]}*"
        # Getting the markdown formula of the model
        model_formula = eos_core_formula_mark[idx_model]
        # Getting the type of the model
        if model in ["HLPS-2","HLPS-3","NLD","PS"]:
            model_type="2"
        else:
            model_type="1"
        # Getting the color of the model
        model_color = eos_core_color[idx_model]
        # Getting the figure of the model
        model_figure = wdg2_core_eos_fig(lang,model=model,color=model_color)           
    return model_fullname,model_type,model_formula,model_figure

# WIDGET 3: Updating the content of the "wdg3-poly-method" content based on the selection of the "wdg3-skip-method" checklist button
@callback(
    Output("wdg3-poly-method", 'style'),
    Input("wdg3-show-poly-method","value"),
    State("lang-store", "data")
)  

# WIDGET 3: Syncing "wdg3-poly-method" html.Div([]) and the "wdg3-skip-method" checklist button
def wdg3_show_poly_method(show_value,lang):
    tr=translations_eos_widgets_NS[lang]
    if 1 in show_value:
        return {"display": "block","border": "2px solid #4A7762", "borderRadius": "12px",}
    else:
        return {"display": "none"}
    
# WIDGET 3: Updating the content of the "wdg3-poly-grid-graph" content based on the selection of the "wdg3-poly-grids-gamma", "wdg3-poly-grids-segs", 
# "wdg3-poly-grids-final-dens" and "wdg3-poly-grids-main-eos" buttons

@callback(
    Output("wdg3-poly-grid-graph","figure"),
    Output("wdg3-poly-grids-slider-HLPS-2","marks"),
    Output("wdg3-poly-grids-slider-HLPS-2","min"),
    Output("wdg3-poly-grids-slider-HLPS-2","max"),
    Output("wdg3-poly-grids-slider-HLPS-3","marks"),
    Output("wdg3-poly-grids-slider-HLPS-3","min"),
    Output("wdg3-poly-grids-slider-HLPS-3","max"),
    Input("wdg3-poly-grids-gamma","value"),
    Input("wdg3-poly-grids-segs","value"),
    Input("wdg3-poly-grids-final-dens","value"),
    Input("wdg3-poly-grids-main-eos","value"),
    Input("wdg3-poly-grids-slider-HLPS-2","value"),
    Input("wdg3-poly-grids-slider-HLPS-3","value"),
    State("lang-store", "data")
)

# Syncing "wdg3-poly-grid-graph" content with the "wdg3-poly-grids-gamma", "wdg3-poly-grids-segs", 
# "wdg3-poly-grids-final-dens" and "wdg3-poly-grids-main-eos" buttons

def wdg3_update_poly_grid_graph(Γ_values,segments,final_dens,main_eos,HLPS_2_grid_choice,HLPS_3_grid_choice,lang):
    # Getting the combos of Γ values
    if Γ_values==2:
        Γ_choices=[1,4]
    elif Γ_values==4:
        Γ_choices=[1,2,3,4]
    Γ_combos = Γ_total_combos_num(Γ_choices=Γ_choices,num_segments=segments)

    # Reseting the selected model index to if it exceeds the Γ_combos list length
    if HLPS_2_grid_choice>len(Γ_combos):
        HLPS_2_grid_choice=1
    if HLPS_3_grid_choice>len(Γ_combos):
        HLPS_3_grid_choice=1  
      
    
    if main_eos=="None":
        marks_HLPS_2 = {0: {"label": "None", "style": {"fontSize": "13px", "color": "white"}}}
        marks_HLPS_3 = {0: {"label": "None", "style": {"fontSize": "13px", "color": "white"}}}
        return wdg3_poly_grid(Γ_vals_num=Γ_values,num_segs=segments,rho_n_factor=final_dens,main_eos_choice=main_eos,HLPS_2_grid_choice=0,HLPS_3_grid_choice=0,lang=lang), marks_HLPS_2,None, 0,marks_HLPS_3,None,0
    
    elif main_eos=="HLPS-2":
        marks_HLPS_2 = {1: {"label": "1", "style": {"fontSize": "13px", "color": "white"}}, len(Γ_combos): {"label": f"{len(Γ_combos)}", "style": {"fontSize": "13px", "color": "white"}}}
        marks_HLPS_3 = {0: {"label": "None", "style": {"fontSize": "13px", "color": "white"}}}
        return wdg3_poly_grid(Γ_vals_num=Γ_values,num_segs=segments,rho_n_factor=final_dens,main_eos_choice=main_eos,HLPS_2_grid_choice=HLPS_2_grid_choice-1,HLPS_3_grid_choice=0,lang=lang), marks_HLPS_2,1,len(Γ_combos), marks_HLPS_3,None,0
    
    elif main_eos=="HLPS-3":
        marks_HLPS_2 = {0: {"label": "None", "style": {"fontSize": "13px", "color": "white"}}}
        marks_HLPS_3 = {1: {"label": "1", "style": {"fontSize": "13px", "color": "white"}}, len(Γ_combos): {"label": f"{len(Γ_combos)}", "style": {"fontSize": "13px", "color": "white"}}}
        return wdg3_poly_grid(Γ_vals_num=Γ_values,num_segs=segments,rho_n_factor=final_dens,main_eos_choice=main_eos,HLPS_2_grid_choice=0,HLPS_3_grid_choice=HLPS_3_grid_choice-1,lang=lang), marks_HLPS_2,0,None, marks_HLPS_3,1,len(Γ_combos)
    
    elif main_eos=="Both":
        marks_HLPS_2 = {1: {"label": "1", "style": {"fontSize": "13px", "color": "white"}}, len(Γ_combos): {"label": f"{len(Γ_combos)}", "style": {"fontSize": "13px", "color": "white"}}}
        marks_HLPS_3 = {1: {"label": "1", "style": {"fontSize": "13px", "color": "white"}}, len(Γ_combos): {"label": f"{len(Γ_combos)}", "style": {"fontSize": "13px", "color": "white"}}}
        return wdg3_poly_grid(Γ_vals_num=Γ_values,num_segs=segments,rho_n_factor=final_dens,main_eos_choice=main_eos,HLPS_2_grid_choice=HLPS_2_grid_choice-1,HLPS_3_grid_choice=HLPS_3_grid_choice-1,lang=lang), marks_HLPS_2,1,len(Γ_combos), marks_HLPS_3,1,len(Γ_combos)


# WIDGET 4: Updating the "wdg4-model-info"  based on "wdg4-model-info-btn" selection
@callback(
    Output('wdg4-model-info', 'children'),
    Input("wdg4-model-info-btn","value"),
    State("lang-store", "data")
)

# Syncing "wdg4-model-info-btn" and "wdg4-model-info"
def wdg4_model_info(model_select,lang):
    tr=translations_eos_widgets_NS[lang]
    # MIT BAG model selection
    if model_select==0:
        return [
            html.H3(tr["widget_4"]["mit_model_title"], style={"color": "white"}),
        ]
    elif model_select==1:
        return [
            html.H3(tr["widget_4"]["cfl_model_title"], style={"color": "white"}),
        ]