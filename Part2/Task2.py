import numpy as np

road_lengths = "20 8 9 18 5 12 16 16 6 7"
average_speeds = "44 70 44 66 46 38 38 37 66 67"
r_l = np.array(list(map(int, road_lengths.split())))
a_s = np.array(list(map(int, average_speeds.split())))
print(f"Road parts lengths: {road_lengths}")
print(f"Road parts average speeds: {average_speeds}")

k = int(input("Enter entrance part of road: "))
p = int(input("Enter exit part of road: "))

road = r_l[k - 1 : p]
speeds = a_s[k - 1 : p]
time = road / speeds
print(f"S = {np.sum(road)} km") 
print(f"T = {np.sum(time)} h") 
print(f"V = {np.sum(speeds) / speeds.size} km/h")