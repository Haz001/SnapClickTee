# Flask modules
from flask import render_template, request
from jinja2 import TemplateNotFound

# App modules
from apps import app


# example
# from apps.view import user

# App main route + generic routing
@app.route('/')
def index():
    try:

        return render_template('index.html')

    except TemplateNotFound:
        print("404")
        return "Shit is fucked up", 404

@app.route('/ai_merge')
def merge():
    try:
        return render_template('merge.html')
    except TemplateNotFound:
        print("404")
        return "Shit is fucked up", 404
