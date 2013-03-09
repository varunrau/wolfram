import math
def solver(force=None, mass=None, acceleration=None, velocity_i=None, velocity_f=None, distance=None, time=None, torque=None, radius=None, theta=None, height = None):

    theta = theta * math.pi/180
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
        values["velocity_i"] = None
        values["velocity_f"] = None
        values["distance"] = None
        values["time"] = None
        values["torque"] = None
        values["radius"] = None
        values["theta"] = None
        values["height"] = None

        if velocity_i and time and theta:
            dist1 = velocity_i * time - 1/2 * g * math.sin(theta) * time**2
            values["distance"] = dist1
        if distance and time != 0 and theta:
            velocity_i = (distance - .5 * g * math.sin(theta) * time**2)/time
            values["vi"] = velocity_i
        if velocity_i and distance and theta:
            time_nof = quadratic(.5 * g * math.sin(theta), velocity_i, -distance)
            values["time"] = time_nof
        if theta:
            if acceleration is None:
                acceleration = g * math.sin(theta)
            else:
                acceleration -= g * math.sin(theta)
            values["acceleration"] = acceleration
            if distance and time and height:
                height = height * math.sin(theta)
                values["height"] = height
        if theta and force:
            mass = force/(g * math.sin(theta))
            values["mass"] = mass

        change = True
        while change:
            change = False
            if velocity_i and time and theta:
                dist1 = velocity_i * time - 1/2 * g * math.sin(theta) * time**2
                if dist1 != values["distance"]:
                    values["distance"] = dist1
                    change = True
            if distance and time != 0 and theta:
                velocity_i = (distance - .5 * g * math.sin(theta) * time**2)/time
                if velocity_i != values["vi"]:
                    values["vi"] = velocity_i
                    change = True
            if velocity_i and distance and theta:
                time_nof = quadratic(.5 * g * math.sin(theta), velocity_i, -distance)
                if time_nof != values["time"]:
                    values["time"] = time_nof
                    change = True
            if theta and velocity_i:
                time = -velocity_i/acceleration
                if time:
                    dist1 = velocity_i * time - 1/2 * acceleration * time**2
                    if dist1 != values["distance"]:
                        values["distance"] = dist1
                        change = True
                if distance:
                    time_nof = quadratic(.5 * acceleration, velocity_i, -distance)
                    if time_nof != values["time"]:
                        values["time"] = time_nof
                        change = True
                if distance and time and height:
                    height = height * math.sin(theta)
                    if height != values["height"]:
                        values["height"] = height
                        change = True
            elif theta and force:
                mass = force/(g * math.sin(theta))
                if mass != values["mass"]:
                    values["mass"] = mass
                    change = True
                acceleration = force/mass
                if acceleration != values["acceleration"]:
                    values["acceleration"] = mass
                    change = True
        return values

    def projectileproblem(force=None, mass=None, acceleration=None, velocity_i=None, velocity_f=None, distance=None, time=None, torque=None, radius=None, theta=None, height = None):
        if height:
            time = math.sqrt(2*height/g)
            values["time"] = time
        if velocity_i and time:
            distance = velocity_i * time
            values["distance"] = distance
        if velocity_i and distance:
            velocity_i = distance/time
            values["vi"] = velocity_i
        if theta and velocity_i and time:
            height = velocity_i * math.sin(theta) * time/2 - 1/2 * g * (time/2)**2
            values["height"] = height

        change = True
        while change:
            change = False
            if height:
                time = math.sqrt(2*height/g)
                if time != values["time"]:
                    values["time"] = time
                    changes = True
            if velocity_i and time:
                distance = velocity_i * time
                if distance != values["distance"]:
                    values["distance"] = distance
                    changes = True
            if velocity_i and distance:
                time = math.sqrt(2*height/g)
                if time != values["time"]:
                    values["time"] = time
                    changes = True
                velocity_i = distance/time
                if velocity_i != values["vi"]:
                    values["vi"] = velocity_i
                    changes = True
            if theta and velocity_i:
                time = 4 * velocity_i * math.sin(theta)/g
                if time != values["time"]:
                    values["time"] = time
                    changes = True
                distance = velocity_i * math.cos(theta) * time
                if distance != values["distance"]:
                    values["distance"] = time
                    changes = True
                height = velocity_i * math.sin(theta) * time/2 - 1/2 * g * (time/2)**2
                if height != values["height"]:
                    values["height"] = height
                    changes = True
        return values


    def kinematicproblem(force=None, mass=None, acceleration=None, velocity_i=None, velocity_f=None, distance=None, time=None, torque=None, radius=None, theta=None, height = None):
        if mass and acceleration:
            force = mass * acceleration
            values["force"] = force
        if force and acceleration:
            mass = force/acceleration
            values["mass"] = mass
        if force and mass:
            acceleration = force/mass
            values["acceleration"] = acceleration
        if velocity_i and time and acceleration:
            distance_orig = velocity_i*time - .5 * acceleration*time*time
            values["distance"] = distance_orig
        if velocity_i and acceleration and distance:
            velocityf2_orig = velocity_i**2 + 2 * acceleration*distance
            values["velocityf2"] = velocityf2_orig
        if velocity_i and acceleration and time:
            velocityf = velocity_i + acceleration * time
            values["velocityf"] = velocityf
        if distance and acceleration and time:
            vinitial_nof = (distance - .5 * acceleration * time**2)/time
            values["vi"] = vinitial_nof
        if acceleration and velocity_i and distance:
            time_nof = quadratic(.5 * acceleration, velocity_i, -distance)
            values["time"] = time_nof
        if distance and velocity_i and time:
            accel_nof = (2 * (distance - velocity_i * time))/(time*time)
            values["acceleration"] = accel_nof
        if velocity_f and acceleration and distance:
            vinitial_f = math.sqrt(velocity_f*velocity_f - 2*acceleration*distance)
            values["vi"] = vinitial_f
        if velocity_f and velocity_i and distance:
            accel_f = (velocity_f*velocity_f - velocity_i*velocity_i)/(2*distance)
            values["acceleration"] = accel_f
        if velocity_f and velocity_i and acceleration:
            distance_f = (velocity_f*velocity_f - velocity_i*velocity_i)/(2*acceleration)
            values["distance"] = distance_f
        if velocity_f and acceleration and time:
            vinitial_nod = velocity_f - acceleration * time
            values["vi"] = vinitial_nod
        if velocity_f and velocity_i and time:
            acceleration_nod = (velocity_f - velocity_i)/time
            values["acceleration"] = acceleration_nod
        if velocity_i and velocity_f and acceleration:
            time_nod = (velocity_f - velocity_i)/acceleration
            values["time"] = time_nod
        if distance and time and velocity_f:
            vinitial_noaccel = 2*distance/time - velocity_f
            values["vi"] = vinitial_noaccel
        if distance and time and velocity_i:
            vfinal_noaccel = 2*distance/time - velocity_i
            values["velocity_f"] = vfinal_noaccel
        if distance and velocity_i and velocity_f:
            time_noaccel = 2*distance/(velocity_i + velocity_f)
            values["time"] = time_noaccel

        change = True
        while change:
            change = False
            if mass and acceleration:
                force = mass * acceleration
                if force != values["force"]:
                    values["force"] = force
                    change = True
            if force and acceleration and acceleration != 0:
                mass_basic = force/acceleration
                if mass != values["mass"]:
                    values["mass"] = mass
                    change = True
            if force and mass:
                acceleration = force/mass
                if acceleration != values["acceleration"]:
                    values["acceleration"] = acceleration
                    change = True
            if velocity_i and time and acceleration:
                distance_orig = velocity_i*time - .5 * acceleration*time*time
                if distance_orig != values["distance"]:
                    values["distance"] = distance_orig
                    change = True
            if velocity_i and acceleration and distance:
                velocityf2_orig = velocity_i**2 + 2 * acceleration*distance
                if velocityf2_orig != values["velocityf2"]:
                    values["velocityf2"] = velocityf2_orig
                    change = True
            if velocity_i and acceleration and time:
                velocityf = velocity_i + acceleration*time
                if velocityf != values["velocityf"]:
                    values["velocityf"] = velocityf
                    change = True
            if distance and acceleration and time and time != 0:
                vinitial_nof = (distance - .5 * acceleration*time*time)/time
                if vinitial_nof != values["vi"]:
                    values["vi"] = vinitial_nof
                    change = True
            if acceleration and velocity_i and distance:
                time_nof = quadratic(.5 * acceleration, velocity_i, -distance)
                if time_nof != values["time"]:
                    values["time"] = time_nof
                    change = True
            if distance and velocity_i and time and time != 0:
                accel_nof = (2 * (distance - velocity_i*time))/(time*time)
                if accel_nof != values["acceleration"]:
                    values["acceleration"] = accel_nof
                    change = True

            if velocity_f and acceleration and distance:
                vinitial_f = math.sqrt(velocity_f*velocity_f - 2*acceleration*distance)
                if vinitial_f != values["vi"]:
                    values["vi"] = vinitial_f
                    change = True
            if velocity_f and velocity_i and distance:
                accel_f = (velocity_f*velocity_f - velocity_i*velocity_i)/(2*distance)
                if accel_f != values["acceleration"]:
                    values["acceleration"] = accel_f
                    change = True
            if velocity_f and velocity_i and acceleration:
                distance_f = (velocity_f*velocity_f - velocity_i*velocity_i)/(2*acceleration)
                if distance_f != values["distance"]:
                    values["distance"] = distance_f
                    change = True
            if velocity_f and acceleration and time:
                vinitial_nod = velocity_f - acceleration * time
                if vinitial_nod != values["vi"]:
                    values["vi"] = vinitial_nod
                    change = True
            if velocity_f and velocity_i and time:
                acceleration_nod = (velocity_f - velocity_i)/time
                if acceleration_nod != values["acceleration"]:
                    values["acceleration"] = acceleration_nod
                    change = True
            if velocity_i and velocity_f and acceleration:
                time_nod = (velocity_f - velocity_i)/acceleration
                if time_nod != values["time"]:
                    values["time"] = time_nod
                    change = True
            if distance and time and velocity_f:
                vinitial_noaccel = 2*distance/time - velocity_f
                if vinitial_noaccel != values["vi"]:
                    values["vi"] = vinitial_noaccel
                    change = True
            if distance and time and velocity_i:
                vfinal_noaccel = 2*distance/time - velocity_i
                if vfinal_noaccel != values["velocity_f"]:
                    values["velocity_f"] = vfinal_noaccel
                    change = True
            if distance and velocity_i and velocity_f:
                time_noaccel = 2*distance/(velocity_i + velocity_f)
                if time_noaccel != values["time"]:
                    values["time"] = time_noaccel
                    change = True
        return values

    types["hill"] = hillproblem(force, mass, acceleration, velocity_i, velocity_f, distance, time, torque, radius, theta, height)
    types["projectile"] = projectileproblem(force, mass, acceleration, velocity_i, velocity_f, distance, time, torque, radius, theta, height)
    types["kinematics"] = kinematicproblem(force, mass, acceleration, velocity_i, velocity_f, distance, time, torque, radius, theta, height)
    return types["hill"]