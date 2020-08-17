import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set the chart title and label axes.
ax.set_title("Square Numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0 , 1100000])

# The following line would save the plot to a file. The first argument is
#  the filename and the second trims extra whitespace from the plot.
#plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()