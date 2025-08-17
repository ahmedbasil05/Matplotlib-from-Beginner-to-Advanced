# plt.grid() - horizontal and vertical lines in background of plot
# optional --> plt.grid(color="Color name", linestyle ="..", linewidth = 1)

import matplotlib.pyplot as plt

months = ["Jan","Feb","March","April","May"]
sales = [1000, 1300, 800, 2000, 1500]

plt.plot(months, sales, color = "Red", marker = "D", label = "2025 sales")
plt.title("Monthly Sales Data Report")  
plt.xlabel("Months")
plt.ylabel("Sales per month")
plt.legend() 
plt.grid(color="silver",linestyle = "--", linewidth =1)  #horizontal and vertical lines in background of plot
plt.show()