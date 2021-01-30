import matplotlib.pyplot as plt

# line 1
x = [1,2,3,4,5,6]
y = [2,4,1,5,2,6]

plt.plot(x,y,label = "line1")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title("customizing graphs")

# these are for customizing the graph (line-width, line-styles, line-color etc)
plt.plot(x,y,color='green',linestyle='dashed',linewidth = 3, marker='o',markerfacecolor='blue',markersize=12)

plt.ylim(1,8)
plt.xlim(1,8)

plt.show()