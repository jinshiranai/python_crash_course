# Try It Yourself 15-1. Cubes.

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# 15-2. Colored Cubes.
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# Set the chart title and labels.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=20)
ax.set_ylabel("Cube of Value", fontsize=20)

# Set size of tick labels.
ax. tick_params(axis='both', which='major', labelsize=14)

plt.show()