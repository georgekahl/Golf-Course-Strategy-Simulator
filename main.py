import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.optimize import curve_fit
from scipy.stats import truncnorm
from shapely.geometry import Point, Polygon


#To-do
#Add bunckers/rough
#Add Wind
#Add aim-point optimization
#Add club optimization
# build an 18 hold simulator




#Settings
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

simulation_runs = 1000

#Club data

valid_clubs = ["58 degree wedge", "54 degree wedge", "50 degree wedge", "pitching wedge", "9 iron", "8 iron", "7 iron", "6 iron", "5 iron", "4 iron", "4 hybrid", "3 wood", "driver"]

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

#Chipping data
distance_sd_less_5yd = .5
lateral_sd_less_5yd = .5

distance_sd_5yd_to_10yd = 1
lateral_sd_5yd_to_10yd = 1

distance_sd_10yd_to_20yd = 2
lateral_sd_10yd_to_20yd = 1

distance_sd_20yd_to_30yd = 3
lateral_sd_20yd_to_30yd = 1.5

distance_sd_more_30yd = 4
lateral_sd_more_30yd = 2

#Putting data
putt_lengths_ft_data = np.array([0, 3, 5, 8, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
expected_putts_data = np.array([0, 1.01, 1.12, 1.5, 1.61, 1.87, 1.98, 2.06, 2.14, 2.21, 2.27, 2.32, 2.36, 2.4])

#Optimizer Settings
optimization_min_swing = 50
optimization_max_swing = 100
optimization_swing_step = 5

optimization_min_aim = -10
optimization_max_aim = 10
optimization_aim_step = 1

optimization_simulation_runs = 500

#Green creation
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

#Pin    
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


#Club parameters
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


def ask_club_selection(valid_clubs):
    while True:
        club = input("Which club would you like to use? ")
        if club in valid_clubs:
            return club

        print("Invalid club. Please try again.")
    
#Aim
def ask_aim(average_shot):
    x_aim = float(input("Aim left/right (negative for left, positive for right) "))

    aim_x = average_shot[0] + x_aim
    return aim_x

def ask_swing_percentage():
    while True:
        swing_percentage = float(input("Swing Percentage (0-100): "))
        swing_percentage = swing_percentage/100

        if 0 < swing_percentage <= 1:
            return swing_percentage
        print("Please enter a percentage between 1 and 100.")

#Swing adjustments
def get_swing_standard_deviation(standard_deviation, swing_percentage, sd_k = 1.5):
    swing_sd_multiplier = swing_percentage ** sd_k

    adjusted_sd_x = standard_deviation[0] * swing_sd_multiplier
    adjusted_sd_y = standard_deviation[1] * swing_sd_multiplier
    return [adjusted_sd_x, adjusted_sd_y]

def get_swing_distance(average_shot, swing_percentage, d_k = 0.7):
    distance_multiplier = swing_percentage **d_k

    adjusted_x = average_shot[0]
    adjusted_y = average_shot[1] * distance_multiplier

    return [adjusted_x, adjusted_y]

#Shot simulation
def simulate_shots(average_shot, standard_deviation, simulation_runs):
    shots_x = np.random.normal(average_shot[0], standard_deviation[0], simulation_runs)
    shots_y = np.random.normal(average_shot[1], standard_deviation[1], simulation_runs)
    return shots_x, shots_y

#Distance
def distance_from_pin(pin_position, shots_x, shots_y):
    distances = []

    for i in range(len(shots_x)):
        shot = Point(shots_x[i], shots_y[i])
        distance = shot.distance(pin_position)
        distances.append(distance)
    return distances

#Putting model
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

#Chipping
def get_chip_parameters(chip_distance):
    if chip_distance <= 5:
        distance_sd = distance_sd_less_5yd
        lateral_sd = lateral_sd_less_5yd
    elif chip_distance <= 10:
        distance_sd = distance_sd_5yd_to_10yd
        lateral_sd = lateral_sd_5yd_to_10yd
    elif chip_distance <= 20:
        distance_sd = distance_sd_10yd_to_20yd
        lateral_sd = lateral_sd_10yd_to_20yd
    elif chip_distance <= 30:
        distance_sd = distance_sd_20yd_to_30yd
        lateral_sd = lateral_sd_20yd_to_30yd
    else:
        distance_sd = distance_sd_more_30yd
        lateral_sd = lateral_sd_more_30yd
    return distance_sd, lateral_sd

def simulate_chipping(shot, pin_position):
    dx = pin_position.x - shot.x
    dy = pin_position.y - shot.y

    chip_distance = np.sqrt(dx**2 + dy**2)

    if chip_distance == 0:
        return Point(pin_position.x, pin_position.y)

    distance_sd, lateral_sd = get_chip_parameters(chip_distance)

    unit_x = dx / chip_distance
    unit_y = dy / chip_distance

    perp_x = -unit_y
    perp_y = unit_x

    lower_bound = (0-chip_distance) / distance_sd
    actual_chip_distance = truncnorm.rvs(lower_bound, np.inf, loc = chip_distance, scale = distance_sd)

    
    lateral_error = np.random.normal(0,lateral_sd)

    chip_x = (shot.x + unit_x * actual_chip_distance + perp_x * lateral_error)
    chip_y = (shot.y + unit_y * actual_chip_distance + perp_y * lateral_error)

    return Point(chip_x, chip_y)

#Chip and putt
def simulate_chip_and_calculate_putt(shot, green, pin_position, a, b, c):
    chip = simulate_chipping(shot, pin_position)

    if green.contains(chip):
        chip_to_pin = chip.distance(pin_position)
        putt_distance = yards_to_feet(chip_to_pin)
        putts = expected_putts(putt_distance, a, b, c)

        expected_strokes = 2 + putts

        return chip, True, expected_strokes, putts
    else:
        return chip, False, None, None

#Evaluate simulation
def evaluate_shots(shots_x, shots_y, green, pin_position, a, b, c):
    expected_strokes = []
    expected_putts_list = []

    green_hit_count = 0
    chip_count = 0
    chip_green_count = 0
    chip_miss_count = 0

    for i in range (len(shots_x)):
        shot = Point(shots_x[i], shots_y[i])
        if green.contains(shot):
            green_hit_count += 1

            putt_distance_yards = shot.distance(pin_position)
            putt_distance_ft = yards_to_feet(putt_distance_yards)
            putts = expected_putts(putt_distance_ft, a, b, c)
            total_expected_strokes = 1 + putts

            expected_strokes.append(total_expected_strokes)
            expected_putts_list.append(putts)
        else:
            chip_count += 1

            chip, chip_hit_green, chip_expected_strokes, putts = (simulate_chip_and_calculate_putt(shot, green, pin_position, a, b, c))

            if chip_hit_green:
                chip_green_count += 1

                expected_strokes.append(chip_expected_strokes)
                expected_putts_list.append(putts)
            else:
                chip_miss_count += 1
                recovery_strokes = 2.5
                total_expected_strokes = 1 + 1 + recovery_strokes

                expected_strokes.append(total_expected_strokes)
    average_expected_strokes = np.mean(expected_strokes)

    if expected_putts_list:
        average_expected_putts = np.mean(expected_putts_list)
    else:
        average_expected_putts = 0
    return (average_expected_strokes, average_expected_putts, green_hit_count, chip_count, chip_green_count, chip_miss_count)

def optimization(green, pin_position, putt_a, putt_b, putt_c):

    import time

    results = []

    swing_percentages = np.arange(optimization_min_swing, optimization_max_swing + optimization_swing_step, optimization_swing_step)
    aim_values = np.arange(optimization_min_aim, optimization_max_aim + optimization_aim_step, optimization_aim_step)

    total_combinations = (len(valid_clubs) * len(swing_percentages) * len(aim_values))

    completed = 0

    start_time = time.perf_counter()

    print()
    print("========================================")
    print("          STARTING OPTIMIZATION")
    print("========================================")
    print(f"Strategies to test: {total_combinations:,}")
    print(f"Shots per strategy: {optimization_simulation_runs:,}")
    print(f"Total simulated shots: " f"{total_combinations * optimization_simulation_runs:,}")
    print()

    for club in valid_clubs:
        average_shot, standard_deviation = get_club_parameters(club)

        for swing_percentage in swing_percentages:
            swing = swing_percentage / 100

            adjusted_standard_deviation = get_swing_standard_deviation(standard_deviation, swing)
            adjusted_distance = get_swing_distance(average_shot, swing)

            for aim in aim_values:
                aim_x = average_shot[0] + aim
                adjusted_distance[0] = aim_x
                shots_x, shots_y = simulate_shots(adjusted_distance, adjusted_standard_deviation, optimization_simulation_runs)
                (average_expected_strokes,average_expected_putts,green_hit_count,chip_count,chip_green_count, chip_miss_count) = evaluate_shots(shots_x, shots_y, green, pin_position, putt_a, putt_b, putt_c)
                results.append({"club": club, "swing_percentage": swing_percentage, "aim": aim, "expected_strokes": average_expected_strokes, "expected_putts": average_expected_putts,"green_hit_percentage": green_hit_count / optimization_simulation_runs * 100, "chip_success_percentage": (chip_green_count / chip_count * 100 if chip_count > 0 else 0)})

                completed += 1

                if completed % 100 == 0 or completed == total_combinations:
                    elapsed = time.perf_counter() - start_time

                    progress = (completed/total_combinations)

                    percentage = progress * 100

                    estimated_total = (elapsed/progress)

                    remaining = (estimated_total - elapsed)

                    elapsed_minutes = elapsed / 60
                    remaining_minutes = remaining / 60

                    print( f"{completed:,}/{total_combinations:,} " f"({percentage:5.1f}%) | "f"Elapsed: {elapsed_minutes:5.1f} min | " f"Remaining: {remaining_minutes:5.1f} min | " f"{club}, " f"{swing_percentage:.0f}%, "f"aim {aim:+.0f}")


    best_result = min(results, key = lambda result: result ["expected_strokes"])

    total_time = time.perf_counter() - start_time

    print()
    print("=========================================")
    print("             OPTIMIZATION FINISHED")
    print("=========================================")
    print(f"Strategies tested: " f"{total_combinations:,}")
    print(f"Shots simulated: " f"{total_combinations * optimization_simulation_runs:,}")
    print()


    return best_result, results
#Plotting
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

#Results
def print_statement(club, average_expected_putts, green_hit_count, simulation_runs, chip_count, chip_green_count,chip_miss_count,average_expected_strokes):
    print()
    print("========== SIMULATION RESULTS ==========")
    print()
    print("Club:", club)
    print("Green hits:",green_hit_count,"/",simulation_runs)
    print("Green hit percentage:", (green_hit_count / simulation_runs) * 100, "%")
    print()
    print("Shots requiring a chip:", chip_count)
    print("Chips that hit the green:", chip_green_count)
    print("Chip success percentage:",(chip_green_count / chip_count * 100 if chip_count > 0 else 0),"%")
    print()
    print("Chips that missed the green:",chip_miss_count)
    print()
    print("Average expected strokes:",average_expected_strokes)
    print("Average putts after reaching green:",average_expected_putts)
    print()

def print_optimization_results(best_result):
    print()
    print()
    print("========================================")
    print("          OPTIMAL SHOT STRATEGY")
    print("========================================")
    print()

    print("Club:", best_result["club"])
    print("Swing:", f'{best_result["swing_percentage"]:.0f}%')
    print("Aim:", f'{best_result["aim"]:+.1f} yards')
    print("Expected strokes", f'{best_result["expected_strokes"]:.3f}')
    print("Expected putts:", f'{best_result["expected_putts"]:.3f}')
    print("Green hit percentage:" f'{best_result["green_hit_percentage"]:.1f}%')
    print("Chip success percentage:", f'{best_result["chip_success_percentage"]:.1f}%')
    print()
                                             
#Main

#Uncomment for repeatable sim
#np.random.seed(42)

while True:
    #build green and pin
    green = rand_green_creation(max_distance_from_pin, min_distance_from_pin, max_distance_left_from_pin, max_distance_right_from_pin, min_green_width, min_green_height, max_green_height, max_green_width, number_points_on_green)
    pin_position = set_pin_position(green)
    if pin_position is not None:
        break;

#print green
plot_green(green, pin_position)
print_green_info(green, pin_position)

a, b, c, covariance = fit_putting_model(putt_lengths_ft_data,expected_putts_data)

best_result, optimization_results = optimization(green, pin_position, a, b, c)

print_optimization_results(best_result)

club = best_result["club"]
swing_percentage = best_result["swing_percentage"] / 100
aim = best_result["aim"]

average_shot, standard_deviation = get_club_parameters(club)



adjusted_standard_deviation = get_swing_standard_deviation(standard_deviation, swing_percentage)
adjusted_distance = get_swing_distance(average_shot, swing_percentage)

aim_x = average_shot[0] + aim
adjusted_distance[0] = aim_x

#simulate shots and find greens hit/distance from pin
shots_x, shots_y = simulate_shots(adjusted_distance, adjusted_standard_deviation, simulation_runs)

(average_expected_strokes,average_expected_putts, green_hit_count, chip_count, chip_green_count, chip_miss_count) = evaluate_shots(shots_x, shots_y, green, pin_position, a, b, c)

#print results
print()
print("========== FINAL SIMULATION ==========")
print_statement(club, average_expected_putts, green_hit_count, simulation_runs, chip_count, chip_green_count, chip_miss_count, average_expected_strokes)
plot_shots(shots_x, shots_y, green, pin_position, aim_x, adjusted_distance[1])
