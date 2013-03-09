from bottle import route, run, template, view, post, request, get, static_file
#import nltk
import re
import math
from solver import *
from makeQuery import *

@route('/')
@view('main_template')
def main():
    return dict(values=None)

@post('/query')
@view('main_template')
def q():
    value = request.forms.get('value')
    return dict(values=values)

@post('/query-async')
def qa():
    query_dict = request.POST.dict
    query_string = query_dict['value']
    import ipdb; ipdb.set_trace() # BREAKPOINT

    print query_string
    vals_dict = create_query(query_string)
    print vals_dict
    vals_list = get_vals(vals_dict)
    values = solver(vals_list[0], vals_list[1], vals_list[2], vals_list[3], vals_list[4], vals_list[5], vals_list[6], vals_list[7], vals_list[8], vals_list[9], vals_list[10])
    return values

def get_vals(vals_dict):
    non_none = set()
    to_return = [None for x in range(12)]
    for key in vals_dict:
        value = vals_dict[key]
        if value is not None:
            if 'newtons' in "".join(value[1:].split()):
                to_return[0] = value[0]
            elif 'grams' in "".join(value[1:].split()):
                to_return[0] = value[1]
            elif 'meters per second squared' in "".join(value[1:].split()):
                to_return[0] = value[2]
            elif 'meters per second' in "".join(value[1:].split()):
                to_return[0] = value[3]
            elif 'meters per second' in "".join(value[1:].split()):
                to_return[0] = value[4]
            elif 'meters' in "".join(value[1:].split()):
                to_return[0] = value[5]
            elif 'seconds' in "".join(value[1:].split()):
                to_return[0] = value[6]
            elif 'stuff' in "".join(value[1:].split()):
                to_return[0] = value[7]
            elif 'meters' in "".join(value[1:].split()):
                to_return[0] = value[8]
            elif 'degrees' in "".join(value[1:].split()):
                to_return[0] = value[9]
            elif 'meters' in "".join(value[1:].split()):
                to_return[0] = value[10]
    return to_return


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
