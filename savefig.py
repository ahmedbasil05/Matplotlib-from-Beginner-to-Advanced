# savefig() - saving visualizations
# plt.savefig('filename.extension', dpi = value, bbox_inches = 'tight')

import matplotlib.pyplot as plt

x  = [1,2,3,4]
y = [10,20,15,25]

plt.plot(x,y)
plt.title('Simple Line Chart')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.savefig('line.png', dpi = 300, bbox_inches = 'tight')
plt.show()