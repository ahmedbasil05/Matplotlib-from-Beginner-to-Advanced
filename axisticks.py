# plt.xticks() - meaningful labelling for x-axis
# plt.yticks() - meaningful labelling for x-axis 

import matplotlib.pyplot as plt

months = ["Jan","Feb","March","April","May"]
sales = [1000, 1300, 800, 2000, 1500]

plt.plot(months, sales, color = "Red", marker = "D", label = "2025 sales")
plt.title("Monthly Sales Data Report")  
plt.xlabel("Months")
plt.ylabel("Sales per month")
plt.legend() 
plt.grid()
plt.xlim(0,4)  
plt.ylim(500,2200)
plt.xticks([1,2,3,4],["M1","M2","M3","M4"])  
plt.show()