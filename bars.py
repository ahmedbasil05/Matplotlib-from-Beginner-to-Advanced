# bars - comparison between groups using bars
# plt.bar(x,height, color = 'color', label = 'label', width =  value)
# length is directily proportional to value

import matplotlib.pyplot as plt

product = ["A","B","C","D","E"]
sales = [1000,1500,1200,800,1400]

plt.barh(product,sales, color = 'yellow', label = ' Sales ')
plt.title("Product Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.legend()
plt.show()