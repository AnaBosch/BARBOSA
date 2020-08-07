# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import operator
from datetime import datetime, time
import pandas as pd

from app import app
from variables import duracion_L6N, colors
import functions as fc

#*********************************************************************************************************#
#  Llamadas necesarias para la actualización del cuadro de mandos detalle-tema en función de sus entradas #
#*********************************************************************************************************#

#Devolución de colaboradores en función de un programa concreto
@app.callback(
    Output('select-speaker', 'options'),
    [Input('programas', 'value'), Input('output', 'children')])
def set_tema_options(programa_name, output):
    arch_colaboradores = fc.switch_tertulianos(programa_name, output)  #Se selecciona el archivo correspondiente al programa
    return [{'label': i, 'value': i} for i in arch_colaboradores['Tertuliano']]  #Se obtienen los colaboradores del archivo

#Devolución de un tema concreto entre todas las opciones que tenemos disponibles
@app.callback(
    Output('select-speaker', 'value'),
    [Input('select-speaker', 'options')])
def set_speaker_value(available_options):
    return available_options[0]['value']

#Se obtiene como filtro el valor del selector de tema
@app.callback(
    Output('datatable-detalle-colaborador', 'filter_query'),
    [Input('select-speaker', 'value')])
def write_query(query):
    if query is None:
        return ''
    return query

#Actualización del detalle de tema en función del tema que estemos tratando
@app.callback(
    Output('datatable-detalle-colaborador', 'data'),
    [Input('datatable-detalle-colaborador', 'filter_query'), Input('programas', 'value'), Input('output', 'children')])
def update_details_table(query, programa_name, output):
    ##Extracción y transformación de las horas iniciales del archivo Emociones:
    #1. Transformación al formato en el que se encuentran la transcripción
    arch_emociones = fc.switch_emociones(programa_name, output) #Se selecciona el archivo correspondiente al programa
    inicio = [i for i in arch_emociones['Inicio']]  #Se obtiene una lista con las horas iniciales
    inicio_format = []  #Lista con las horas iniciales en el formato correcto

    for i in inicio:  #Se trasforma el formato horario de un archivo en el formato del otro archivo
        inicio_format.append(datetime.strptime(i, "%Hh%Mm%S.%fs").strftime('%H:%M:%S'))

    #2. Transformación al formato datetime
    inicio_datetime = fc.obtener_datetime(inicio_format, programa_name)

    ##Extracción y transformación de las horas de la transcripción al formato datetime:
    arch_transcripcion = fc.switch_transcripcion(programa_name, output)  #Se selecciona el archivo correspondiente al programa
    horas_format = fc.obtener_datetime(arch_transcripcion['Hora'], programa_name) #Establece el formato datetime a cada una de las horas del archivo de Hashtag

    ##Obtención de las frases del programa:
    #1. Se extrae las frases
    sentences = fc.sentences(arch_transcripcion)

    #2. Se filtran las emociones
    arousal = fc.emotion_filter(arch_emociones['Emociones'], 'arousal')
    valencia = fc.emotion_filter(arch_emociones['Emociones'], 'valence')

    #3. Se añaden las emociones a cada frase
    sentences_e = fc.sentence_emotion(horas_format, list(sentences.values()), inicio_datetime, arousal, valencia, programa_name)

    #4. Transformar filtro en su codigo
    arch_colaborador = fc.switch_tertulianos(programa_name, output)
    code = fc.find_code(query, arch_colaborador)

    #5. Crear dataframe
    sent = []
    arol = []
    val = []
    col = []

    for i in list(sentences_e.keys()):
        for j in sentences_e[i]:
            sent.append(j[0])
            arol.append(j[1])
            val.append(j[2])
            col.append(i)

    data = {'Code': col, 'Sentencia': sent,'Arousal': arol, 'Valencia':val}
    dataframe = pd.DataFrame(data, columns = ['Code', 'Sentencia', 'Arousal', 'Valencia'])

    #6. Obtener los valores del dataframe
    filter = dataframe.loc[getattr(dataframe['Code'], 'eq')(code)]

    return filter.to_dict('records')

#Actualización del titulo de la tabla detalle en función del colaborador que se este pasando
@app.callback(
    Output('speakers-datatable', 'children'),
    [Input('select-speaker', 'value')])
def update_output_label_details_datatable(selected):
    return 'Detalle de ' + selected
