import matplotlib.pyplot as plt

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