# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

import layouts.headers.header as hd
import layouts.main_dash_layout as main

#************************************************#
#  Diseño modular del cuadro de mandos principal #
#************************************************#

valence_layout = html.Div(children=[

    #Se añade el cuerpo de la página principal
    main.main_layout,

    #Opción de cambiar de gráfico
    html.Div([
        dcc.Link('Valencia', href='http://127.0.0.1:8050/principal/valence/', className="option-button option-button-derecha option-button-active"),
        dcc.Link('Arousal', href='http://127.0.0.1:8050/principal/arousal/', className="option-button option-button-izquierda option-button-inactive"),

    ], className="diseño-option-button"),

    #Gráfico inferior
    html.Div( #Gráfico que muestra la distribución de los temas en función de su arousal y valencia
        dcc.Graph(
            id='graphic-valence',
            config={
                'displayModeBar': False
            }),

            style={
                'width' : '70%',
                'marginTop': '-1.8%',
                'marginLeft': '15%',
                'borderStyle': 'solid',
                'borderColor': '#1822dc',
                'borderWidth': 1,
                'paddingTop': 10,
                'paddingBottom': 10,
                'zIndex': 0,
                'position': 'relative',
           }
   ),
],style={ #Estilo de la página
    'borderStyle': 'solid',
    'borderColor': '#CCCCCC',
    'borderWidth': 5,
    'paddingBottom':50
})
