# -*- coding: utf-8 -*-
from datetime import datetime, time
import pandas as pd
import ast

from variables import duracion_L6N, inicio_L6N

#****************************************************************************************************#
#  Funciones necesarias para la extracción, transformación, carga y representación de la información #
#****************************************************************************************************#

#Función para seleccionar el archivo en el que se encuentran los temas del programa seleccionado
def switch_tema(fecha, ruta):
    if(fecha == '24/10/2015'):
        arch_prog_tema = pd.read_csv(ruta + '/Hashtags/hashtags_L6N_2015_10_24')
    elif(fecha == '14/11/2015'):
        arch_prog_tema = pd.read_csv(ruta + '/Hashtags/hashtags_L6N_2015_11_14')
    elif(fecha == '21/11/2015'):
        arch_prog_tema = pd.read_csv(ruta + '/Hashtags/hashtags_L6N_2015_11_21')
    elif(fecha == '19/12/2015'):
        arch_prog_tema = pd.read_csv(ruta + '/Hashtags/hashtags_L6N_2015_12_19')
    elif(fecha == '26/12/2015'):
        arch_prog_tema = pd.read_csv(ruta + '/Hashtags/hashtags_L6N_2015_12_26')
    elif(fecha == '02/01/2016'):
        arch_prog_tema = pd.read_csv(ruta + '/Hashtags/hashtags_L6N_2016_01_02')
    elif(fecha == '09/01/2016'):
        arch_prog_tema = pd.read_csv(ruta + '/Hashtags/hashtags_L6N_2016_01_09')
    elif(fecha == '16/01/2016'):
        arch_prog_tema = pd.read_csv(ruta + '/Hashtags/hashtags_L6N_2016_01_16')
    elif(fecha == '23/01/2016'):
        arch_prog_tema = pd.read_csv(ruta + '/Hashtags/hashtags_L6N_2016_01_23')

    return arch_prog_tema

#Función para seleccionar el archivo con la información referente a los tweets del programa seleccionado
def switch_tweets(fecha, ruta):

    if(fecha == '24/10/2015'):
        arch_prog_tweets = pd.read_csv(ruta + '/Tweets/L6N-20151024.txt', sep='{')
    elif(fecha == '14/11/2015'):
        arch_prog_tweets = pd.read_csv(ruta + '/Tweets/L6N-20151114.txt', sep='{')
    elif(fecha == '21/11/2015'):
        arch_prog_tweets = pd.read_csv(ruta + '/Tweets/L6N-20151121.txt', sep='{')
    elif(fecha == '19/12/2015'):
        arch_prog_tweets = pd.read_csv(ruta + '/Tweets/L6N-20151219.txt', sep='{')
    elif(fecha == '26/12/2015'):
        arch_prog_tweets = pd.read_csv(ruta + '/Tweets/L6N-20151226.txt', sep='{')
    elif(fecha == '02/01/2016'):
        arch_prog_tweets = pd.read_csv(ruta + '/Tweets/L6N-20160102.txt', sep='{')
    elif(fecha == '09/01/2016'):
        arch_prog_tweets = pd.read_csv(ruta + '/Tweets/L6N-20160109.txt', sep='{')
    elif(fecha == '16/01/2016'):
        arch_prog_tweets = pd.read_csv(ruta + '/Tweets/L6N-20160116.txt', sep='{')
    elif(fecha == '23/01/2016'):
        arch_prog_tweets = pd.read_csv(ruta + '/Tweets/L6N-20160123.txt', sep='{')

    return arch_prog_tweets

