import numpy as np

from shapely.geometry import Point
from putting import(yards_to_feet, expected_putts)
from chipping import(simulate_chip_and_calculate_putt)

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

def simulate_shots(average_shot, standard_deviation, SIMULATION_RUNS):
    shots_x = np.random.normal(average_shot[0], standard_deviation[0], SIMULATION_RUNS)
    shots_y = np.random.normal(average_shot[1], standard_deviation[1], SIMULATION_RUNS)
    return shots_x, shots_y

def distance_from_pin(pin_position, shots_x, shots_y):
    distances = []
    for i in range(len(shots_x)):
        shot = Point(shots_x[i], shots_y[i])
        distance = shot.distance(pin_position)
        distances.append(distance)

    return distances

