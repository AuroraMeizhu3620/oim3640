from flask import Flask, render_template
from stocks import get_price

app = Flask(__name__)

@app.get('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

