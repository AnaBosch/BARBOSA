# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import Flask, Response, redirect, url_for, request, session, abort
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
import flask
import crypt
from hmac import compare_digest as compare_hash

from app import app, server, login_manager
from layouts.main_dash_layout import main_layout
from layouts.arousal_layout import arousal_layout
from layouts.valence_layout import valence_layout
from layouts.hashtag_detail_layout import hashtag_detail_layout
from layouts.speakers_detail_layout import speakers_detail_layout
from layouts.page_not_found import page_not_found_layout
from layouts.home import home_layout
from callbacks import main_dash_calls, hashtag_detail_call, speakers_detail_call, home_call

# Código de la clase User se obtuvó del usuario numpynewb desde la página web: https://github.com/plotly/dash/issues/214
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = str(id)
        self.password = crypt.crypt('mundo')

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)

user = User("usuario")

#Código de la función login se obtuvó y modifico del usuario numpynewb desde la página web: https://github.com/plotly/dash/issues/214
@server.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if compare_hash(user.password, crypt.crypt(password, user.password)) and user.name == username:
            login_user(user)
            return flask.redirect('/home/')
        else:
            return abort(401)
    else:
        return Response(
        '''
        <style>
            body {
                font-family: Arial, Helvetica, sans-serif;
            }
            form {
                border: 3px solid #f1f1f1;
                margin-left:32.5%;
                width:35%;
            }
            h2 {
                text-align: center;
                font-family: Gill Sans;
                line-height: 2.2;
                font-weight: 100;
                font-variant: small-caps;
                font-size:32px;
                margin-top: 2%;
                flex:50%;
            }
            input[type=text], input[type=password] {
              width: 100%;
              padding: 12px 20px;
              margin: 8px 0;
              display: inline-block;
              border: 1px solid #ccc;
              box-sizing: border-box;
              font-size: 12.5px;
            }
            .container {
              padding: 16px;
            }
            button {
              background-color: #3A484A;
              color: white;
              padding: 14px 20px;
              margin: 8px 0;
              border: none;
              cursor: pointer;
              width: 100%;
              font-size:15px;
              font-variant: small-caps;
              font-weight: 100;
              transition: .3s ease;
            }
            button:hover {
              background-color: #F98084
            }

            .imgcontainer {
              text-align: center;
              margin: 24px 0 12px 0;
            }
            img.avatar {
              width: 35%;
            }
            .imgtitulo {
              display:flex;
              text-align: center;
              margin: 24px 0 12px 0;
              width: 30%;
              margin-left:34.6%;
            }
            img.tit {
              flex: 50%;
              width: 1px;
              margin-right: 24px;
              margin-left: -24px;
            }
        </style>
        <head>
            <link rel="shortcut icon" href="/assets/favicon.ico" />
            <title>BARBOSA</title>
        </head>
        <div class="imgtitulo">
            <h2> Bienvenido a </h2>
            <img src="/assets/logo.png" class="tit">
        </div>
        <form action="" method="post">
            <div class="imgcontainer">
                <img src="/assets/avatar.png"  alt="Avatar" class="avatar"> <!--Icono diseñado por Freepik encontrado en la web https://www.flaticon.es/-->
            </div>
            <div class="container">
                <label for="username"><b>Nombre de usuario</b></label>
                <input type=text name=username placeholder="Introduzca usuario" required>
                <p><label for="password"><b>Contraseña</b></label>
                <input type=password name=password placeholder="Introduzca contraseña" required>
                <button type="submit">Iniciar sesión</button>
            </div>
        </form>
        ''')

