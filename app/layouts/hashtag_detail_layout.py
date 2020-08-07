# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import layouts.headers.header as hd

#**********************************************************#
#  Diseño modular del cuadro de mandos detalle de los tema #
#**********************************************************#

hashtag_detail_layout = html.Div([
    #Se añade la cabecera de la aplicacion
    hd.header,

    #Selector de tema en función del programa elegido en el cuadro de mandos principal
    html.Div( [
        dcc.Dropdown(
            id='select-tema',
            searchable=False,
            clearable=False,
        )
    ], className="selector-tema"),

    #Título de la tabla detalle
    html.Label(
        id='details-datatable',
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
            'marginTop': 80,
            'zIndex': 15,
            'position': 'relative'
        }
    ),

    #Tabla detalle en la que se muestrar los tweets generados por cada uno de los temas
    html.Div( [
        dash_table.DataTable(
            id='datatable-detalle-tema',

            #Columnas de la tabla (en este caso eliminamos ciertos campos del csv original)
            columns= [{'name': i, 'id': i, 'deletable': False} for i in ['Id', 'Hashtag', 'Usuario', 'Fecha', 'Tweet', 'Retweets', 'Likes'] if (i != 'Id' and i != 'Hashtag' and i != 'Usuario')],
            fixed_rows={ 'headers': True, 'data': 0 }, #Permite dejar la cabecera fija durante el scroll

            #Estilo de la tabla
            style_table={
                'maxHeight': '481px',
                'overflowY': 'scroll'
            },

            #Estilo de cada una de las celdas
            style_cell={
                'maxWidth': 0,
                'textAlign': 'left',
            },

            #Estilos condicionales en función de cada una de las celdas
            style_cell_conditional=[
                {'if': {'column_id': 'Fecha'},
                 'width': '15%',
                 'paddingLeft':'10px',
                 'paddingRight':'10px'},
                {'if': {'column_id': 'Tweet'},
                  'textOverflow': 'ellipsis',
                  'paddingLeft':'5px',
                  'paddingRight':'5px'},
                {'if': {'column_id': 'Retweets'},
                  'width': '9.5%',
                  'textAlign': 'center'},
                {'if': {'column_id': 'Likes'},
                  'width': '9.5%',
                  'textAlign': 'center'},
            ],

            #Estilo de la cabecera
            style_header={
                'color': 'white',
                'backgroundColor': '#338A3B',
                'textAlign': 'center',
            },

            #Estilo condicional para los datos (Es lo que nos permite que las filas tengan diferente color)
            style_data_conditional=[{
                'if': {'row_index': 'odd'},
                'backgroundColor': '#EEFFF9',
                'indent':20
                }
            ],
        ),
    ],  className="tabla-tema",
        style={
            'borderStyle': 'solid',
            'borderColor': '#1822dc',
            'borderWidth': 1,
            'paddingTop': 50,
            'paddingLeft': 25,
            'paddingRight': 25,
            'paddingBottom': 50,
            'zIndex': 0,
            'position': 'relative'
       }),

    #Títulos de la parte inferior de la pestaña
    html.Div([
        html.Label(
            'Dedicación del programa',
            className='titulos-graficos-izquierda',
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
            className='titulos-graficos-derecha',
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

    #Gráfico de sectores en el que se representa el porcentaje con respecto al total que dura el tema seleccionado
    html.Div([
        html.Div(id='duracion'),

        html.Div( #Gráfico que muestra la distribución de los colaboradores en función del programa seleccionado
            dcc.Graph(
                id='details-hashtag-colaborador',
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
    ],  className="detalle-inferior",
        style={
            'columnCount': 2,
            'marginTop': -16,
            'zIndex': 0,
            'position': 'relative',
        }),

], style={ #Estilo de la página
    'borderStyle': 'solid',
    'borderColor': '#CCCCCC',
    'borderWidth': 5,
    'paddingBottom':50
})
