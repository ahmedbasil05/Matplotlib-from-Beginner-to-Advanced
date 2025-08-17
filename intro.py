import matplotlib.pyplot as plt  #pyplot in built fucntions/ readymate tools

x = ["Mon","Tues","Wedn","Thurs","Fri"]
y = [15,20,11,17,30]

plt.plot(x,y)  #draw line graph
plt.title("Baker sales this week")
plt.xlabel("Day of the weeks")
plt.ylabel("No. of sales")
plt.show()