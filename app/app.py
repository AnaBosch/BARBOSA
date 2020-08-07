# -*- coding: utf-8 -*-
import dash
import flask
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

server = flask.Flask(__name__)

server.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_xxx'
)

login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = "login"

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, server = server, external_stylesheets=external_stylesheets)

app.renderer = 'var renderer = new DashRenderer();'
server = app.server
app.config.suppress_callback_exceptions = True
