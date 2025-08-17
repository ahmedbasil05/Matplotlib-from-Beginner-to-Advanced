# plt.legend() - a small box to tell the details abouth the plot
# optional --> plt.legend(loc="upper left/bottom right", fontsize=2)

import matplotlib.pyplot as plt

months = ["Jan","Feb","March","April","May"]
sales = [1000, 1300, 800, 2000, 1500]

plt.plot(months, sales, color = "Red", marker = "D", label = "2025 sales")
plt.title("Monthly Sales Data Report")  
plt.xlabel("Months")
plt.ylabel("Sales per month")
plt.legend()  #a small box to tell the details abouth the plot
plt.show()