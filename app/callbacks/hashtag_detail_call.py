# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import operator

from app import app
from variables import duracion_L6N, colors
import functions as fc

#*********************************************************************************************************#
#  Llamadas necesarias para la actualización del cuadro de mandos detalle-tema en función de sus entradas #
#*********************************************************************************************************#

#Devolución de temas en función de un programa concreto
@app.callback(
    Output('select-tema', 'options'),
    [Input('programas', 'value'), Input('output', 'children')])
def set_tema_options(programa_name, output):
    arch_tema = fc.switch_tema(programa_name, output)  #Se selecciona el archivo correspondiente al programa
    return [{'label': i, 'value': i} for i in arch_tema['Hashtag']]  #Se obtienen los hashtag del archivo

#Devolución de un tema concreto entre todas las opciones que tenemos disponibles
@app.callback(
    Output('select-tema', 'value'),
    [Input('select-tema', 'options')])
def set_tema_value(available_options):
    return available_options[0]['value']

#Se obtiene como filtro el valor del selector de tema
@app.callback(
    Output('datatable-detalle-tema', 'filter_query'),
    [Input('select-tema', 'value')])
def write_query(query):
    if query is None:
        return ''
    return query

#Actualización del detalle de tema en función del tema que estemos tratando
@app.callback(
    Output('datatable-detalle-tema', 'data'),
    [Input('datatable-detalle-tema', 'filter_query'), Input('programas', 'value'), Input('output', 'children')])
def update_details_table(query, programa_name, output):
    arch_tweets = fc.switch_tweets_likes(programa_name, output)

    filter = arch_tweets.loc[getattr(arch_tweets['Hashtag'], 'eq')(query)]
    return filter.to_dict('records')

#Actualización de la comparación de duración del tema actual con respecto al resto de temas
@app.callback(
    Output('duracion', 'children'),
    [Input('select-tema', 'value'),Input('programas', 'value'), Input('output', 'children')])
def update_graph(selected, programa_name, output):
    #Variables necesarias para obtener la duración de los temas
    arch_tema = fc.switch_tema(programa_name, output)
    duracion = 0

    #Se transforma a segundos la variable global
    duracion_L6N_seg = fc.segundos(duracion_L6N)

    #Obtenemos la duracion concreta de nuestro tema
    for i in range(len(arch_tema['Hashtag'])):
        if arch_tema['Hashtag'][i]==selected:
            duracion = arch_tema['Duracion'][i]

    duracion_prog = duracion_L6N_seg - duracion
    #Establecemos los valores que va a tener el grafico de sectores
    data = [{
        'values': [duracion, duracion_prog],
        'type': 'pie',
        'labels': ['Duración ' + selected,'Duración Programa'],
        'pull':[0, 0.2],
        'marker': dict(
            colors=['rgb(82,224,61,88)', 'rgb(240,255,188,100)'],
        ),
        'hoverinfo':'skip',
    }]

    #Se devuelve el grafico de sectores que se ha creado con los datos establecidos
    return html.Div([
        dcc.Graph(
            id='graph',
            config={
                'displayModeBar': False
            },
            figure={
                'data': data,
                'layout': {
                    'margin': {'l': 40, 'r': 0, 'b': 30, 't': 80},
                    'legend': {'x': -0.05, 'y': 1.1}
                }
            }
        )
    ],
    style={
            'borderStyle': 'solid',
            'borderColor': '#1822dc',
            'borderWidth': 1,
            'paddingBottom': 10,
            'paddingTop': 11,
    }
)

#Actualización del titulo de la tabla detalle en función del tema que se este dando
@app.callback(
    Output('details-datatable', 'children'),
    [Input('select-tema', 'value'), Input('output', 'children')])
def update_output_label_details_datatable(selected, output):
    return 'Detalle de ' + selected

#Actualización del gráfico de la distribución por colaborador
@app.callback(
    Output('details-hashtag-colaborador', 'figure'),
    [Input('select-tema', 'value'),Input('programas', 'value'), Input('output', 'children')])
def update_graph(selected, programa_name, output):
    #Valores del eje de abscisas
    arch_tertulianos = fc.switch_tertulianos(programa_name, output)  #Se selecciona el archivo correspondiente al programa
    tertulianos = [i for i in arch_tertulianos['Usuario']]  #Se obtienen los tertulianos del archivo
    x_tertulianos = [x for x in tertulianos if str(x) != 'nan']  #Se eliminan de la selección anterior los valores nulos

    #Valores del eje de ordenadas
    arch_tweets = fc.switch_tweets(programa_name, output)  #Se selecciona el archivo correspondiente al programa
    tweets_fracc = []  #Lista para almacenar todas las palabras de los tweets
    y_tweets_tertuliano = []  #Lista del eje de ordenadas

    #Enlazamos los hashtag con las menciones para poder ver la repercusión que tienen los colaboradores por hastag
    pair =  [[x, y] for x, y in zip(arch_tweets['Hashtag'], arch_tweets['Tweet'])]

    for a,b in pair:  #Se obtienen las palabras de todos los tweets del hashtag seleccionado
        if a == selected:
            tweets_fracc += b.split()

    for i in x_tertulianos: #Se calcula el número de tweets correspondiente a cada tertuliano y se añade a la lista que representa el eje de ordenadas
        y_tweets_tertuliano.append(tweets_fracc.count(i))

    #Generamos un pair con ambas listas
    pair =  [[x, y] for x, y in zip(x_tertulianos, y_tweets_tertuliano)]

    #Se ordenan los elementos en función del segundo parametro del pair
    pair.sort(key=operator.itemgetter(1))
    pair.reverse()  #Se invierte el orden para que sea de mayor a menor

    #Se actualizan las listas que se muestran
    x_tertulianos = []
    y_tweets_tertuliano = []

    for a,b in pair:
        x_tertulianos.append(a)
        y_tweets_tertuliano.append(b)

    #Datos y estilo del gráfico
    return {
        'data': [dict(
            x = y_tweets_tertuliano,
            y = x_tertulianos,
            type ='bar',
            text= 'tweets',
            marker = dict(
                color= colors
            ),
            hovertemplate = '%{x} tweets <extra></extra>',
            orientation='h'
        )],
        'layout': dict(
            yaxis=dict(
                    autorange='reversed',
                    linecolor = 'white' ,
                    linewidth = 3 ,
                    ),
            xaxis = dict(title = "Tweets", titlefont= dict(size= 16)),
            margin= dict(l=135, r=20, t=70, b=65)
        )
    }