#Función para seleccionar el archivo con la información referente al contenido detallado del programa seleccionado
def switch_tweets_likes(fecha, ruta):

    if(fecha == '24/10/2015'):
        arch_prog_tweets_likes = pd.read_csv(ruta + '/Tweets_with_likes/L6N-20151024.txt')
    elif(fecha == '14/11/2015'):
        arch_prog_tweets_likes = pd.read_csv(ruta + '/Tweets_with_likes/L6N-20151114.txt')
    elif(fecha == '21/11/2015'):
        arch_prog_tweets_likes = pd.read_csv(ruta + '/Tweets_with_likes/L6N-20151121.txt')
    elif(fecha == '19/12/2015'):
        arch_prog_tweets_likes = pd.read_csv(ruta + '/Tweets_with_likes/L6N-20151219.txt')
    elif(fecha == '26/12/2015'):
        arch_prog_tweets_likes = pd.read_csv(ruta + '/Tweets_with_likes/L6N-20151226.txt')
    elif(fecha == '02/01/2016'):
        arch_prog_tweets_likes = pd.read_csv(ruta + '/Tweets_with_likes/L6N-20160102.txt')
    elif(fecha == '09/01/2016'):
        arch_prog_tweets_likes = pd.read_csv(ruta + '/Tweets_with_likes/L6N-20160109.txt')
    elif(fecha == '16/01/2016'):
        arch_prog_tweets_likes = pd.read_csv(ruta + '/Tweets_with_likes/L6N-20160116.txt')
    elif(fecha == '23/01/2016'):
        arch_prog_tweets_likes = pd.read_csv(ruta + '/Tweets_with_likes/L6N-20160123.txt')

    return arch_prog_tweets_likes

#Función para seleccionar el archivo en el que se encuentran los tertulianos del programa seleccionado
def switch_tertulianos(fecha, ruta):
    if(fecha == '24/10/2015'):
        arch_prog_tertulianos = pd.read_csv(ruta + '/Tertulianos/tertulianos_L6N_2015_10_24')
    elif(fecha == '14/11/2015'):
        arch_prog_tertulianos = pd.read_csv(ruta + '/Tertulianos/tertulianos_L6N_2015_11_14')
    elif(fecha == '21/11/2015'):
        arch_prog_tertulianos = pd.read_csv(ruta + '/Tertulianos/tertulianos_L6N_2015_11_21')
    elif(fecha == '19/12/2015'):
        arch_prog_tertulianos = pd.read_csv(ruta + '/Tertulianos/tertulianos_L6N_2015_12_19')
    elif(fecha == '26/12/2015'):
        arch_prog_tertulianos = pd.read_csv(ruta + '/Tertulianos/tertulianos_L6N_2015_12_26')
    elif(fecha == '02/01/2016'):
        arch_prog_tertulianos = pd.read_csv(ruta + '/Tertulianos/tertulianos_L6N_2016_01_02')
    elif(fecha == '09/01/2016'):
        arch_prog_tertulianos = pd.read_csv(ruta + '/Tertulianos/tertulianos_L6N_2016_01_09')
    elif(fecha == '16/01/2016'):
        arch_prog_tertulianos = pd.read_csv(ruta + '/Tertulianos/tertulianos_L6N_2016_01_16')
    elif(fecha == '23/01/2016'):
        arch_prog_tertulianos = pd.read_csv(ruta + '/Tertulianos/tertulianos_L6N_2016_01_23')

    return arch_prog_tertulianos

#Función para seleccionar el archivo en el que se encuentran las emociones causadas por el programa seleccionado
def switch_emociones(fecha, ruta):
    if(fecha == '24/10/2015'):
        arch_prog_emociones = pd.read_csv(ruta + '/Emociones/stream_54_2015_m10_d24_212521_La6_annotaciones.txt', sep=';')
    elif(fecha == '14/11/2015'):
        arch_prog_emociones = pd.read_csv(ruta + '/Emociones/stream_54_2015_m11_d14_212021_La6_annotaciones.txt', sep=';')
    elif(fecha == '21/11/2015'):
        arch_prog_emociones = pd.read_csv(ruta + '/Emociones/stream_54_2015_m11_d21_212021_La6_annotaciones.txt', sep=';')
    elif(fecha == '19/12/2015'):
        arch_prog_emociones = pd.read_csv(ruta + '/Emociones/stream_54_2015_m12_d19_212021_La6_annotaciones.txt', sep=';')
    elif(fecha == '26/12/2015'):
        arch_prog_emociones = pd.read_csv(ruta + '/Emociones/stream_54_2015_m12_d26_212021_La6_annotaciones.txt', sep=';')
    elif(fecha == '02/01/2016'):
        arch_prog_emociones = pd.read_csv(ruta + '/Emociones/stream_54_2016_m01_d02_212021_La6_annotaciones.txt', sep=';')
    elif(fecha == '09/01/2016'):
        arch_prog_emociones = pd.read_csv(ruta + '/Emociones/stream_54_2016_m01_d09_212021_La6_annotaciones.txt', sep=';')
    elif(fecha == '16/01/2016'):
        arch_prog_emociones = pd.read_csv(ruta + '/Emociones/stream_54_2016_m01_d16_212021_La6_annotaciones.txt', sep=';')
    elif(fecha == '23/01/2016'):
        arch_prog_emociones = pd.read_csv(ruta + '/Emociones/stream_54_2016_m01_d23_212021_La6_annotaciones.txt', sep=';')

    return arch_prog_emociones

