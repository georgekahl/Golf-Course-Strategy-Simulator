import numpy as np
import matplotlib.pyplot as plt
import random
from shapely.geometry import Point, Polygon

green_points = [ (-10, 150), (5, 155), (12, 148), (10, 135), (0, 130), (-12, 135)]
green = Polygon(green_points)
min_pin_distance_from_edge = 5

average_distance_x = 0
average_distance_y = 140
average_shot = [average_distance_x, average_distance_y]

standard_deviation_x = 5
standard_deviation_y = 3

standard_deviation = [standard_deviation_x, standard_deviation_y]

simulation_runs = 1000

def set_pin_position(green):
    pin_area = green.buffer(-min_pin_distance_from_edge)
    min_x, min_y, max_x, max_y = pin_area.bounds

    while True:
        x_pin_position = np.random.uniform(min_x, max_x)
        y_pin_position = np.random.uniform(min_y, max_y)

        pin_position = Point(x_pin_position, y_pin_position)


        if pin_area.contains(pin_position):
            return pin_position

def simulate_shots():
    shots_x = np.random.normal(average_shot[0], standard_deviation[0], simulation_runs)
    shots_y = np.random.normal(average_shot[1], standard_deviation[1], simulation_runs)
    return shots_x, shots_y

def distance_from_pin(pin_position, shots_x, shots_y):
    distances = []
    print("Pin Position: ", pin_position)
    for i in range(len(shots_x)):
        shot = Point(shots_x[i], shots_y[i])
        distance = shot.distance(pin_position)
        distances.append(distance)
    return distances

def check_hit_green(green, shots_x, shots_y):
    hits = 0
    for i in range(len(shots_x)):
        shot = Point(shots_x[i], shots_y[i])
        if green.contains(shot):
            hits += 1
    return hits

def plot_shots(shots_x, shots_y, green, pin_position):
    green_x, green_y = green.exterior.xy
    plt.scatter(shots_x, shots_y, label = "Shots", alpha = 0.5)
    plt.fill(green_x, green_y, color = "green", alpha = 0.3)
    plt.plot(green_x, green_y, color = "green", label = "Green")
    plt.scatter(pin_position.x, pin_position.y, color = "red", marker = "X", s = 100, label = "Pin")

    plt.xlabel("Left/Right (yards)")
    plt.ylabel("Distance (yards)")
    plt.title("Pitching Wedge Shot Distribution")

    plt.legend()

    plt.show()

def print_statment(shots_x, shots_y, hits, pin_position, distances):
    print("Golf Course Strategy Simulator")
    print()
    print("Pitching Wedge")
    print("-------------------------")
    print("Pin Position:", f"({pin_position.x:.2f}, {pin_position.y:.2f})")
    print()
    print("Average simulated distance (X): ", np.mean(shots_x))
    print("Standard deviation of simulated distance (X): ", np.std(shots_x))
    print("Furthest shot left (X): ", np.min(shots_x))
    print("Furthest shot right (X): ", np.max(shots_x))
    print()
    print("Average simulated distance (Y): ", np.mean(shots_y))
    print("Standard deviation of simulated distance (Y): ", np.std(shots_y))
    print("Shortest shot (Y): ", np.min(shots_y))
    print("Longest shot (Y): ", np.max(shots_y))
    print()
    print("Number of hits: ", hits)
    print("Percentage of hits: ", (hits / len(shots_x)) * 100, "%")
    print()
    print("Average distance from pin: ", np.mean(distances), "yards")
    print("Closest shot to pin: ", np.min(distances), "yards")
    print("Farthest shot from pin: ", np.max(distances), "yards")

pin_position = set_pin_position(green)
shots_x, shots_y = simulate_shots()
hits = check_hit_green(green, shots_x, shots_y)
distances = distance_from_pin(pin_position, shots_x, shots_y)
print_statment(shots_x, shots_y, hits, pin_position, distances)
plot_shots(shots_x, shots_y, green, pin_position)
