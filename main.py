import numpy as np
import matplotlib.pyplot as plt

#Pitching Wedge
average_distace = 140
standard_devation = 5

#Simulate 1000 shots with a normal distribution
shots = np.random.normal(average_distace, standard_devation, 1000)

#Print Info
print("Golf Course Strategy Simulator")
print()
print("Pitching Wedge")
print("Average simulated distance: ", np.mean(shots))
print("Standard deviation of simulated distance: ", np.std(shots))
print("Shortest shot: ", np.min(shots))
print("Longest shot: ", np.max(shots))

#Plot Distribution
plt.hist(shots, bins=50, edgecolor='black')

plt.title("Pitching Wedge Shot Distribution")
plt.xlabel("Distance (yards)")
plt.ylabel("Number of Shots")

plt.show()
