from bottle import route, run
from sympy import Matrix
from numpy import linalg

@route('/')
def main():
    return "Hello World!"

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
