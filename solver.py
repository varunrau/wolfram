def solver(force=None, mass=None, acceleration=None, velocity_i=None, velocity_f=None, distance=None, time=None, torque=None, radius=None, theta=None):

    def quadratic(a, b, c):
        if a == 0:
            return -c/b
        return max((-b + math.sqrt(b**2 - 4*a*c))/(2*a), (-b - math.sqrt(b**2 - 4*a*c))/(2*a))

    values = {}
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
        values["velocity_i"] = velocity_i
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
    """
        force_basic = [mass*acceleration, force]
        distance_orig = [velocity_i*time, 1/2*acceleration*time*time, distance]
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
    force = mass*acceleration
    mass = force/acceleration
    acceleration = force/mass
    distance_orig = velocity_i*time - 1/2*acceleration*time*time
    velocityf2_orig = velocity_i**2 + 2*acceleration*distance
    velocity_f_orig = velocity_i + acceleration*time
    vinitial_nof = (distance - .5*acceleration*time*time)/time
    time_nof = quadratic(1/2*acceleration, velocity_i, -distance)
    accel_nof = (2*(distance - velocity_i*time))/(time*time)
    vinitial_f = math.sqrt(velocity_f*velocity_f - 2*acceleration*distance)
    accel_f = (velocity_f*velocity_f - velocity_i*velocity_i)/(2*distance)
    distance_f = (velocity_f*velocity_f - velocity_i*velocity_i)/(2*acceleration)
    vinitial_nod = velocity_f - acceleration * time
    acceleration_nod = (velocity_f - velocity_i)/time
    time_nod = (velocity_f - velocity_i)/acceleration
    vinitial_noaccel = 2*distance/time - velocity_f
    vfinal_noaccel = 2*distance/time - velocity_i
    time_noaccel = 2*distance/(velocity_i + velocity_f)

    hooks_force = -spring_constant * spring_displacement
    torque = radius*force*math.sin(theta)
    theta = math.asine(torque/(radius*force))
    force = torque/(radius*math.sin(theta))
    radius = torque/(force*sin(theta))
        """

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
        values["vinitial_nof"] = vinitial_nof
    if acceleration and velocity_i and distance:
        time_nof = quadratic(.5 * acceleration, velocity_i, -distance)
        values["t_nof"] = time_nof
    if distance and velocity_i and time:
        accel_nof = (2 * (distance - velocity_i * time))/(time*time)
        values["a_nof"] = accel_nof
    if velocity_f & acceleration & distance:
        vinitial_f = math.sqrt(velocity_f*velocity_f - 2*acceleration*distance)
        values["vi"] = vinitial_f
    if velocity_f & velocity_i & distance:
        accel_f = (velocity_f*velocity_f - velocity_i*velocity_i)/(2*distance)
        values["acceleration"] = accel_f
    if velocity_f & velocity_i & acceleration:
        distance_f = (velocity_f*velocity_f - velocity_i*velocity_i)/(2*acceleration)
        values["distance"] = distance_f
    if velocity_f & acceleration & time:
        vinitial_nod = velocity_f - acceleration * time
        values["vi"] = vinitial_nod
    if velocity_f & velocity_i & time:
        acceleration_nod = (velocity_f - velocity_i)/time
        values["acceleration"] = acceleration_nod
    if velocity_i & velocity_f & acceleration:
        time_nod = (velocity_f - velocity_i)/acceleration
        values["t"] = time_nod
    if distance & time & velocity_f:
        vinitial_noaccel = 2*distance/time - velocity_f
        values["vi"] = vinitial_noaccel
    if distance & time & velocity_i:
        vfinal_noaccel = 2*distance/time - velocity_i
        values["velocity_f"] = vfinal_noaccel
    if distance & velocity_i & velocity_f:
        time_noaccel = 2*distance/(velocity_i + velocity_f)
        values["t"] = time_noaccel

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
            if time_nof != values["t"]:
                values["t"] = time_nof
                change = True
        if distance and velocity_i and time and time != 0:
            accel_nof = (2 * (distance - velocity_i*time))/(time*time)
            if accel_nof != values["acceleration"]:
                values["acceleration"] = accel_nof
                change = True

        if velocity_f & acceleration & distance:
            vinitial_f = math.sqrt(velocity_f*velocity_f - 2*acceleration*distance)
            if vinitial_f != values["vi"]:
                values["vi"] = vinitial_f
                change = True
        if velocity_f & velocity_i & distance:
            accel_f = (velocity_f*velocity_f - velocity_i*velocity_i)/(2*distance)
            if accel_f != values["acceleration"]:
                values["acceleration"] = accel_f
                change = True
        if velocity_f & velocity_i & acceleration:
            distance_f = (velocity_f*velocity_f - velocity_i*velocity_i)/(2*acceleration)
            if distance_f != values["distance"]:
                values["distance"] = distance_f
                change = True
        if velocity_f & acceleration & time:
            vinitial_nod = velocity_f - acceleration * time
            if vinitial_nod != values["vi"]:
                values["vi"] = vinitial_nod
                change = True
        if velocity_f & velocity_i & time:
            acceleration_nod = (velocity_f - velocity_i)/time
            if acceleration_nod != values["acceleration"]
                values["acceleration"] = acceleration_nod
                change = True
        if velocity_i & velocity_f & acceleration:
            time_nod = (velocity_f - velocity_i)/acceleration
            if time_nod != values["t"]:
                values["t"] = time_nod
                change = True
        if distance & time & velocity_f:
            vinitial_noaccel = 2*distance/time - velocity_f
            if vinitial_noaccel != values["vi"]:
                values["vi"] = vinitial_noaccel
                change = True
        if distance & time & velocity_i:
            vfinal_noaccel = 2*distance/time - velocity_i
            if vfinal_noaccel != values["velocity_f"]:
                values["velocity_f"] = vfinal_noaccel
                change = True
        if distance & velocity_i & velocity_f:
            time_noaccel = 2*distance/(velocity_i + velocity_f)
            if time_noaccel != values["t"]:
                values["t"] = time_noaccel
                change = True

    return values
