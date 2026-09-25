import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon


x_distance_middle_green = 0
y_distance_middle_green = 140


average_distance_x = 0
average_distance_y = 140
average_shot = [average_distance_x, average_distance_y]

standard_deviation_x = 5
standard_deviation_y = 3

standard_deviation = [standard_deviation_x, standard_deviation_y]

pin_Position = "front"  # Options: "front", "middle", "back"

green_radius = 15
green_points = [ (-10, 150), (5, 155), (12, 148), (10, 135), (0, 130), (-12, 135)]
green = Polygon(green_points)

simulation_runs = 1000

def distance_from_Pin(x, y, pin_Position):
    if pin_Position == "front":
        return np.sqrt(x**2 + (y - 135)**2)
    elif pin_Position == "middle":
        return np.sqrt(x**2 + (y - 140)**2)
    elif pin_Position == "back":
        return np.sqrt(x**2 + (y - 145)**2)


def check_hit_green(green):
    hits = 0
    for i in range(simulation_runs):
        point = Point(shots_x[i], shots_y[i])
        if green.contains(point):
            hits += 1
    return hits


#Simulate 1000 shots with a normal distribution
shots_x = np.random.normal(average_shot[0], standard_deviation[0], simulation_runs)
shots_y = np.random.normal(average_shot[1], standard_deviation[1], simulation_runs)

hits = check_hit_green(green)


#Print Info
print("Golf Course Strategy Simulator")
print()
print("Pitching Wedge")
print("Average simulated distance (X): ", np.mean(shots_x))
print("Standard deviation of simulated distance (X): ", np.std(shots_x))
print("Shortest shot (X): ", np.min(shots_x))
print("Longest shot (X): ", np.max(shots_x))
print()
print("Average simulated distance (Y): ", np.mean(shots_y))
print("Standard deviation of simulated distance (Y): ", np.std(shots_y))
print("Shortest shot (Y): ", np.min(shots_y))
print("Longest shot (Y): ", np.max(shots_y))
print("Number of hits: ", hits)
print("Percentage of hits: ", (hits / len(shots_x)) * 100, "%")

#Plot Distribution
green_x, green_y = green.exterior.xy
plt.scatter(shots_x, shots_y)
plt.plot(green_x, green_y, color = "green", label = "Green")
plt.xlabel("Left/Right (yards)")
plt.ylabel("Distance (yards)")
plt.title("Pitching Wedge Shot Distribution")
plt.show()