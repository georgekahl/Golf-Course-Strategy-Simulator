import numpy as np
from config import (SIMULATION_RUNS, PUTT_LENGTHS_FT_DATA, EXPECTED_PUTTS_DATA, MAX_DISTANCE_FROM_PIN, MIN_DISTANCE_FROM_PIN, MAX_DISTANCE_LEFT_FROM_PIN, MAX_DISTANCE_RIGHT_FROM_PIN, MIN_GREEN_WIDTH, MIN_GREEN_HEIGHT, MAX_GREEN_HEIGHT, MAX_GREEN_WIDTH, NUMBER_POINTS_ON_GREEN)

from green import (rand_green_creation, set_pin_position, print_green_info)

from putting import fit_putting_model

from optimization import optimization

from clubs import (get_club_parameters, get_swing_standard_deviation, get_swing_distance)

from shot_simulation import (evaluate_shots, simulate_shots)

from plotting import (plot_green,plot_shots)

from output import (print_statement, print_optimization_results)


# Uncomment for repeatable simulations
# np.random.seed(42)
def main():
    while True:
        #build green and pin
        green = rand_green_creation(MAX_DISTANCE_FROM_PIN, MIN_DISTANCE_FROM_PIN, MAX_DISTANCE_LEFT_FROM_PIN, MAX_DISTANCE_RIGHT_FROM_PIN, MIN_GREEN_WIDTH, MIN_GREEN_HEIGHT, MAX_GREEN_HEIGHT, MAX_GREEN_WIDTH, NUMBER_POINTS_ON_GREEN)
        pin_position = set_pin_position(green)
        if pin_position is not None:
            break;

    #print green
    plot_green(green, pin_position)
    print_green_info(green, pin_position)

    a, b, c, covariance = fit_putting_model(PUTT_LENGTHS_FT_DATA,EXPECTED_PUTTS_DATA)

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
    shots_x, shots_y = simulate_shots(adjusted_distance, adjusted_standard_deviation, SIMULATION_RUNS)

    (average_expected_strokes,average_expected_putts, green_hit_count, chip_count, chip_green_count, chip_miss_count) = evaluate_shots(shots_x, shots_y, green, pin_position, a, b, c)

    #print results
    print()
    print("========== FINAL SIMULATION ==========")
    print_statement(club, average_expected_putts, green_hit_count, SIMULATION_RUNS, chip_count, chip_green_count, chip_miss_count, average_expected_strokes)
    plot_shots(shots_x, shots_y, green, pin_position, aim_x, adjusted_distance[1])

main()