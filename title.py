# plt.title("text") - gives a description/ title to the plot

import matplotlib.pyplot as plt

months = ["Jan","Feb","March","April","May"]
sales = [1000, 1300, 800, 2000, 1500]

plt.plot(months, sales, color = "Red", marker = "D", label = "2025 sales")
plt.title("Monthly Sales Data Report")  #gives a description/ title to the plot
plt.xlabel("Months")
plt.ylabel("Sales per month")
plt.show()