#Función para seleccionar el archivo en el que se encuentra la transcripción del programa seleccionado
def switch_transcripcion(fecha, ruta):
    if(fecha == '24/10/2015'):
        arch_prog_transcripcion = pd.read_csv(ruta + '/Transcripcion/stream_54_2015_m10_d24_212521_La6.txt', sep='{', encoding = "ISO-8859-1")
    elif(fecha == '14/11/2015'):
        arch_prog_transcripcion = pd.read_csv(ruta + '/Transcripcion/stream_54_2015_m11_d14_212021_La6.txt', sep='{', encoding = "ISO-8859-1")
    elif(fecha == '21/11/2015'):
        arch_prog_transcripcion = pd.read_csv(ruta + '/Transcripcion/stream_54_2015_m11_d21_212021_ La6.txt', sep='{', encoding = "ISO-8859-1")
    elif(fecha == '19/12/2015'):
        arch_prog_transcripcion = pd.read_csv(ruta + '/Transcripcion/stream_54_2015_m12_d19_212021_La6.txt', sep='{', encoding = "ISO-8859-1")
    elif(fecha == '26/12/2015'):
        arch_prog_transcripcion = pd.read_csv(ruta + '/Transcripcion/stream_54_2015_m12_d26_212021_La6.txt', sep='{', encoding = "ISO-8859-1")
    elif(fecha == '02/01/2016'):
        arch_prog_transcripcion = pd.read_csv(ruta + '/Transcripcion/stream_54_2016_m01_d02_212021_La6.txt', sep='{', encoding = "ISO-8859-1")
    elif(fecha == '09/01/2016'):
        arch_prog_transcripcion = pd.read_csv(ruta + '/Transcripcion/stream_54_2016_m01_d09_212021_La6.txt', sep='{', encoding = "ISO-8859-1")
    elif(fecha == '16/01/2016'):
        arch_prog_transcripcion = pd.read_csv(ruta + '/Transcripcion/stream_54_2016_m01_d16_212021_La6.txt', sep='{', encoding = "ISO-8859-1")
    elif(fecha == '23/01/2016'):
        arch_prog_transcripcion = pd.read_csv(ruta + '/Transcripcion/stream_54_2016_m01_d23_212021_La6.txt', sep='{', encoding = "ISO-8859-1")

    return arch_prog_transcripcion

#Función para establecer el formato datetime a una lista
def obtener_datetime(lista, programa_name):
    formato = []

    for i in lista:  #Bucle que establece el formato datetime
        formato.append(datetime.strptime(programa_name+' '+i, "%d/%m/%Y %H:%M:%S"))

    return formato

#Función para conocer que speaker hablan en un tiempo concreto
def speaker(transcripcion):
    dic_transcripcion = dict()
    #Se recorre el archivo de transcripcion creando un diccionario cuya clave es la hora y los valores los participantes
    for i in range(len(transcripcion['Hora'])):
        speaker_list = []
        bloque = transcripcion['Informacion'][i].split()

        #Añadimos a la lista de speakers solo las palabras que contienen #
        for palabra in bloque:
            if any(s in palabra for s in ('#')):
                speaker_list.append(palabra)

        #Se añade esa clave y esa lista de valores al diccionario
        dic_transcripcion[transcripcion['Hora'][i]] = speaker_list

    return dic_transcripcion

