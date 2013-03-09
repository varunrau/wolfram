from bottle import route, run, template, view, post, request, get, static_file
import nltk
import re
from sympy import Matrix
from numpy import linalg
import math
from solver import *

@route('/')
@view('main_template')
def main():
    return dict(values=None)

@post('/query')
@view('main_template')
def q():
    value = request.forms.get('value')
    # values = solver(5, 10, None, 15, None, 20)
    values = {'hi': 1, 'hello':2, 'world':3}
    return dict(values=values)

def evaluate(query):
    values_regex = re.compile('\w+ is \d+')
    question_regex = re.compile('\w+\?')
    values_matches = values_regex.findall(query)
    values = {}
    for match in values_matches:
        vals = match.split()
        values[vals[0]] = vals[2]
    values_matches = question_regex.findall(query)
    match = values_matches[0]
    question = match[:-1]
    return (values, question)

""" The next three methods are used to serve static files. """
@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get('/<filename:re:.*\.png>')
def images(filename):
    return static_file(filename, root='static/images')

run(host='localhost', port=8000, debug=True)
