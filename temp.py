if velocity_f & acceleration & distance:

            vinitial_f = math.sqrt(velocity_f*velocity_f - 2*acceleration*distance)

            if vinitial_f != values["velocity_i"]:

                values["velocity_i"] = vinitial_f

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

            if vinitial_nod != values["velocity_i"]:

                values[velocity_i] = vinitial_nod

                change = True

        if velocity_f & velocity_i & time:

            acceleration_nod = (velocity_f - velocity_i)/time

            if acceleration_nod != values["acceleration"]

                values["acceleration"] = acceleration_nod

                change = True

        if velocity_i & velocity_f & acceleration:

            time_nod = (velocity_f - velocity_i)/acceleration

            if time_nod != values["time"]:

                values["time"] = time_nod

                change = True

        if distance & time & velocity_f:

            vinitial_noaccel = 2*distance/time - velocity_f

            if vinitial_noaccel != values["velocity_i"]:

                values["velocity_i"] = vinitial_noaccel

                change = True

        if distance & time & velocity_i:

            vfinal_noaccel = 2*distance/time - velocity_i

            if vfinal_noaccel != values[velocity_f]:

                values["velocity_f"] = vfinal_noaccel

                change = True

        if distance & velocity_i & velocity_f:

            time_noaccel = 2*distance/(velocity_i + velocity_f)

            if time_noaccel != values[time]:

                values["time"] = time_noaccel

                change = True


