# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

import layouts.headers.basic_header as hd
from variables import programa

#*****************************#
#  Cabecera de la aplicación  #
#*****************************#

header = html.Div(children=[
    #Se añade la cabecera basica de la aplicacion
    hd.basic_header,

    #Barra de navegación
    html.Div([
        dcc.Link('Principal', href='http://127.0.0.1:8050/principal/arousal/', className="navbar"),
        dcc.Link('Detalle hashtag', href='http://127.0.0.1:8050/detalle_hashtag/', className="navbar"),
        dcc.Link('Detalle colaborador', href='http://127.0.0.1:8050/detalle_colaborador/', className="navbar")
    ], className="diseño-navbar"),

    html.Br(),
    html.Br(),
    #Selector de programa
    html.Div( [
        dcc.Dropdown(
            id='programas',
            options=[{'label': i, 'value': i} for i in programa],
            value='24/10/2015',
            searchable=False,
            clearable=False,
            persistence=True
        )
    ], className="selector-fecha"),

])
