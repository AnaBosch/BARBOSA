# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

import layouts.headers.basic_header as hd

#*************************#
#  Diseño modular de Home #
#*************************#

home_layout = html.Div(children=[

    hd.basic_header,

    html.Div(children=[
        html.Div([
            html.A([
                html.Img(
                    src='/assets/principal.png', #Iconos diseñados por xnimrodx encontrado en la web https://www.flaticon.es/
                    className="icon"
                ),
            ], href='http://127.0.0.1:8050/principal/arousal/'),
            dcc.Link('Principal', href='http://127.0.0.1:8050/principal/arousal/', className="menu"),
        ], className="block-icon block-icon-left"),

        html.Div([
            html.A([
                html.Img(
                    src='/assets/detalle-hashtag.png', #Iconos diseñados por Freepik encontrado en la web https://www.flaticon.es/
                    className="icon icon-hashtag"
                ),
            ], href='http://127.0.0.1:8050/detalle_hashtag/'),
            dcc.Link('Detalle hashtag', href='http://127.0.0.1:8050/detalle_hashtag/', className="menu"),
        ], className="block-icon"),

        html.Div([
            html.A([
                html.Img(
                    src='/assets/detalle-colaborador.png', # Iconos diseñados por Vitaly Gorbachev encontrado en la web https://www.flaticon.es/
                    className="icon icon-colaborador"
                ),
            ], className="lnk", href='http://127.0.0.1:8050/detalle_colaborador/'),
            dcc.Link('Detalle colaborador', href='http://127.0.0.1:8050/detalle_colaborador/', className="menu"),
        ], className="block-icon block-icon-right"),


    ], className="iconos")
], style={ #Estilo de la página
    'borderStyle': 'solid',
    'borderColor': '#CCCCCC',
    'borderWidth': 5,
    'paddingBottom':50
})
