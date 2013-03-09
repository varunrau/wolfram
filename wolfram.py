from bottle import route, run, template, view, post, request, get, static_file
import nltk
import re

@route('/')
@view('main_template')
def main():
    return dict(greeting='Wolfram')

@post('/query')
@view('query_template')
def q():
    value = request.forms.get('value')
    values, question = evaluate(value)
    return dict(values=values, question=question)

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
