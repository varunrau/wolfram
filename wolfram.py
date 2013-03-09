<<<<<<< HEAD
from bottle import route, run
from sympy import Matrix
from numpy import linalg
=======
from bottle import route, run, template, view, post, request, get, static_file
import re
>>>>>>> d73187938a7803e5a2f9c4a8888b3d97025ae341

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


    def quadratic(a, b, c):
    	return max((-b + math.sqrt(b*b-4*a*c))/(2*a), (-b + math.sqrt(b*b-4*a*c))/(2*a))

    def matrixz(force, mass, acceleration, velocity_i, velocity_f, distance, time)
    	force_basic = [mass*acceleration, force]
        distance_orig = [velocity_i*time, 1/2 * acceleration * time * time, distance]
        velocityf2_orig = [velocity_i*velocity_i, 2*acceleration*distance, velocity_f*velocity_f]
        velocity_f_orig = [velocity_i, acceleration*time, velocity_f]


    	mass_basic = [force/acceleration, mass]
    	accel_basic = [force/mass, acceleration]
    	vinitial_nof = [distance/(time), -.5*acceleration*time, velocity_i]
    	time_nof1 = [-velocity_i/acceleration, math.sqrt(velocity_i*velocity_i + 2*acceleration*distance), time]
    	time_nof2 = [-velocity_i/acceleration, -math.sqrt(velocity_i*velocity_i + 2*acceleration*distance), time]
        accel_nof = [2*distance/(time**2), -2*velocity_i*time/(time**2), acceleration]
        vinitial_f = [math.sqrt(velocity_f - 2 * acceleration * distance), velocity_i]
    	accel_f = [velocity_f*velocity_f/(2*distance), -velocity_i*velocity_i/(2*distance), acceleration]
    	distance_f = [velocity_f*velocity_f/(2*acceleration), -velocity_i*velocity_i/(2*acceleration), distance]
        velocity_i_nod = [velocity_f, -acceleration*time, velocity_i]
        accel_nod = [velocity_f/time, -velocity_i/time, acceleration]
        time_nod = [velocity_f/acceleration, -velocity_i/acceleration, time]
        distance_orig = [velocity_i/2*time, velocity_f/2*time, distance]
        time_noaccel = [2*distance/(velocity_i + velocity_f), time]
        vinitial_noaccel = [2*distance/time, -velocity_f, velocity_i]
        vfinal_noaccel = [2*distance/time, -velocity_i, velocity_f]
        






    	A = Matrix([[force_basic, velocityf2_orig, velocity_f_orig, distance_orig], [force_basic, velocityf2_orig, velocity_f_orig, distance_orig], [force_basic, velocityf2_orig, velocity_f_orig, distance_orig], [force_basic, velocityf2_orig, velocity_f_orig, distance_orig])
    	
    	print(A.rref())


    		/mass, force/acceleration, force, velocity_i*time, 1/2*acceleration*time*time, distance, ], [mass, acceleration, mass*acceleration, force/mass, force/acceleration, force])
run(host='localhost', port=8000, debug=True)
