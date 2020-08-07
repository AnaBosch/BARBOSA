# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

import layouts.headers.basic_header_error as hd

#***********************************#
#  Diseño modular de page not found #
#***********************************#

page_not_found_layout = html.Div(children=[
    #Se añade la cabecera de la aplicacion
    hd.basic_header_error,

    #Gif de error 404
    html.Img(
        src='/assets/404_error.gif', #Gif de freefrontend visualizado mediante la web Pinterest: https://www.pinterest.es/pin/526921225151735674/
        className="error"            #Modificado mediante la web ezgif: https://ezgif.com
    ),
])
