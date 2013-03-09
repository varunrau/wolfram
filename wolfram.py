from bottle import route, run, template, view, post, request, get, static_file
#import nltk
import re
import math
from solver import *
from makeQuery import *

@route('/')
@view('main_template')
def main():
    return dict(values=None, steps=None)

@post('/query')
@view('main_template')
def q():
    value = request.forms.get('value')
    vals_dict = parser(value)
    print vals_dict
    vals_list = get_vals(vals_dict)
    values = solver(vals_list[0], vals_list[1], vals_list[2], vals_list[3], vals_list[4], vals_list[5], vals_list[6], vals_list[7], vals_list[8], vals_list[9], vals_list[10])
    new_dict = {}
    for key in values:
        if values[key] is not None:
            new_dict[key] = values[key]
    steps = oursteps()
    return dict(values=new_dict, steps=steps)

@post('/query-async')
def qa():
    return ''

def parser(str):
    strlist = str.split()
    val_dict = {}
    offset = 0
    for i in range(len(strlist)):
        unit = ""
        if re.match("\d+\.*\d*", strlist[i]):
            if i != (len(strlist) - 1):
                i += 1
            check = strlist[i]
            if check == 'N' or check == 'newtons' or check == 'newton' or check == 'g/m/s/s' or check == 'grams per meters per second squared' or check == 'g/m/s^2':
                unit = "newtons"
            elif check == 'g' or check == 'grams' or check == 'Grams' or check == 'G':
                unit = "grams"
            elif strlist[i] == 'meters per second squared' or check == 'm/s/s' or check == 'm/s^2' or check == 'm/s2':
                unit = 'meters per second squared'
            elif strlist[i] == 'meters per second' or check == "m/s" or check == "meter per second" or check == "meter per seconds":
                unit = "meters per second"
            elif check == "seconds" or check == "s." or check == "second" or check == "seconds.":
                print 'seconds'
                unit = "seconds"
            elif strlist[i] == "meters" or check == "meter" or check == "m":
                unit = "meters"
            elif strlist[i] == "degrees" or check == "degree" or check == "\*":
                unit = "degrees"
            val_dict[i] = strlist[i - 1] + " " + unit
        if strlist[i] == "distance" and re.match("\d+\.\d+", strlist[i + 2]):
            val_dict[i] = strlist[i + 2] + " " + "meters" + "(distance)"
    return val_dict


def get_vals(vals_dict):
    non_none = set()
    to_return = [None for x in range(12)]
    for key in vals_dict:
        value = vals_dict[key]
        if value is not None:
            if 'newtons' in value:
                to_return[0] = value.split()[0]
            elif 'grams' in value:
                to_return[1] = value.split()[0]
            elif 'meters per second squared' in value:
                to_return[2] = value.split()[0]
            elif 'meters per second' in value:
                to_return[3] = value.split()[0]
            elif 'meters per second' in value:
                to_return[4] = value.split()[0]
            elif 'meters' in value:
                to_return[5] = value.split()[0]
            elif 'seconds' in value:
                to_return[6] = value.split()[0]
            elif 'stuff' in value:
                to_return[7] = value.split()[0]
            elif 'meters' in value:
                to_return[8] = value.split()[0]
            elif 'degrees' in value:
                to_return[9] = value.split()[0]
            elif 'meters' in value:
                to_return[10] = value.split()[0]
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
