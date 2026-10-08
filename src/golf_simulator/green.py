import random
import numpy as np

from shapely.geometry import Point, Polygon
from config import(MIN_PIN_DISTANCE_FROM_EDGE)



def rand_green_creation(MAX_DISTANCE_FROM_PIN, MIN_DISTANCE_FROM_PIN, MAX_DISTANCE_LEFT_FROM_PIN, MAX_DISTANCE_RIGHT_FROM_PIN, MIN_GREEN_WIDTH, MIN_GREEN_HEIGHT, MAX_GREEN_HEIGHT, MAX_GREEN_WIDTH, NUMBER_POINTS_ON_GREEN):
    while True:
        rand_center_of_green_y = random.randint(MIN_DISTANCE_FROM_PIN, MAX_DISTANCE_FROM_PIN)
        rand_center_of_green_x = random.randint(-MAX_DISTANCE_LEFT_FROM_PIN, MAX_DISTANCE_RIGHT_FROM_PIN)

        width = random.uniform(MIN_GREEN_WIDTH, MAX_GREEN_WIDTH)
        height = random.uniform(MIN_GREEN_HEIGHT, MAX_GREEN_HEIGHT)

        radius_x = width / 2
        radius_y = height / 2


        green_points = []

        for i in range(NUMBER_POINTS_ON_GREEN):
            angle = (2*np.pi *i) / NUMBER_POINTS_ON_GREEN

            random_radius = random.uniform(0.90, 1.10)

            x = (rand_center_of_green_x + radius_x * random_radius * np.cos(angle))
            y = (rand_center_of_green_y + radius_y * random_radius * np.sin(angle))

            green_points.append((x,y))

        green = Polygon(green_points)

        min_x, min_y, max_x, max_y = green.bounds

        actual_width = max_x - min_x
        actual_height = max_y - min_y

        if actual_width >= MIN_GREEN_WIDTH and actual_height >= MIN_GREEN_HEIGHT:
            return green

def set_pin_position(green):
    pin_area = green.buffer(-MIN_PIN_DISTANCE_FROM_EDGE)

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
