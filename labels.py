# plt.xlabel("text") - labelling on x-axis
# plt.ylabel("text") - labelling on y-axis

import matplotlib.pyplot as plt

months = ["Jan","Feb","March","April","May"]
sales = [1000, 1300, 800, 2000, 1500]

plt.plot(months, sales, linestyle = "--", color = "Green", marker = "o", label = "2025 sales")
plt.xlabel("Months")             #labelling on x-axis
plt.ylabel("Sales per month")    #labelling on y-axis
plt.show()