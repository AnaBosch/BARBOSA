# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import layouts.headers.header as hd

#**********************************************************#
#  Diseño modular del cuadro de mandos detalle de los tema #
#**********************************************************#

speakers_detail_layout = html.Div([
    #Se añade la cabecera de la aplicacion
    hd.header,

    #Selector de tema en función del programa elegido en el cuadro de mandos principal
    html.Div( [
        dcc.Dropdown(
            id='select-speaker',
            searchable=False,
            clearable=False,
        )
    ], className="selector-tema"),

    #Título de la tabla detalle
    html.Label(
        id='speakers-datatable',
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
            id='datatable-detalle-colaborador',

            #Columnas de la tabla (en este caso eliminamos ciertos campos del csv original)
            columns= [{'name': i, 'id': i, 'deletable': False} for i in ['Code', 'Sentencia', 'Arousal', 'Valencia'] if (i != 'Code')],
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
                {'if': {'column_id': 'Arousal'},
                 'width': '15.5%',
                 'textAlign': 'center'},
                 {'if': {'column_id': 'Valencia'},
                  'width': '15.5%',
                  'textOverflow': 'ellipsis',
                  'textAlign': 'center'},
                {'if': {'column_id': 'Sentencia'},
                  'textOverflow': 'ellipsis',
                  'paddingLeft':'5px',
                  'paddingRight':'5px'},
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

], style={ #Estilo de la página
    'borderStyle': 'solid',
    'borderColor': '#CCCCCC',
    'borderWidth': 5,
    'paddingBottom':50
})
