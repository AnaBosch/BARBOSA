# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html


#*****************************#
#  Cabecera de la aplicación  #
#*****************************#

basic_header = html.Div(children=[
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

    dcc.Input(id="input_folder", className='folder', persistence='True', debounce=True, type="search", placeholder="introduzca la ubicación de los archivos",
        style={
            'fontFamily': '"Courier New", Courier, monospace',
            'fontSize': 14.5
        }),
    html.Div(id="output",
        style={
            'display': 'none',
        }),
])
