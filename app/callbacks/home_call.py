# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output, State

from app import app
import functions as fc

#************************************************************************#
#  Llamadas necesarias para la actualización del panel de administración #
#************************************************************************#
ruta_input = ''
#Selección de la ubicación de los archivos
@app.callback(
    Output("output", "children"),
    [Input("input_folder", "value")],
)
def update_output(input):
    return input
