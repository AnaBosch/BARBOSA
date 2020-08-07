# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

import layouts.headers.header as hd

#************************************************#
#  Diseño modular del cuadro de mandos principal #
#************************************************#

main_layout = html.Div(children=[
    #Se añade la cabecera de la aplicacion
    hd.header,

    #Títulos de los gráficos superiores
    html.Div([
        html.Label(
            'Repercusión por hashtag',
            className = 'titulos-graficos-izquierda',
            style={
                'textAlign': 'center',
                'fontFamily': 'Gill Sans',
                'lineHeight': 2.2,
                'color': 'white',
                'background': '#1822dc',
                'fontWeight': 100,
                'fontVariant': 'small-caps',
                'fontSize':17,
            }
        ),

        html.Label(
            'Repercusión por colaborador',
            className = 'titulos-graficos-derecha',
            style={
                'textAlign': 'center',
                'fontFamily': 'Gill Sans',
                'lineHeight': 2.2,
                'color': 'white',
                'background': '#1822dc',
                'fontWeight': 100,
                'fontVariant': 'small-caps',
                'fontSize':17,
                }
        ),
    ],
    style={
        'columnCount': 2,
        'marginTop': 80,
        'zIndex': 15,
        'position': 'relative'
    }),

    #Gráficos superiores
    html.Div([
        html.Div( #Gráfico que muestra la distribución de los temas en función del programa seleccionado
            dcc.Graph(
                id='graphic-distribucion-temas',
                config={
                    'displayModeBar': False
                }),

            style={
                'borderStyle': 'solid',
                'borderColor': '#1822dc',
                'borderWidth': 1,
                'paddingBottom': 10,
                'paddingTop': 11,
            }
        ),

        html.Div( #Gráfico que muestra la distribución de los colaboradores en función del programa seleccionado
            dcc.Graph(
                id='graphic-distribucion-colaborador',
                config={
                    'displayModeBar': False
                }),

            style={
               'borderStyle': 'solid',
               'borderColor': '#1822dc',
               'borderWidth': 1,
               'paddingBottom': 10,
               'paddingTop': 11,
           }
       ),
    ],
    style={
        'columnCount': 2,
        'marginTop': -16,
        'marginLeft': '3.7%',
        'marginRight': '3.7%',
        'paddingTop': 1,
        'zIndex': 0,
        'position': 'relative'
    }),

    #Título del gráfico inferior
    html.Label(
        'Análisis emocional',
        className='titulos-graficos-individual',
        style={
            'textAlign': 'center',
            'fontFamily': 'Gill Sans',
            'lineHeight': 2.2,
            'color': 'white',
            'background': '#1822dc',
            'fontWeight': 100,
            'fontVariant': 'small-caps',
            'fontSize':17,
            'marginTop': '6%',
            'zIndex': 999,
            'position': 'relative',
            'float': 'left'
            }
    ),

])
