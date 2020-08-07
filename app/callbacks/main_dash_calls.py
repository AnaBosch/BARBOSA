# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output, State
from datetime import datetime, time
import operator
from plotly.graph_objs import Box
import plotly.graph_objects as go

from app import app
from variables import colors
import functions as fc

#*****************************************************************************************************#
#  Llamadas necesarias para la actualización de cuadro de mandos principal en función de sus entradas #
#*****************************************************************************************************#

#Actualización del gráfico de la distribución por tema
@app.callback(
    Output('graphic-distribucion-temas', 'figure'),
    [Input('programas', 'value'), Input('output', 'children')],
    [State('programas', 'value')])
def update_graph(programa_name, output, pn):
    #Valores del eje de abscisas
    arch_tema = fc.switch_tema(programa_name, output)  #Se selecciona el archivo correspondiente al programa
    x_tema = [i for i in arch_tema['Hashtag']]  #Se obtienen los hashtag del archivo

    #Valores del eje de ordenadas
    arch_tweets = fc.switch_tweets(programa_name, output)  #Se selecciona el archivo correspondiente al programa
    tweets_tema = [i for i in arch_tweets['Hashtag']]  #Se obtienen los hashtag del archivo
    y_tema = [x for x in tweets_tema if str(x) != 'nan']  #Se eliminan de la selección anterior los valores nulos
    y_tweets_tema = []  #Lista del eje de ordenadas

    for i in x_tema: #Se calcula el número de tweets correspondiente a cada tema y se añade a la lista que representa el eje de ordenadas
        y_tweets_tema.append(y_tema.count(i))

    #Generamos un pair con ambas listas
    pair =  [[x, y] for x, y in zip(x_tema, y_tweets_tema)]

    #Se ordenan los elementos en función del segundo parametro del pair
    pair.sort(key=operator.itemgetter(1))
    pair.reverse()  #Se invierte el orden para que sea de mayor a menor

    #Se actualizan las listas que se muestran
    x_tema = []
    y_tweets_tema = []

    for a,b in pair:
        x_tema.append(a)
        y_tweets_tema.append(b)

    return {
        #Datos y estilo del gráfico
        'data': [dict(
            x = x_tema,
            y = y_tweets_tema,
            type ='bar',
            text= 'tweets',
            marker = dict(
                color= colors
            ),
            hovertemplate = '%{y} tweets <extra></extra>'
        )],
        'layout': dict(
            margin= dict(l=70, r=95, t=67, b=90),
            yaxis = dict(title = "Tweets", titlefont= dict(size= 16)),
        )
    }

#Actualización del gráfico de la distribución por colaborador
@app.callback(
    Output('graphic-distribucion-colaborador', 'figure'),
    [Input('programas', 'value'), Input('output', 'children')])
def update_graph(programa_name, output):
    #Valores del eje de abscisas
    arch_tertulianos = fc.switch_tertulianos(programa_name, output)  #Se selecciona el archivo correspondiente al programa
    tertulianos = [i for i in arch_tertulianos['Usuario']]  #Se obtienen los tertulianos del archivo
    x_tertulianos = [x for x in tertulianos if str(x) != 'nan']  #Se eliminan de la selección anterior los valores nulos

    #Valores del eje de ordenadas
    arch_tweets = fc.switch_tweets(programa_name, output)  #Se selecciona el archivo correspondiente al programa
    tweets_fracc = []  #Lista para almacenar todas las palabras de los tweets
    y_tweets_tertuliano = []  #Lista del eje de ordenadas

    for i in arch_tweets['Tweet']:  #Se obtienen las palabras de todos los tweets
        tweets_fracc += i.split()

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

#Actualización del gráfico que muestra el arousal de cada colaborador
@app.callback(
    Output('graphic-arousal', 'figure'),
    [Input('programas', 'value'), Input('output', 'children')])
