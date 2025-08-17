# histogram - numerical continuous data
#           - shows distibution of data by dividing into ranges
#           - groups data, shows frequency

# plt.hist(data,bins = no.of bins, color = 'color', edgecolor = 'color')

import matplotlib.pyplot as plt

scores = [45,67,89,56,78,88,92,60,74,81,59,66,75,82,90,85,70]

plt.hist(scores, bins = 5, color='yellow', edgecolor = 'orange')
plt.title('Scores distribution of students')
plt.xlabel('Score Ranges')
plt.ylabel("No. of students")
plt.show()