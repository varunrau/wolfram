import math
import Queue

steps = []
def solver(force=None, mass=None, acceleration=None, velocity_i=None, velocity_f=None, distance=None, time=None, torque=None, radius=None, theta=None, height = None):

    if theta:
        print theta
        print 'that was theta'
        theta = float(theta) * math.pi/180
    g = 9.8
    values = {}
    types = {}

    def quadratic(a, b, c):
        if a == 0:
            return -c/b
        return max((-b + math.sqrt(b**2 - 4*a*c))/(2*a), (-b - math.sqrt(b**2 - 4*a*c))/(2*a))

    if force:
        force = float(force)
        values["force"] = force
    if mass:
        mass = float(mass)
        values["mass"] = mass
    if acceleration:
        acceleration = float(acceleration)
        values["acceleration"] = acceleration
    if velocity_i:
        velocity_i = float(velocity_i)
        values["vi"] = velocity_i
    if velocity_f:
        velocity_f = float(velocity_f)
        values["velocity_f"] = velocity_f
    if distance:
        distance = float(distance)
        values["distance"] = distance
    if time:
        time = float(time)
        values["time"] = time
    if torque:
        torque = float(torque)
        values["torque"] = torque
    if radius:
        radius = float(radius)
        values["radius"] = radius
    if theta:
        theta = float(theta)
        values["theta"] = theta
    if height:
        height = float(height)
        values["height"] = height


    def hillproblem(force=None, mass=None, acceleration=None, velocity_i=None, velocity_f=None, distance=None, time=None, torque=None, radius=None, theta=None, height = None):

        values["force"] = None
        values["mass"] = None
        values["acceleration"] = None
        values["vi"] = None
        values["velocity_f"] = None
        values["distance"] = None
        values["time"] = None
        values["torque"] = None
        values["radius"] = None
        values["theta"] = None
        values["height"] = None

        if force:
            force = float(force)
            values["force"] = force
        if mass:
            mass = float(mass)
            values["mass"] = mass
        if acceleration:
            acceleration = float(acceleration)
            values["acceleration"] = acceleration
        if velocity_i:
            velocity_i = float(velocity_i)
            values["vi"] = velocity_i
        if velocity_f:
            velocity_f = float(velocity_f)
            values["velocity_f"] = velocity_f
        if distance:
            distance = float(distance)
            values["distance"] = distance
        if time:
            time = float(time)
            values["time"] = time
        if torque:
            torque = float(torque)
            values["torque"] = torque
        if radius:
            radius = float(radius)
            values["radius"] = radius
        if theta:
            theta = float(theta)
            values["theta"] = theta
        if height:
            height = float(height)
            values["height"] = height


        if theta:
            if acceleration is None:
                acceleration = g * math.sin(theta)
                steps.append("Acceleration = g * Sin(theta)")
            else:
                acceleration -= g * math.sin(theta)
                steps.append("Acceleration = acceleration - g * Sin(theta)")
            values["acceleration"] = acceleration

        change = True
        while change:
            change = False
            if velocity_i and time and theta:
                dist1 = velocity_i * time - 1/2 * g * math.sin(theta) * time**2
                if dist1 != values["distance"]:
                    steps.append("Distance = V_0 * time - 1/2 * g * Sin(theta) * time^2")
                    steps.append("Distance = " + str(dist1))
                    values["distance"] = dist1
                    change = True
            if distance and time != 0 and theta:
                velocity_i = (distance - .5 * g * math.sin(theta) * time**2)/time
                if velocity_i != values["vi"]:
                    steps.append("(V_0 = distance - 1/2 * g * Sin(theta) * time^2)/time")
                    steps.append("V_0 = " + str(velocity_i))
                    values["vi"] = velocity_i
                    change = True
            if velocity_i and distance and theta:
                time_nof = quadratic(.5 * g * math.sin(theta), velocity_i, -distance)
                if time_nof != values["time"]:
                    steps.append("Time = (-v0 +- sqrt(v0^2 - 4*(.5*g*Sin(theta))*(-distance)))/(2*g*Sin(theta))")
                    steps.append("Time = " + str(time_nof))
                    values["time"] = time_nof
                    change = True
            if theta and velocity_i and acceleration:
                time = -velocity_i/acceleration
                if time:
                    dist1 = velocity_i * time - 1/2 * acceleration * time**2
                    if dist1 != values["distance"]:
                        values["distance"] = dist1
                        steps.append("Distance = velocity_i * time - 1/2 * acceleration * time^2")
                        steps.append("Distance = " + str(dist1))
                        change = True
                if distance:
                    time_nof = quadratic(.5 * acceleration, velocity_i, -distance)
                    if time_nof != values["time"]:
                        values["time"] = time_nof
                        steps.append("Time = (-v0 +- sqrt(v0^2 - 4*(.5*g*Sin(theta))*(-distance)))/(2*g*Sin(theta))")
                        steps.append("Time = " + str(time.nof))
                        change = True
                if distance and time and height:
                    height = height * math.sin(theta)
                    if height != values["height"]:
                        values["height"] = height
                        steps.append("Height = Height * Sin(theta)")
                        steps.append("Height = " + str(height))
                        change = True
            elif theta and force:
                mass = force/(g * math.sin(theta))
                if mass != values["mass"]:
                    values["mass"] = mass
                    steps.append("Mass = force/(g * Sin(theta))")
                    steps.append("Mass = " + str(mass))
                    change = True
                acceleration = force/mass
                if acceleration != values["acceleration"]:
                    values["acceleration"] = mass
                    steps.append("Acceleration = force/mass")
                    steps.append("Acceleration = " + str(acceleration))
                    change = True
        return values

    def projectileproblem(force=None, mass=None, acceleration=None, velocity_i=None, velocity_f=None, distance=None, time=None, torque=None, radius=None, theta=None, height = None):

        values["force"] = None
        values["mass"] = None
        values["acceleration"] = None
        values["vi"] = None
        values["velocity_f"] = None
        values["distance"] = None
        values["time"] = None
        values["torque"] = None
        values["radius"] = None
        values["theta"] = None
        values["height"] = None

        if force:
            force = float(force)
            values["force"] = force
        if mass:
            mass = float(mass)
            values["mass"] = mass
        if acceleration:
            acceleration = float(acceleration)
            values["acceleration"] = acceleration
        if velocity_i:
            velocity_i = float(velocity_i)
            values["vi"] = velocity_i
        if velocity_f:
            velocity_f = float(velocity_f)
            values["velocity_f"] = velocity_f
        if distance:
            distance = float(distance)
            values["distance"] = distance
        if time:
            time = float(time)
            values["time"] = time
        if torque:
            torque = float(torque)
            values["torque"] = torque
        if radius:
            radius = float(radius)
            values["radius"] = radius
        if theta:
            theta = float(theta)
            values["theta"] = theta
        if height:
            height = float(height)
            values["height"] = height

        change = True
        while change:
            change = False
            if height:
                time = math.sqrt(2 * height/g)
                if time != values["time"]:
                    values["time"] = time
                    steps.append("Time = Sqrt(2 * height/gravity)")
                    steps.append("Time = " + str(time))
                    changes = True
            if velocity_i and time:
                distance = velocity_i * time
                if distance != values["distance"]:
                    steps.append("Distance = v0 * time")
                    steps.append("Distance = " + str(distance))
                    values["distance"] = distance
                    changes = True
            if time and distance:
                velocity_i = distance/time
                if velocity_i != values["vi"]:
                    steps.append("V_0 = distance/time")
                    steps.append("V_0 = " + str(velocity_i))
                    values["vi"] = velocity_i
                    changes = True
            if theta and velocity_i:
                time = 4 * velocity_i * math.sin(theta)/g
                if time != values["time"]:
                    values["time"] = time
                    steps.append("Time = 4 * v0 * Sin(theta)/gravity")
                    steps.append("Time = " + str(time))
                    changes = True
                distance = velocity_i * math.cos(theta) * time
                if distance != values["distance"]:
                    values["distance"] = time
                    steps.append("Distance = v0 * Cos(theta) * time")
                    steps.append("Distance = " + str(distance))
                    changes = True
                height = velocity_i * math.sin(theta) * time/2 - 1/2 * g * (time/2)**2
                if height != values["height"]:
                    values["height"] = height
                    steps.append("Height = v0 * Sin(theta) * time/2 - 1/2 * g * (time/2)^2")
                    steps.append("Height = " + str(height))
                    changes = True
        return values


    def kinematicproblem(force=None, mass=None, acceleration=None, velocity_i=None, velocity_f=None, distance=None, time=None, torque=None, radius=None, theta=None, height = None):
        if mass and acceleration:
            force = mass * acceleration
            values["force"] = force
            steps.append("Force = mass * acceleration")
        if force and acceleration:
            mass = force/acceleration
            values["mass"] = mass
            steps.append("Mass = force/acceleration")
        if force and mass:
            acceleration = force/mass
            values["acceleration"] = acceleration
            steps.append("Acceleration = force/mass")
        if velocity_i and time and acceleration:
            distance_orig = velocity_i*time - .5 * acceleration*time*time
            values["distance"] = distance_orig
            steps.append("Distance = v0*time - .5 * acceleration*time^2")
        if velocity_i and acceleration and distance:
            velocityf2_orig = velocity_i**2 + 2 * acceleration*distance
            values["velocityf2"] = velocityf2_orig
            steps.append("Distance = v0^2 + 2 * acceleration * distance")
        if velocity_i and acceleration and time:
            velocityf = velocity_i + acceleration * time
            steps.append("V_f = v0 + acceleration * time")
            values["velocityf"] = velocityf
        if distance and acceleration and time:
            vinitial_nof = (distance - .5 * acceleration * time**2)/time
            values["vi"] = vinitial_nof
            steps.append("V0 = (distance - .5 * acceleration * time^2)/time")
        if acceleration and velocity_i and distance:
            time_nof = quadratic(.5 * acceleration, velocity_i, -distance)
            steps.append("Time = (-v0 +- sqrt(v0^2 - 4*(.5*acceleration)*(-distance)))/(2*acceleration)")
            values["time"] = time_nof
        if distance and velocity_i and time:
            accel_nof = (2 * (distance - velocity_i * time))/(time*time)
            values["acceleration"] = accel_nof
            steps.append("Acceleration = (2 * (distance - v0 * time))/(time^2)")
        if velocity_f and acceleration and distance:
            vinitial_f = math.sqrt(velocity_f*velocity_f - 2*acceleration*distance)
            values["vi"] = vinitial_f
            steps.append("V0 = Sqrt(velocity_f^2 - 2 * acceleration * distance)")
        if velocity_f and velocity_i and distance:
            accel_f = (velocity_f*velocity_f - velocity_i*velocity_i)/(2*distance)
            steps.append("Acceleration = (velocity_f^2 - velocity_i^2)/ (2 * distance)")
            values["acceleration"] = accel_f
        if velocity_f and velocity_i and acceleration:
            distance_f = (velocity_f*velocity_f - velocity_i*velocity_i)/(2*acceleration)
            values["distance"] = distance_f
            steps.append("Distance = (velocity_f^2 - velocity_i^2)/ (2 * acceleration)")
        if velocity_f and acceleration and time:
            vinitial_nod = velocity_f - acceleration * time
            values["vi"] = vinitial_nod
            steps.append("V0 = vf - acceleration * time")
        if velocity_f and velocity_i and time:
            acceleration_nod = (velocity_f - velocity_i)/time
            values["acceleration"] = acceleration_nod
            steps.append("Acceleration = (velocity_f - velocity_i)/time")
        if velocity_i and velocity_f and acceleration:
            time_nod = (velocity_f - velocity_i)/acceleration
            values["time"] = time_nod
            steps.append("Time = (velocity_f - velocity_i)/acceleration")
        if distance and time and velocity_f:
            vinitial_noaccel = 2*distance/time - velocity_f
            values["vi"] = vinitial_noaccel
            steps.append("v0 = 2 * distance/time - vf")
        if distance and time and velocity_i:
            vfinal_noaccel = 2*distance/time - velocity_i
            values["velocity_f"] = vfinal_noaccel
            steps.append("vf = 2 * distance/time - v0")
        if distance and velocity_i and velocity_f:
            time_noaccel = 2*distance/(velocity_i + velocity_f)
            values["time"] = time_noaccel
            steps.append("time = 2 * distance/(v0 + vf)")

        change = True
        while change:
            print 'in lloop'
            change = False
            if mass and acceleration:
                force = mass * acceleration
                if force != values["force"]:
                    steps.append("Force = mass * acceleration")
                    steps.append("Force = " + force)
                    values["force"] = force
                    change = True
                    steps.append("Force = mass * acceleration")
            if force and acceleration and acceleration != 0:
                mass_basic = force/acceleration
                if mass != values["mass"]:
                    steps.append("Mass = force/acceleration")
                    steps.append("Mass = " + mass_basic)
                    values["mass"] = mass
                    change = True
            if force and mass:
                acceleration = force/mass
                if acceleration != values["acceleration"]:
                    values["acceleration"] = acceleration
                    steps.append("Acceleration = force/mass")
                    steps.append("Acceleration = " + acceleration)
                    change = True
            if velocity_i and time and acceleration:
                distance_orig = velocity_i*time - .5 * acceleration*time*time
                if distance_orig != values["distance"]:
                    values["distance"] = distance_orig
                    steps.append("Distance = v0*time - .5 * acceleration*time^2")
                    steps.append("Distance = " + distance_orig)
                    change = True
            if velocity_i and acceleration and distance:
                velocityf2_orig = velocity_i**2 + 2 * acceleration*distance
                if velocityf2_orig != values["velocityf2"]:
                    values["velocityf2"] = velocityf2_orig
                    change = True
                    steps.append("Vf^2 = v0^2 + 2 * acceleration * distance")
                    steps.append("Vf^2 = " + velocityf2_orig)
            if velocity_i and acceleration and time:
                velocityf = velocity_i + acceleration*time
                if velocityf != values["velocityf"]:
                    values["velocityf"] = velocityf
                    change = True
                    print "adding to steps"
                    steps.append("V_f = v0 + acceleration * time")
                    steps.append("V_f = " + velocityf)
                    print steps
            if distance and acceleration and time and time != 0:
                vinitial_nof = (distance - .5 * acceleration*time*time)/time
                if vinitial_nof != values["vi"]:
                    values["vi"] = vinitial_nof
                    change = True
                    steps.append("V_0 = (distance - .5 * acceleration * time^2)/time")
                    steps.append("V_0 = " + vinitial_nof)
            if acceleration and velocity_i and distance:
                time_nof = quadratic(.5 * acceleration, velocity_i, -distance)
                if time_nof != values["time"]:
                    values["time"] = time_nof
                    change = True
                    steps.append("Time = (-v0 +- sqrt(v0^2 - 4*(.5*acceleration)*(-distance)))/(2*acceleration)")
                    steps.append("Time = " + time_nof)
            if distance and velocity_i and time and time != 0:
                accel_nof = (2 * (distance - velocity_i*time))/(time*time)
                if accel_nof != values["acceleration"]:
                    values["acceleration"] = accel_nof
                    change = True
                    steps.append("Acceleration = (2 * (distance - v0 * time))/(time^2)")
                    steps.append("Acceleration = " + accel_nof)
            if velocity_f and acceleration and distance:
                vinitial_f = math.sqrt(velocity_f*velocity_f - 2*acceleration*distance)
                if vinitial_f != values["vi"]:
                    values["vi"] = vinitial_f
                    change = True
                    steps.append("V_0 = Sqrt(velocity_f^2 - 2 * acceleration * distance)")
                    steps.append("V_0 = " + vinitial_f)
            if velocity_f and velocity_i and distance:
                accel_f = (velocity_f*velocity_f - velocity_i*velocity_i)/(2*distance)
                if accel_f != values["acceleration"]:
                    values["acceleration"] = accel_f
                    change = True
                    steps.append("Acceleration = (velocity_f^2 - velocity_i^2)/ (2 * distance)")
                    steps.append("Acceleration = " + accel_f)
            if velocity_f and velocity_i and acceleration:
                distance_f = (velocity_f*velocity_f - velocity_i*velocity_i)/(2*acceleration)
                if distance_f != values["distance"]:
                    values["distance"] = distance_f
                    change = True
                    steps.append("Distance = (velocity_f^2 - velocity_i^2)/ (2 * acceleration)")
                    steps.append("Distance = " + distance_f)
            if velocity_f and acceleration and time:
                vinitial_nod = velocity_f - acceleration * time
                if vinitial_nod != values["vi"]:
                    values["vi"] = vinitial_nod
                    change = True
                    steps.append("V_0 = vf - acceleration * time")
                    steps.append("V_0 = " + vinitial_f)
            if velocity_f and velocity_i and time:
                acceleration_nod = (velocity_f - velocity_i)/time
                if acceleration_nod != values["acceleration"]:
                    values["acceleration"] = acceleration_nod
                    change = True
                    steps.append("Acceleration = (velocity_f - velocity_i)/time")
                    steps.append("Acceleration = " + acceleration_nod)
            if velocity_i and velocity_f and acceleration:
                time_nod = (velocity_f - velocity_i)/acceleration
                if time_nod != values["time"]:
                    values["time"] = time_nod
                    change = True
                    steps.append("Time = (velocity_f - velocity_i)/acceleration")
                    steps.append("Time = " + time_nod)
            if distance and time and velocity_f:
                vinitial_noaccel = 2*distance/time - velocity_f
                if vinitial_noaccel != values["vi"]:
                    values["vi"] = vinitial_noaccel
                    change = True
                    steps.append("V_0 = 2 * distance/time - vf")
                    steps.append("V_0 = " + vinitial_noaccel)
            if distance and time and velocity_i:
                vfinal_noaccel = 2*distance/time - velocity_i
                if vfinal_noaccel != values["velocity_f"]:
                    values["velocity_f"] = vfinal_noaccel
                    change = True
                    steps.append("V_F = 2 * distance/time - v0")
                    steps.append("V_F = " + vfinal_noaccel)
            if distance and velocity_i and velocity_f:
                time_noaccel = 2*distance/(velocity_i + velocity_f)
                if time_noaccel != values["time"]:
                    values["time"] = time_noaccel
                    change = True
                    steps.append("Time = 2 * distance/(v0 + vf)")
                    steps.append("Time = " + time_noaccel)
        return values


    types["hill"] = hillproblem(force, mass, acceleration, velocity_i, velocity_f, distance, time, torque, radius, theta, height)
    types["projectile"] = projectileproblem(force, mass, acceleration, velocity_i, velocity_f, distance, time, torque, radius, theta, height)
    types["kinematics"] = kinematicproblem(force, mass, acceleration, velocity_i, velocity_f, distance, time, torque, radius, theta, height)
    return types["projectile"]

def oursteps():
    statement = "Here we will show you the steps we took to get the answer. \nFirst, we do: "
    return steps