def update_graph(programa_name, output):
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

    ##Obtención de los speakers del programa:
    #1. Se extrae los speakers
    speakers = fc.speaker(arch_transcripcion)

    #2. Se filtran las emociones
    arousal = fc.emotion_filter(arch_emociones['Emociones'], 'arousal')

    #3. Se añaden las emociones a cada speaker
    emotions_arousal = fc.speaker_emotion(horas_format, list(speakers.values()), inicio_datetime, arousal, programa_name)

    #4. Se eliminan los speakers que no son tertulianos
    arch_tertulianos = fc.switch_tertulianos(programa_name, output)
    arousal_tertulianos = fc.delete_speakers(emotions_arousal, arch_tertulianos['Numero'])

    ##Obtención del porcentaje de emociones de los tertulianos
    #1. Se contabiliza cada valor
    count_arousal = fc.count_emotion(arousal_tertulianos)

    #2. Se calcula el porcentaje de cada valor
    total_arousal = fc.calcular_total(count_arousal)
    percent_arousal = fc.emotion_percent(count_arousal, total_arousal)

    ##Se crea el diseño del gráfico
    #1. Se obtiene la serie x
    x = fc.obtener_tertuliano(percent_arousal, arch_tertulianos)

    #2. Se obtienen las series de y
    y1 = []
    y2 = []
    y3 = []

    #Para que el gráfico identifique bien los valores es necesario remarcar los valores ausentes de cada categoria
    for i in percent_arousal:
        l = list(percent_arousal[i].keys())

        if 'Alterado' not in l:
            percent_arousal[i]['Alterado'] = 0
        if 'Ligeramente alterado' not in l:
            percent_arousal[i]['Ligeramente alterado'] = 0
        if 'Neutro' not in l:
            percent_arousal[i]['Neutro'] = 0

    #Se incorporan los valores a las diferentes trazas
    for i in percent_arousal:
        for j in percent_arousal[i]:
            if j == 'Alterado':
                y1.append(percent_arousal[i][j])
            elif j == 'Ligeramente alterado':
                y2.append(percent_arousal[i][j])
            elif j == 'Neutro':
                y3.append(percent_arousal[i][j])

    #3. Se establecen los datos
    data=[
        go.Bar(
            name='Alterado',
            x=y1,
            y=x,
            orientation = 'h',
            marker = dict(
                color= 'rgb(33,56,33,22)'
            ),
            hovertemplate = '%{x:.2f}%'
        ),
        go.Bar(
            name='Ligeramente alterado',
            x=y2,
            y=x,
            orientation = 'h',
            marker = dict(
                color= 'rgb(53,140,59,55)'
            ),
            hovertemplate = '%{x:.2f}%'
        ),
        go.Bar(
            name='Neutro',
            x=y3,
            y=x,
            orientation = 'h',
            marker = dict(
                color= 'rgb(231,237,216,93)'
            ),
            hovertemplate = '%{x:.2f}%'
        )
    ]

    return {
            'data': data,
            'layout': go.Layout(
                barmode='stack',
                margin= dict(l=160, r=20, t=75, b=65),
                xaxis= dict(
                    ticksuffix= '%',
                    showgrid=False,
                    zeroline=False,
                    domain=[0.03, 1]
                ),
                yaxis= dict(
                    linecolor = 'white' ,
                    linewidth = 3,
                ),
            )
        }

#Actualización del gráfico que muestra la valencia de cada colaborador
@app.callback(
    Output('graphic-valence', 'figure'),
    [Input('programas', 'value'), Input('output', 'children')])
