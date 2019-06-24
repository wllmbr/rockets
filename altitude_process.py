import blur
import flight_data

def derive(s, dt):
    ds = [0]
    for i in range(1,len(s)):
        ds.append((s[i] - s[i-1]) / dt)
    return ds

smoothed_altitude = blur.smooth_set(flight_data.raw_altitude, 19)

#Get the double derivative of the altitude so we can smooth accel as well

estimated_velocity = derive(smoothed_altitude,0.05)
smoothed_velocity = blur.smooth_set(estimated_velocity, 19)

estimated_acceleration = derive(smoothed_velocity,0.05)
smoothed_acceleration = blur.smooth_set(estimated_acceleration, 19)

with open("smoothed_altitude",'w') as file_handle:
    for element in smoothed_altitude:
        file_handle.write(str(element))
        file_handle.write("\n")

with open("smoothed_velocity",'w') as file_handle:
    for element in smoothed_velocity:
        file_handle.write(str(element))
        file_handle.write("\n")

with open("smoothed_acceleration",'w') as file_handle:
    for element in smoothed_acceleration:
        file_handle.write(str(element))
        file_handle.write("\n")