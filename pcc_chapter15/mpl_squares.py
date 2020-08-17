import matplotlib.pyplot as plt

x = 1
squares = []
input_values = []

# Instead of using the first 5 squares as provided in the book,
#  opted to generate the first 100 and slice the first 5.
while x < 100:
    input_values.append(x)
    squares.append(x**2)
    x += 1

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values[:5], squares[:5], linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick lables.
ax.tick_params(axis='both', labelsize=14)

plt.show()