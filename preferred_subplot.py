# Subplots - multiple plots in same column
#           -> compare multiple datasets, EDA, space
#           -> preferred method

# fig, ax = plt.subplots(1,2, figsize = (width,height))

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,2, figsize = (10,6))

x = [1,2,3,4]
y = [10,20,15,25]

ax[0].plot(x,y)
ax[0].set_title("Line Chart")

ax[1].bar(x,y)
ax[1].set_title('Bar Chart')

fig.suptitle('Comparison between Line and Bar Chart')
plt.tight_layout()  #used for automatic adjustments, before show
plt.show()