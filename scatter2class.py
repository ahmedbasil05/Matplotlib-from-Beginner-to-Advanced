# multiple scatter plots
# multiple plots/data in a single figure

import matplotlib.pyplot as plt

plt.scatter([1,2,3],[50,55,60], color = 'green', marker = 's', label = 'A')
plt.scatter([1,2,3],[43,51,64], color = 'red', marker = 'o', label = 'B')

plt.xlabel('Hours studied')
plt.ylabel('Exam scores')
plt.title("Comparison between two classes")
plt.grid()
plt.legend()
plt.show()