#Función que filtra la emoción
def emotion_filter(emociones, tipo):
    emotion_list = []
    wanted_emotion = []

    #Se recorren las emociones
    for i in emociones:
        dict_emocion = ast.literal_eval(i)    #Se transforma en dict el string

        #Se recorren las diferentes listas de emocion para la misma hora
        for j in dict_emocion:
            emotion_list.append(j.get(tipo))  #Se obtiene la emoción que buscamos

        wanted_emotion.append(emotion_list)   #Para cada hora se obtiene una lista con la emocion buscada
        emotion_list = []

    return wanted_emotion

#Función para conocer las emociones de cada speaker
def speaker_emotion(speakers_time, speakers, emotion_time, emotions, programa_name):
    inicio_L6N_format = datetime.strptime(programa_name+' '+inicio_L6N, "%d/%m/%Y %H:%M:%S")  #Se transforma a datetime
    dic_emotion = dict()

    #Se recorren las horas de las que tenemos la información de la emoción
    for i in range(len(emotion_time)):
        personas = set()

        #Se recorren las horas de las que tenemos información de los speakers que intervienen
        for j in range(len(speakers_time)):
            #En el caso de evaluar la primera hora en la que tenemos emoción se usa el valor del comienzo del programa
            if(i == 0):
                if (speakers_time[j] < emotion_time[i]) and (speakers_time[j] >= inicio_L6N_format):
                    #Se añaden las personas que han intervenido en el intervalo que genera dicha emoción
                    for persona in speakers[j]:
                        personas.add(persona)
            #Para el resto
            else:
                if (speakers_time[j] < emotion_time[i]) and (speakers_time[j] >= emotion_time[i-1]):
                    #Se añaden las personas que han intervenido en el intervalo que genera dicha emoción
                    for persona in speakers[j]:
                        personas.add(persona)

        #A cada persona que ha intervenido en ese periodo se le añaden las emociones observadas
        for persona in personas:
            #Si la key ya esta en el dict, se añaden las nuevas emociones
            if persona in dic_emotion:
                dic_emotion[persona] += emotions[i]
            #Si no lo esta, se crea la key y se añaden las emociones
            else:
                dic_emotion[persona] = emotions[i]

    return dic_emotion

#Función para eliminar los speakers que no son tertulianos
def delete_speakers(emocion, tertulianos):
    for i in list(emocion):
        #Si no pertenece a la lista de tertulianos se elimina
        if i not in list(tertulianos):
            del emocion[i]

    return emocion

#Función para contabilizar los valores de la emoción
def count_emotion(emocion):
    return_dict = dict()

    for i in emocion:
        count_dict = dict()
        #Se contabiliza cada emoción
        for j in emocion[i]:
            if j in count_dict:
                count_dict[j]+=1
            else:
                count_dict[j]=1

        #Se añade a cada tertuliano
        return_dict[i] = count_dict

    return return_dict

#Función que calcula el total de emociones de cada tertuliano
def calcular_total(emocion):
    sum_dict = dict()

    for i in emocion:
        for j in emocion[i]:
            if i in sum_dict:
                sum_dict[i] += emocion[i][j]
            else:
                sum_dict[i] = emocion[i][j]

    return sum_dict

#Función para calcular el porcentaje
def calcular_porcentaje(valor, total):
    return valor * 100 / total

#Función para conocer los porcentajes de los valores de emoción
def emotion_percent(emocion, total):
    percent_dict = dict()

    for i in emocion:
        aux_dict = dict()
        #Se calcula el porcentaje de cada emoción
        for j in emocion[i]:
            aux_dict[j] = calcular_porcentaje(emocion[i][j], total[i])

        percent_dict[i] = aux_dict

    return percent_dict

#Función para obtener el tertuliano en función de su número
def obtener_tertuliano(emocion, arch_tertulianos):
    x = []

    for i in emocion:
        for j in range(len(arch_tertulianos['Numero'])):
            if i == arch_tertulianos['Numero'][j]:
                x.append(arch_tertulianos['Tertuliano'][j])

    return x

#Función para convertir la hora dado como un string en segundos
def segundos(duracion):
    return sum(x * int(t) for x, t in zip([3600, 60, 1], duracion.split(":")))

