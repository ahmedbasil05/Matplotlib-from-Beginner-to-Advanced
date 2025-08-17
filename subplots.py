# Subplots - multiple plots in same column
#           -> compare multiple datasets, EDA, space

# plt.subplot(nrows,ncols,index)

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]

plt.subplot(1,2,1) #first row, second column, first index(subplot)
plt.plot(x,y)
plt.title('Line Chart')

plt.subplot(1,2,2) #first row, second column, second index(subplot)
plt.bar(x,y)
plt.title('Bar Chart')

plt.show()