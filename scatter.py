# scatter - relationship between things (x and y axis)
# plt.scatter(x,y,color = 'color', marker = 'o'. label = 'label')

import matplotlib.pyplot as plt

hours = [1,2,3,4,5,6]
scores = [50,55,60,70,80,90]

plt.scatter(hours,scores, color = 'green', marker = 'o')
plt.xlabel('Hours studied')
plt.ylabel('Exam scores')
plt.title("Relation between hours and exams scores")
plt.grid()
plt.legend()
plt.show()
