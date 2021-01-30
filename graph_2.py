import matplotlib.pyplot as plt

# line 1
x = [1,2,3]
y = [2,4,1]
# line 2
x2 = [1,2,3]
y2 = [4,1,3]

# naming the two lines
plt.plot(x,y,label = "line1")
plt.plot(x2,y2,label = "line2")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title("2 lined graph")

plt.legend()
plt.show()