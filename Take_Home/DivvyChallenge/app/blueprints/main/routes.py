from flask import render_template, request, jsonify
from .import bp as app
from .models import DivvyTable
from datetime import datetime as dt


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate')
def calculate():
    start = request.args.get('start')
    end = request.args.get('end')

        