@server.errorhandler(401)
def error(e):
    return Response(
    '''<style>
        body {font-family: Arial, Helvetica, sans-serif;}
        form {
            border: 3px solid #f1f1f1;
            margin-top:5%;
            margin-left:30%;
            width:40%;
        }
        h2 {
            text-align: center;
            font-family: Gill Sans;
            line-height: 2.2;
            font-weight: 100;
            font-variant: small-caps;
            font-size:32px;
            margin-top: 2%;
        }
        .container {
          padding: 10px;
          text-align: center;
          font-family: Gill Sans;
          font-weight: 100;
          font-size:25px;
          padding-bottom:10%;
        }
        .imgcontainer {
          text-align: center;
          margin: 24px 0 12px 0;
        }
        img.avatar {
          width: 35%;
        }
        img.error {
          width: 8%;
          float: left;
          margin-bottom:2%;
          margin-left:23%;
        }
        a.link {
            background-color: #3A484A;
            text-decoration: none;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            cursor: pointer;
            width: 100%;
            font-size:15px;
            font-weight: 100;
            font-variant: small-caps;
            transition: .3s ease;
        }
        a.link:hover {
            background-color: #F98084;
        }
        p.mensaje {
            padding-bottom:3%;
        }
    </style>
    <head>
        <link rel="shortcut icon" href="/assets/favicon.ico" />
        <title>BARBOSA</title>
    </head>
    <h2> Se ha producido un error en la autenticación </h2>
    <form action="" method="post">
        <div class="imgcontainer">
            <img src="/assets/contrasena.png" alt="Avatar" class="avatar"> <!--Iconos diseñados por Freepik encontrado en la web https://www.flaticon.es/-->
        </div>
        <div class="container">
            <p class="mensaje"> Por favor inténtelo de nuevo </p>
            <a class="link" href="http://127.0.0.1:8050/login/">Iniciar sesión</a>
        </div>
    </form>
    ''')

# Función load_user, obtenida del usuario numpynewb desde la página web: https://github.com/plotly/dash/issues/214
@login_manager.user_loader
def load_user(userid):
    return User(userid)

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>BARBOSA</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
@login_required

def display_page(pathname):
    if pathname == '/home/' or pathname == '/':
        return home_layout
    elif pathname == '/principal/arousal/':
        return arousal_layout
    elif pathname == '/principal/valence/':
        return valence_layout
    elif pathname == '/detalle_hashtag/':
        return hashtag_detail_layout
    elif pathname == '/detalle_colaborador/':
        return speakers_detail_layout
    else:
        return page_not_found_layout

@server.route("/logout/")
@login_required
def logout():
    logout_user()
    return Response(
    '''<style>
        body {font-family: Arial, Helvetica, sans-serif;}
        form {
            border: 3px solid #f1f1f1;
            margin-left:30%;
            width:40%;
        }
        h2 {
            text-align: center;
            font-family: Gill Sans;
            line-height: 2.2;
            font-weight: 100;
            font-variant: small-caps;
            font-size:32px;
            margin-top: 2%;
        }
        .container {
          padding: 10px;
          text-align: center;
          font-family: Gill Sans;
          font-weight: 100;
          font-size:25px;
          padding-bottom:10%;
        }
        .imgcontainer {
          text-align: center;
          margin: 24px 0 12px 0;
        }
        img.avatar {
          height: 20%;
          width:32%
        }
        img.error {
          width: 8%;
          float: left;
          margin-bottom:2%;
          margin-left:23%;
        }
        a.link {
            background-color: #3A484A;
            text-decoration: none;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            cursor: pointer;
            width: 100%;
            font-size:15px;
            font-weight: 100;
            font-variant: small-caps;
            transition: .3s ease;
        }
        a.link:hover {
            background-color: #F98084;
        }
        p.mensaje {
            padding-bottom:3%;
        }
    </style>
    <head>
        <link rel="shortcut icon" href="/assets/favicon.ico" />
        <title>BARBOSA</title>
    </head>
    <h2> Su sesión ha finalizado </h2>
    <form action="" method="post">
        <div class="imgcontainer">
            <img src="/assets/salir.png" alt="Avatar" class="avatar"> <!--Iconos diseñados por Freepik encontrado en la web https://www.flaticon.es/-->
        </div>
        <div class="container">
            <p class="mensaje"> ¿Desea volver a iniciar sesión? </p>
            <a class="link" href="http://127.0.0.1:8050/login/">Iniciar sesión</a>
        </div>
    </form>
    ''')

if __name__ == '__main__':
    app.run_server(debug=True)
