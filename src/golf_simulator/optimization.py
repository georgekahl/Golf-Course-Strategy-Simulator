import time

import numpy as np

from config import (VALID_CLUBS, OPTIMIZATION_MIN_SWING, OPTIMIZATION_MAX_SWING, OPTIMIZATION_SWING_STEP, OPTIMIZATION_MIN_AIM, OPTIMIZATION_MAX_AIM, OPTIMIZATION_AIM_STEP, OPTIMIZATION_SIMULATION_RUNS)


from clubs import (get_club_parameters, get_swing_standard_deviation, get_swing_distance)

from shot_simulation import (evaluate_shots, simulate_shots)

def optimization(green, pin_position, putt_a, putt_b, putt_c):

    import time

    results = []

    swing_percentages = np.arange(OPTIMIZATION_MIN_SWING, OPTIMIZATION_MAX_SWING + OPTIMIZATION_SWING_STEP, OPTIMIZATION_SWING_STEP)
    aim_values = np.arange(OPTIMIZATION_MIN_AIM, OPTIMIZATION_MAX_AIM + OPTIMIZATION_AIM_STEP, OPTIMIZATION_AIM_STEP)

    total_combinations = (len(VALID_CLUBS) * len(swing_percentages) * len(aim_values))

    completed = 0

    start_time = time.perf_counter()

    print()
    print("========================================")
    print("          STARTING OPTIMIZATION")
    print("========================================")
    print(f"Strategies to test: {total_combinations:,}")
    print(f"Shots per strategy: {OPTIMIZATION_SIMULATION_RUNS:,}")
    print(f"Total simulated shots: " f"{total_combinations * OPTIMIZATION_SIMULATION_RUNS:,}")
    print()

    for club in VALID_CLUBS:
        average_shot, standard_deviation = get_club_parameters(club)

        for swing_percentage in swing_percentages:
            swing = swing_percentage / 100

            adjusted_standard_deviation = get_swing_standard_deviation(standard_deviation, swing)
            adjusted_distance = get_swing_distance(average_shot, swing)

            for aim in aim_values:
                aim_x = average_shot[0] + aim
                adjusted_distance[0] = aim_x
                shots_x, shots_y = simulate_shots(adjusted_distance, adjusted_standard_deviation, OPTIMIZATION_SIMULATION_RUNS)
                (average_expected_strokes,average_expected_putts,green_hit_count,chip_count,chip_green_count, chip_miss_count) = evaluate_shots(shots_x, shots_y, green, pin_position, putt_a, putt_b, putt_c)
                results.append({"club": club, "swing_percentage": swing_percentage, "aim": aim, "expected_strokes": average_expected_strokes, "expected_putts": average_expected_putts,"green_hit_percentage": green_hit_count / OPTIMIZATION_SIMULATION_RUNS * 100, "chip_success_percentage": (chip_green_count / chip_count * 100 if chip_count > 0 else 0)})

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
    print(f"Shots simulated: " f"{total_combinations * OPTIMIZATION_SIMULATION_RUNS:,}")
    print()


    return best_result, results