import numpy as np
import matplotlib.pyplot as plt
import random
from shapely.geometry import Point, Polygon

green_points = [ (-10, 150), (5, 155), (12, 148), (10, 135), (0, 130), (-12, 135)]
green = Polygon(green_points)
min_pin_distance_from_edge = 5


average_distance_x_58degreeWedge = 0
average_distance_y_58degreeWedge = 100
average_shot_58degreeWedge = [average_distance_x_58degreeWedge, average_distance_y_58degreeWedge]
standard_deviation_x_58degreeWedge = 2
standard_deviation_y_58degreeWedge = 1
standard_deviation_58degreeWedge = [standard_deviation_x_58degreeWedge, standard_deviation_y_58degreeWedge]

average_distance_x_54degreeWedge = 0
average_distance_y_54degreeWedge = 110
average_shot_54degreeWedge = [average_distance_x_54degreeWedge, average_distance_y_54degreeWedge]
standard_deviation_x_54degreeWedge = 3
standard_deviation_y_54degreeWedge = 1
standard_deviation_54degreeWedge = [standard_deviation_x_54degreeWedge, standard_deviation_y_54degreeWedge]

average_distance_x_50degreeWedge = 0
average_distance_y_50degreeWedge = 120
average_shot_50degreeWedge = [average_distance_x_50degreeWedge, average_distance_y_50degreeWedge]
standard_deviation_x_50degreeWedge = 4
standard_deviation_y_50degreeWedge = 2
standard_deviation_50degreeWedge = [standard_deviation_x_50degreeWedge, standard_deviation_y_50degreeWedge]

average_distance_x_pitchingWedge = 0
average_distance_y_pitchingWedge = 140
average_shot_pitchingWedge = [average_distance_x_pitchingWedge, average_distance_y_pitchingWedge]
standard_deviation_x_pitchingWedge = 5
standard_deviation_y_pitchingWedge = 3
standard_deviation_pitchingWedge = [standard_deviation_x_pitchingWedge, standard_deviation_y_pitchingWedge]

average_distance_x_9iron = 0
average_distance_y_9iron = 150
average_shot_9iron = [average_distance_x_9iron, average_distance_y_9iron]
standard_deviation_x_9iron = 6
standard_deviation_y_9iron = 4
standard_deviation_9iron = [standard_deviation_x_9iron, standard_deviation_y_9iron]

average_distance_x_8iron = 0
average_distance_y_8iron = 160
average_shot_8iron = [average_distance_x_8iron, average_distance_y_8iron]
standard_deviation_x_8iron = 7
standard_deviation_y_8iron = 5
standard_deviation_8iron = [standard_deviation_x_8iron, standard_deviation_y_8iron]

average_distance_x_7iron = 0
average_distance_y_7iron = 170
average_shot_7iron = [average_distance_x_7iron, average_distance_y_7iron]
standard_deviation_x_7iron = 8
standard_deviation_y_7iron = 6
standard_deviation_7iron = [standard_deviation_x_7iron, standard_deviation_y_7iron]

average_distance_x_6iron = 0
average_distance_y_6iron = 180
average_shot_6iron = [average_distance_x_6iron, average_distance_y_6iron]
standard_deviation_x_6iron = 9
standard_deviation_y_6iron = 7
standard_deviation_6iron = [standard_deviation_x_6iron, standard_deviation_y_6iron]

average_distance_x_5iron = 0
average_distance_y_5iron = 190
average_shot_5iron = [average_distance_x_5iron, average_distance_y_5iron]
standard_deviation_x_5iron = 10
standard_deviation_y_5iron = 8
standard_deviation_5iron = [standard_deviation_x_5iron, standard_deviation_y_5iron]

average_distance_x_4iron = 0
average_distance_y_4iron = 200
average_shot_4iron = [average_distance_x_4iron, average_distance_y_4iron]
standard_deviation_x_4iron = 11
standard_deviation_y_4iron = 9
standard_deviation_4iron = [standard_deviation_x_4iron, standard_deviation_y_4iron]

average_distance_x_4hybrid = 0
average_distance_y_4hybrid = 220
average_shot_4hybrid = [average_distance_x_4hybrid, average_distance_y_4hybrid]
standard_deviation_x_4hybrid = 12
standard_deviation_y_4hybrid = 10
standard_deviation_4hybrid = [standard_deviation_x_4hybrid, standard_deviation_y_4hybrid]

average_distance_x_3wood = 0
average_distance_y_3wood = 240
average_shot_3wood = [average_distance_x_3wood, average_distance_y_3wood]
standard_deviation_x_3wood = 13
standard_deviation_y_3wood = 11
standard_deviation_3wood = [standard_deviation_x_3wood, standard_deviation_y_3wood]

average_distance_x_driver = 0
average_distance_y_driver = 260
average_shot_driver = [average_distance_x_driver, average_distance_y_driver]
standard_deviation_x_driver = 14
standard_deviation_y_driver = 12
standard_deviation_driver = [standard_deviation_x_driver, standard_deviation_y_driver]



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
