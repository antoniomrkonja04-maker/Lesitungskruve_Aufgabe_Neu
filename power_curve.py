import matplotlib.pyplot as plt
import csv
from load_data import load_data
from sort import bubble_sort 

x = []
y = []

data = load_data("activity.csv")
power_values = list(data["PowerOriginal"])
sorted_power_values = bubble_sort(power_values)

x_values = list(range(len(sorted_power_values)))
y_values = sorted_power_values[::-1] 

with open('activity.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots, None)  # Überspringt die erste Zeile mit den Spaltennamen
    for row in plots:
        x.append(int(row[0]))
        y.append(float(row[1]))

plt.plot(x, y, label="Power", color='red', marker='o')
plt.xlabel("Zeit(s)")
plt.ylabel("Kraft(W)")
plt.grid(True)
plt.title('Leistungskurve')
plt.legend(loc="lower right")
plt.show()