#Lab1
'''
import geopy.distance

cars = [ 
    [30.0550629,31.0404102],
    [30.0072457,30.9728776],
    [30.0445439,31.2330771]
]

client_location = [30.063249588012695,31.24689292907715]
best_car_distance = 99999999999999999
target_car_index = -1

for i in range(len(cars)):
    distance = geopy.distance.geodesic(client_location,cars[i]).km
    if distance < best_car_distance :
        best_car_distance = distance
        target_car_index = i

print(best_car_distance,target_car_index)
'''

#Lab2
'''
d = [ 4, -5, 50]
result = 9999999999999999

for i in range(len(d)):
    if d[i] < result:
        result = d[i]
print(result)
'''

