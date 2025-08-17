# plt.lim() - range 
# plt.xlim() - range for x-axis
# plt.ylim() - range for y-axis

import matplotlib.pyplot as plt

months = ["Jan","Feb","March","April","May"]
sales = [1000, 1300, 800, 2000, 1500]

plt.plot(months, sales, color = "Red", marker = "D", label = "2025 sales")
plt.title("Monthly Sales Data Report")  
plt.xlabel("Months")
plt.ylabel("Sales per month")
plt.legend() 
plt.grid()
plt.xlim(0,4)  #sets the range for x-axis
plt.ylim(500,2200)  #sets the range for y-axis
plt.show()