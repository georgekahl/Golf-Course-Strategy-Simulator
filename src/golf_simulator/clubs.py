from config import(CLUB_DATA, VALID_CLUBS)


#Club parameters
def get_club_parameters(club):
    club_data = CLUB_DATA[club]

    average_shot = club_data["average_shot"]
    standard_deviation = club_data["standard_deviation"]

    return average_shot, standard_deviation

def ask_club_selection(VALID_CLUBS):
    while True:
        club = input("Which club would you like to use? ")
        if club in VALID_CLUBS:
            return club

        print("Invalid club. Please try again.")

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



