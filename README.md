# BARBOSA: Desarrollo de un sistema de análisis y visualización de la respuesta de la audiencia en Twitter a programas de televisión.

**BARBOSA** es un sistema de análisis de negocio que permite a las cadenas de televisión analizar y visualizar de forma automática la respuesta de la audiencia en Twitter, proporcionando un conjunto de reportes que apoyan la toma de decisión.

## Contenido 💾

**BARBOSA** cuenta con una estructura modular compuesta de los siguentes módulos.

- Variables del sistema
- Funciones del sistema
- Diseños Dash
- Funcionalidad Dash
- index.py
- app.py
- Directorio assets

## Pre-requisitos 🗒

Python versión 3.7.3.

Pip versión 20.1.1.

## Instalación 🔧

El uso de **BARBOSA** requiere previamente:

#### Obtener las listas de los paquetes disponibles.
```
sudo apt update
```

#### Instalar el sistema de gestión de paquetes Pip.
```
sudo apt install python3-pip
```

#### Actualizar el sistema de gestión de paquetes Pip.
```
pip3 install --upgrade pip
```

#### Instalar el módulo Dash.
```
pip install dash==1.11.0
```

#### Instalar el módulo Pandas.
```
pip install pandas
```

#### Instalar el módulo Flask-Login
```
pip install flask-login
```

## Iniciar BARBOSA 💻

Para iniciar **BARBOSA** es necesario ubicarse en el directorio `app` y ejecutar el archivo `index.py`.
```
python3 index.py
```
Una vez ejecutado el archivo siga los siguientes pasos:

1. Acceda a la dirección http://127.0.0.1:8050/login/ desde su navegador.
2. Introduzca como nombre de usuario **usuario** y como contraseña **mundo**.
3. Seleccione **./data** como directorio, desde el cual obtener la información. Se proporcionan ficheros mock a partir de los cuales probar BARBOSA.

📢 BARBOSA solo dispone de información de prueba para el programa emitido en la fecha 24/10/2015

## Componentes de BARBOSA 📊

### Cuadro de mando principal

- **Repercusión por hashtag:** Número de tweets que recibe cada hashtag del programa.
- **Repercusión por colaborador:** Número de tweets que recibe cada colaborador del programa.
- **Análisis emocional:** Distribución de los valores de *arousal* y *valence* de los colaboradores del programa.

### Cuadro de mando detalle de hashtag

- **Detalle del hashtag:** Texto, fecha, retweets y likes de los tweets en los que se menciona un determinado hashtag.
- **Dedicación del programa:** Duración de las secciones correspondientes a un hashtag respecto a la duración total del programa.
- **Repercusión por colaborador:** Número de tweets que reciben los colaboradores del programa para un determinado hashtag.

### Cuadro de mando detalle de colaborador
Conjunto de intervenciones y valores de *arousal* y *valence* de un colaborador durante un determinado programa.
