def highest_altitude(gain):
    current_altitude = 0
    altitude_list = [0 for i in range(len(gain))]
    print(f"Altitude list: {altitude_list}")
    for k in range(len(gain)):
        altitude_list[k] = altitude_list[k - 1] + gain[k]
    altitude_list = [current_altitude] + altitude_list
    print(f"Altitude list after processing: {altitude_list}")
    return (f"Highest altitude: {max(altitude_list)}")

print(highest_altitude([-5,1,5,0,-7]))