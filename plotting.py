#plt.plot() - connect two points, line graph

import matplotlib.pyplot as plt

#plt.plot(x,y,color ="Color name",linestyle = "style", linewidth = value, marker = "o", label = "label name")

months = ["Jan","Feb","March","April","May"]
sales = [1000, 1300, 800, 2000, 1500]

plt.plot(months,sales, color = "Blue", marker = "o", label = "2025 sales")
plt.show()