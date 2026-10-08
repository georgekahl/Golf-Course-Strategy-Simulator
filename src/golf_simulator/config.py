import numpy as np

#To-do
#Add bunckers/rough
#Add Wind
#Add aim-point optimization
#Add club optimization
# build an 18 hold simulator
#Settings
MAX_DISTANCE_FROM_PIN = 260
MIN_DISTANCE_FROM_PIN = 100

MAX_DISTANCE_LEFT_FROM_PIN = 15
MAX_DISTANCE_RIGHT_FROM_PIN = 15

MIN_GREEN_HEIGHT = 30
MIN_GREEN_WIDTH = 30
MAX_GREEN_HEIGHT = 50
MAX_GREEN_WIDTH = 45

NUMBER_POINTS_ON_GREEN = 40

MIN_PIN_DISTANCE_FROM_EDGE = 5

SIMULATION_RUNS = 1000

#Club data
VALID_CLUBS = ["58 degree wedge", "54 degree wedge", "50 degree wedge", "pitching wedge", "9 iron", "8 iron", "7 iron", "6 iron", "5 iron", "4 iron", "4 hybrid", "3 wood", "driver"]

CLUB_DATA = {

    "58 degree wedge": {
        "average_shot": [0, 100],
        "standard_deviation": [2, 1]
    },

    "54 degree wedge": {
        "average_shot": [0, 110],
        "standard_deviation": [3, 1]
    },

    "50 degree wedge": {
        "average_shot": [0, 120],
        "standard_deviation": [4, 2]
    },

    "pitching wedge": {
        "average_shot": [0, 140],
        "standard_deviation": [5, 3]
    },

    "9 iron": {
        "average_shot": [0, 150],
        "standard_deviation": [6, 4]
    },

    "8 iron": {
        "average_shot": [0, 160],
        "standard_deviation": [7, 5]
    },

    "7 iron": {
        "average_shot": [0, 170],
        "standard_deviation": [8, 6]
    },

    "6 iron": {
        "average_shot": [0, 180],
        "standard_deviation": [9, 7]
    },

    "5 iron": {
        "average_shot": [0, 190],
        "standard_deviation": [10, 8]
    },

    "4 iron": {
        "average_shot": [0, 200],
        "standard_deviation": [11, 9]
    },

    "4 hybrid": {
        "average_shot": [0, 220],
        "standard_deviation": [12, 10]
    },

    "3 wood": {
        "average_shot": [0, 240],
        "standard_deviation": [13, 11]
    },

    "driver": {
        "average_shot": [0, 260],
        "standard_deviation": [14, 12]
    }
}

#Chipping data
DISTANCE_SD_LESS_5YD = .5
LATERAL_SD_LESS_5YD = .5

DISTANCE_SD_5YD_TO_10YD = 1
LATERAL_SD_5YD_TO_10YD = 1

DISTANCE_SD_10YD_TO_20YD = 2
LATERAL_SD_10YD_TO_20YD = 1

DISTANCE_SD_20YD_TO_30YD = 3
LATERAL_SD_20YD_TO_30YD = 1.5

DISTANCE_SD_MORE_30YD = 4
LATERAL_SD_MORE_30YD = 2

#Putting data
PUTT_LENGTHS_FT_DATA = np.array([0, 3, 5, 8, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
EXPECTED_PUTTS_DATA = np.array([0, 1.01, 1.12, 1.5, 1.61, 1.87, 1.98, 2.06, 2.14, 2.21, 2.27, 2.32, 2.36, 2.4])

#Optimizer Settings
OPTIMIZATION_MIN_SWING = 50
OPTIMIZATION_MAX_SWING = 100
OPTIMIZATION_SWING_STEP = 5

OPTIMIZATION_MIN_AIM = -10
OPTIMIZATION_MAX_AIM = 10
OPTIMIZATION_AIM_STEP = 1

OPTIMIZATION_SIMULATION_RUNS = 500