import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.optimize import curve_fit
from shapely.geometry import Point, Polygon


max_distance_from_pin = 260
min_distance_from_pin = 100

max_distance_left_from_pin = 15
max_distance_right_from_pin = 15

min_green_height = 30
min_green_width = 30
max_green_height = 50
max_green_width = 45

number_points_on_green = 40

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


putt_lengths_ft_data = np.array([0, 3, 5, 8, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
expected_putts_data = np.array([0, 1.01, 1.12, 1.5, 1.61, 1.87, 1.98, 2.06, 2.14, 2.21, 2.27, 2.32, 2.36, 2.4])











simulation_runs = 1000

def rand_green_creation(max_distance_from_pin, min_distance_from_pin, max_distance_left_from_pin, max_distance_right_from_pin, min_green_width, min_green_height, max_green_height, max_green_width, number_points_on_green):
    while True:
        rand_center_of_green_y = random.randint(min_distance_from_pin, max_distance_from_pin)
        rand_center_of_green_x = random.randint(-max_distance_left_from_pin, max_distance_right_from_pin)

        width = random.uniform(min_green_width, max_green_width)
        height = random.uniform(min_green_height, max_green_height)

        radius_x = width / 2
        radius_y = height / 2


        green_points = []

        for i in range(number_points_on_green):
            angle = (2*np.pi *i) / number_points_on_green

            random_radius = random.uniform(0.90, 1.10)

            x = (rand_center_of_green_x + radius_x * random_radius * np.cos(angle))
            y = (rand_center_of_green_y + radius_y * random_radius * np.sin(angle))

            green_points.append((x,y))

        green = Polygon(green_points)

        min_x, min_y, max_x, max_y = green.bounds

        actual_width = max_x - min_x
        actual_height = max_y - min_y

        if actual_width >= min_green_width and actual_height >= min_green_height:
            return green
        
def set_pin_position(green):
    pin_area = green.buffer(-min_pin_distance_from_edge)

    if pin_area.is_empty:
        return None

    min_x, min_y, max_x, max_y = pin_area.bounds

    while True:
        x_pin_position = np.random.uniform(min_x, max_x)
        y_pin_position = np.random.uniform(min_y, max_y)

        pin_position = Point(x_pin_position, y_pin_position)


        if pin_area.contains(pin_position):
            return pin_position

def print_green_info(green, pin_position):
    print("Green Coordinates: ", list(green.exterior.coords))
    print("Pin Position: ", f"({pin_position.x:.2f}, {pin_position.y:.2f})")

def get_club_parameters(club):
    match club:
        case "58 degree wedge":
            average_shot = average_shot_58degreeWedge
            standard_deviation = standard_deviation_58degreeWedge
            return average_shot, standard_deviation
        case "54 degree wedge":
            average_shot = average_shot_54degreeWedge
            standard_deviation = standard_deviation_54degreeWedge
            return average_shot, standard_deviation
        case "50 degree wedge":
            average_shot = average_shot_50degreeWedge
            standard_deviation = standard_deviation_50degreeWedge
            return average_shot, standard_deviation
        case "pitching wedge":
            average_shot = average_shot_pitchingWedge
            standard_deviation = standard_deviation_pitchingWedge
            return average_shot, standard_deviation
        case "9 iron":
            average_shot = average_shot_9iron
            standard_deviation = standard_deviation_9iron
            return average_shot, standard_deviation
        case "8 iron":
            average_shot = average_shot_8iron
            standard_deviation = standard_deviation_8iron
            return average_shot, standard_deviation
        case "7 iron":
            average_shot = average_shot_7iron
            standard_deviation = standard_deviation_7iron
            return average_shot, standard_deviation
        case "6 iron":
            average_shot = average_shot_6iron
            standard_deviation = standard_deviation_6iron
            return average_shot, standard_deviation
        case "5 iron":
            average_shot = average_shot_5iron
            standard_deviation = standard_deviation_5iron
            return average_shot, standard_deviation
        case "4 iron":
            average_shot = average_shot_4iron
            standard_deviation = standard_deviation_4iron
            return average_shot, standard_deviation
        case "4 hybrid":
            average_shot = average_shot_4hybrid
            standard_deviation = standard_deviation_4hybrid
            return average_shot, standard_deviation
        case "3 wood":
            average_shot = average_shot_3wood
            standard_deviation = standard_deviation_3wood
            return average_shot, standard_deviation
        case "driver":
            average_shot = average_shot_driver
            standard_deviation = standard_deviation_driver
            return average_shot, standard_deviation

def ask_club_selection():
    club = input("Which club would you like to use?")
    return club

def ask_aim(average_shot):
    x_aim = float(input("Aim left/right (negative for left, positive for right)"))
    y_aim = float(input("Aim short/long"))
    aim_x = average_shot[0] + x_aim
    aim_y = average_shot[1] + y_aim
    return [aim_x, aim_y]

def simulate_shots(average_shot, standard_deviation):
    shots_x = np.random.normal(average_shot[0], standard_deviation[0], simulation_runs)
    shots_y = np.random.normal(average_shot[1], standard_deviation[1], simulation_runs)
    return shots_x, shots_y

def distance_from_pin(pin_position, shots_x, shots_y):
    distances = []

    for i in range(len(shots_x)):
        shot = Point(shots_x[i], shots_y[i])
        distance = shot.distance(pin_position)
        distances.append(distance)
    return distances

def check_hit_green(green, shots_x, shots_y, index):
    shot = Point(shots_x[index], shots_y[index])
    if green.contains(shot):
        return True
    return False

def count_greens_hit(green, shots_x, shots_y):
    hits = 0
    for i in range(len(shots_x)):
        shot = Point(shots_x[i], shots_y[i])
        if green.contains(shot):
            hits += 1
    return hits

def yards_to_feet(distance):
    return distance*3

def expected_putts_model(x, a, b, c):
    return a * ((x+b)**c - b**c)

def expected_putts(distance, a, b, c):
    return expected_putts_model(distance, a, b, c)

def fit_putting_model(putt_lengths_ft_data, expected_putts_data):
    params, covariance = curve_fit(expected_putts_model,putt_lengths_ft_data, expected_putts_data, p0 = [0.5, 1, 0.5], bounds = (0, np.inf), maxfev=100000)
    a, b, c, = params
    return a, b, c, covariance

def average_putts_for_green_hit(green, shots_x, shots_y, distances, a, b, c):
    expected_putts_for_hits = []

    for i in range(len(shots_x)):
        if check_hit_green(green, shots_x, shots_y, i):
            putt_in_ft = yards_to_feet(distances[i])
            putts = expected_putts(putt_in_ft, a, b, c)
            expected_putts_for_hits.append(putts)

    if expected_putts_for_hits:
        average_expected_putts = np.mean(expected_putts_for_hits)
        return average_expected_putts
    else:
        return 0


def plot_green(green, pin_position):
    green_x, green_y = green.exterior.xy
    plt.fill(green_x, green_y, color = "green", alpha = 0.3)
    plt.plot(green_x, green_y, color = "green", label = "Green")
    plt.scatter(pin_position.x, pin_position.y, color = "red", marker = "X", s = 100, label = "Pin")
    plt.xlabel("Left/Right (yards)")
    plt.ylabel("Distance (yards)")
    plt.title("Shot Distribution")
    
    plt.legend()
    
    plt.show()

def plot_shots(shots_x, shots_y, green, pin_position, aim_x, aim_y):
    green_x, green_y = green.exterior.xy
    plt.scatter(shots_x, shots_y, label = "Shots", alpha = 0.5)
    plt.fill(green_x, green_y, color = "green", alpha = 0.3)
    plt.plot(green_x, green_y, color = "green", label = "Green")
    plt.scatter(pin_position.x, pin_position.y, color = "red", marker = "X", s = 100, label = "Pin")
    plt.scatter(aim_x, aim_y, color = "blue", marker = "o", s = 100, label = "Aim")

    plt.xlabel("Left/Right (yards)")
    plt.ylabel("Distance (yards)")
    plt.title("Shot Distribution")

    plt.legend()

    plt.show()

def print_statment(shots_x, shots_y, hits, pin_position, distances, club, average_expected_putts):
    print("Golf Course Strategy Simulator")
    print()
    print(club)
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
    print("Average putts for balls that hit the green: " ,average_expected_putts)





while True:
    #build green and pin
    green = rand_green_creation(max_distance_from_pin, min_distance_from_pin, max_distance_left_from_pin, max_distance_right_from_pin, min_green_width, min_green_height, max_green_height, max_green_width, number_points_on_green)
    pin_position = set_pin_position(green)
    if pin_position is not None:
        break;

#print green
plot_green(green, pin_position)
print_green_info(green, pin_position)

#ask club and aim
club = ask_club_selection()
average_shot, standard_deviation = get_club_parameters(club)
average_shot = ask_aim(average_shot)

#simulate shots and find greens hit/distance from pin
shots_x, shots_y = simulate_shots(average_shot, standard_deviation)
hits = count_greens_hit(green, shots_x, shots_y)
distances = distance_from_pin(pin_position, shots_x, shots_y)

#Fit putting model
a, b, c, covariance = fit_putting_model(putt_lengths_ft_data, expected_putts_data)

#Calculate average expected putts for shots that hit the green
average_expected_putts = average_putts_for_green_hit(green, shots_x, shots_y, distances, a, b, c)

#print results
print_statment(shots_x, shots_y, hits, pin_position, distances, club, average_expected_putts)
plot_shots(shots_x, shots_y, green, pin_position, average_shot[0], average_shot[1])
