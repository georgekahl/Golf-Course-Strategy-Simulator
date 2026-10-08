import numpy as np

from scipy.stats import truncnorm
from shapely.geometry import Point

from config import (DISTANCE_SD_LESS_5YD, LATERAL_SD_LESS_5YD, DISTANCE_SD_5YD_TO_10YD, LATERAL_SD_5YD_TO_10YD, DISTANCE_SD_10YD_TO_20YD, LATERAL_SD_10YD_TO_20YD, DISTANCE_SD_20YD_TO_30YD, LATERAL_SD_20YD_TO_30YD, DISTANCE_SD_MORE_30YD, LATERAL_SD_MORE_30YD)

from putting import (yards_to_feet,expected_putts)

#Chipping
def get_chip_parameters(chip_distance):
    if chip_distance <= 5:
        distance_sd = DISTANCE_SD_LESS_5YD
        lateral_sd = LATERAL_SD_LESS_5YD
    elif chip_distance <= 10:
        distance_sd = DISTANCE_SD_5YD_TO_10YD
        lateral_sd = LATERAL_SD_5YD_TO_10YD
    elif chip_distance <= 20:
        distance_sd = DISTANCE_SD_10YD_TO_20YD
        lateral_sd = LATERAL_SD_10YD_TO_20YD
    elif chip_distance <= 30:
        distance_sd = DISTANCE_SD_20YD_TO_30YD
        lateral_sd = LATERAL_SD_20YD_TO_30YD
    else:
        distance_sd = DISTANCE_SD_MORE_30YD
        lateral_sd = LATERAL_SD_MORE_30YD
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