def update_graph(programa_name, output):
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

    ##Obtención de los speakers del programa:
    #1. Se extrae los speakers
    speakers = fc.speaker(arch_transcripcion)

    #2. Se filtran las emociones
    valence = fc.emotion_filter(arch_emociones['Emociones'], 'valence')

    #3. Se añaden las emociones a cada speaker
    emotions_valence = fc.speaker_emotion(horas_format, list(speakers.values()), inicio_datetime, valence, programa_name)

    #4. Se eliminan los speakers que no son tertulianos
    arch_tertulianos = fc.switch_tertulianos(programa_name, output)
    valence_tertulianos = fc.delete_speakers(emotions_valence, arch_tertulianos['Numero'])

    ##Obtención del porcentaje de emociones de los tertulianos
    #1. Se contabiliza cada valor
    count_valence = fc.count_emotion(valence_tertulianos)

    #2. Se calcula el porcentaje de cada valor
    total_valence = fc.calcular_total(count_valence)
    percent_valence = fc.emotion_percent(count_valence, total_valence)

    ##Se crea el diseño del gráfico
    #1. Se obtiene la serie x
    x = fc.obtener_tertuliano(count_valence, arch_tertulianos)

    #2. Se obtienen las series de y
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []

    #Para que el gráfico identifique bien los valores es necesario remarcar los valores ausentes de cada categoria
    for i in percent_valence:
        l = list(percent_valence[i].keys())

        if 'Negativo (desagradable / no colabora nada)' not in l:
            percent_valence[i]['Negativo (desagradable / no colabora nada)'] = 0
        if 'Ligeramente negativo' not in l:
            percent_valence[i]['Ligeramente negativo'] = 0
        if 'Neutral' not in l:
            percent_valence[i]['Neutral'] = 0
        if 'Ligeramente positivo' not in l:
            percent_valence[i]['Ligeramente positivo'] = 0
        if 'Positivo (agradable / constructivo)' not in l:
            percent_valence[i]['Positivo (agradable / constructivo)'] = 0

    #Se incorporan los valores a las diferentes trazas
    for i in percent_valence:
        for j in percent_valence[i]:
            if j == 'Negativo (desagradable / no colabora nada)':
                y1.append(percent_valence[i][j])
            elif j == 'Ligeramente negativo':
                y2.append(percent_valence[i][j])
            elif j == 'Neutral':
                y3.append(percent_valence[i][j])
            elif j == 'Ligeramente positivo':
                y4.append(percent_valence[i][j])
            elif j == 'Positivo (agradable / constructivo)':
                y5.append(percent_valence[i][j])

    #3. Se establecen los datos
    data=[
        go.Bar(
            name='Negativo',
            x=y1,
            y=x,
            orientation = 'h',
            marker = dict(
                color= 'rgb(33,56,33,22)'
            ),
            hovertemplate = '%{x:.2f}%'

        ),
        go.Bar(
            name='Ligeramente negativo',
            x=y2,
            y=x,
            orientation = 'h',
            marker = dict(
                color= 'rgb(53,140,59,55)'
            ),
            hovertemplate = '%{x:.2f}%'
        ),
        go.Bar(
            name='Neutral',
            x=y3,
            y=x,
            orientation = 'h',
            marker = dict(
                color= 'rgb(231,237,216,93)'

            ),
            hovertemplate = '%{x:.2f}%'
        ),
        go.Bar(
            name='Ligeramente positivo',
            x=y4,
            y=x,
            orientation = 'h',
            marker = dict(
                color= 'rgb(227,255,154,100)'

            ),
            hovertemplate = '%{x:.2f}%'
        ),
        go.Bar(
            name='Positivo',
            x=y5,
            y=x,
            orientation = 'h',
            marker = dict(
                color='rgb(170,255,0,100)'

            ),
            hovertemplate = '%{x:.2f}%'
        )
    ]

    return {
            'data': data,
            'layout': go.Layout(
                barmode='stack',
                margin= dict(l=160, r=20, t=75, b=65),
                xaxis= dict(
                    ticksuffix= '%',
                    showgrid=False,
                    zeroline=False,
                    domain=[0.03, 1]
                ),
                yaxis= dict(
                    linecolor = 'white' ,
                    linewidth = 3 ,
                ),
                hovermode="y"
            )
        }
