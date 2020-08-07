# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

#************************************#
#  Cabecera basica de la aplicación  #
#************************************#

basic_header_error = html.Div(children=[
    #Logo
    html.A([
        html.Img(
            src='/assets/logo.png',
            className="logo"
        )
    ], href='http://127.0.0.1:8050/home/'),

    #Logout
    html.A([
            html.Img(
                src='/assets/cerrarSesion.png', #Icono diseñado por those-icons encontrado en la web https://www.flaticon.es/
                className="logout")
    ], href='http://127.0.0.1:8050/logout/'),

    #Título
    html.Div(
        children='Análisis de la respuesta en twitter de La Sexta Noche',
        className="title",
        style={
            'fontFamily': 'Gill Sans',
            'textIndent': 15,
            'textAlign': 'justify',
            'lineHeight': 2.2,
            'color': 'white',
            'background': '#1822dc',
            'fontWeight': 'lighter',
            'fontVariant': 'small-caps',
            'fontSize':25,
            'marginTop': 15,
        }
    ),

    #Barra de navegación
    html.Div([
        dcc.Link('Principal', href='http://127.0.0.1:8050/principal/arousal/', className="navbar"),
        dcc.Link('Detalle hashtag', href='http://127.0.0.1:8050/detalle_hashtag/', className="navbar"),
        dcc.Link('Detalle colaborador', href='http://127.0.0.1:8050/detalle_colaborador/', className="navbar")
    ], className="diseño-navbar"),
])
