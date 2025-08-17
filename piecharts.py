# pie charts - divide into slices, each slice shows % of value
# plt.pie(values,labels=label_name,autopct='1.1f%%', color = [])
# max 5 to 6 categories

import matplotlib.pyplot as plt

regions = ["North","South","East","West"]
revenue = [3000,2000,1500,2200]

plt.pie(revenue,labels=regions,autopct='%1.1f%%', colors=["Blue","Green","Yellow","Orange"])
plt.title("Revenue Contribution by Region")
plt.show()