#Función que elimina los temas de los cuales no se han recopilado datos de emoción
def eliminar_temas_sin_datos(pair):
    aux = []
    for i in range(len(pair)):
        if pair[i][1] == 'No hay datos registrados':
            aux.append(i)

    pair = [j for i, j in enumerate(pair) if i not in aux]

    return pair

#Función para conocer que speaker hablan en un tiempo concreto
def sentences(transcripcion):
    dic_transcripcion = dict()

    #Se recorre la diarización del programa
    for i in range(len(transcripcion['Hora'])):
        str = transcripcion['Informacion'][i]  #Se obtienen las intervenciones de esa hora

        #Se establecen los iteradores para reestablecer el conjunto de intervenciones y movernos por el contenido del archivo
        inicio = str.find("(")
        inicio_numero = str.find("(")
        fin = 0
        str = str[inicio+1:]

        diccionario = dict()

        #Mientras el conjunto de intervenciones de esa hora no se haya terminado
        while fin != -1:
            #Se reestablecen los iteradores
            inicio = str.find(")")
            fin = str.find("(")

            #Se obtienen cada intervención
            frase = str[inicio+1:fin]
            #Se obtiene el colaborador de la intervención
            numero = str[inicio_numero:inicio+1]

            #Se reestablece el conjunto de intervenciones
            str = str[fin+1:]

            #Si la key ya esta en el dict, se añade la nueva frase
            if numero in diccionario:
                diccionario[numero].append(frase)
            #Si no lo esta, se crea la key y se añade la frase
            else:
                diccionario[numero] = [frase]

        dic_transcripcion[transcripcion['Hora'][i]] = diccionario

    return dic_transcripcion

#Función para encontrar el elemento mas repetido de una lista. Código de la función completamente extraído de: geeksforgeeks.org, https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i

    return num

#Función para encontrar el código correspondiente a un tertuliano
def find_code(query, archivo):
    code = ''

    for i in range(len(archivo['Tertuliano'])):
        if archivo['Tertuliano'][i] == query:
            code = archivo['Numero'][i]

    return code

#Función para conocer las emociones de cada speaker
def sentence_emotion(sentence_time, sentence, emotion_time, arousal_emotions, valencia_emotions, programa_name):
    inicio_L6N_format = datetime.strptime(programa_name+' '+inicio_L6N, "%d/%m/%Y %H:%M:%S")  #Se transforma a datetime
    dic_emotion = dict()

    #Se recorren las horas de las que tenemos la información de la emoción
    for i in range(len(emotion_time)):
        arousal_emotion_index = most_frequent(arousal_emotions[i])
        valencia_emotion_index = most_frequent(valencia_emotions[i])

        #Se recorren las horas de las que tenemos información de los sentence que intervienen
        for j in range(len(sentence_time)):
            #En el caso de evaluar la primera hora en la que tenemos emoción se usa el valor del comienzo del programa
            if(i == 0):
                if (sentence_time[j] < emotion_time[i]) and (sentence_time[j] >= inicio_L6N_format):
                    #Se añaden las personas que han intervenido en el intervalo que genera dicha emoción
                    for n in list(sentence[j].keys()):
                        pair = []

                        for m in sentence[j][n]:
                            pair.append((m,arousal_emotion_index, valencia_emotion_index))
                            sentence[j][n].remove(m)

                        pos = '(' + n

                        if pos in dic_emotion:
                            dic_emotion[pos] += pair
                        #Si no lo esta, se crea la key y se añaden las emociones
                        else:
                            dic_emotion[pos] = pair

            #Para el resto
            else:
                if (sentence_time[j] < emotion_time[i]) and (sentence_time[j] >= emotion_time[i-1]):
                    #Se añaden las personas que han intervenido en el intervalo que genera dicha emoción
                    for n in list(sentence[j].keys()):
                        pair = []

                        for m in sentence[j][n]:
                            pair.append((m,arousal_emotion_index, valencia_emotion_index))
                            sentence[j][n].remove(m)

                        pos = '(' + n

                        if pos in dic_emotion:
                            dic_emotion[pos] += pair
                        #Si no lo esta, se crea la key y se añaden las emociones
                        else:
                            dic_emotion[pos] = pair

    return dic_emotion
