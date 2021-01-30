import matplotlib.pyplot as plt

# x axis values, defining the values as lists
x = [1,2,3]
# corresponding y axis values, defining the values as lists
y = [2,4,1]

# plot points
plt.plot(x,y)

# labeling both the x and y axis, if left untyped, it would be empty
plt.xlabel('x - axis')
plt.ylabel('y - axis')

# show on screen
plt.title("my first graph")
plt.show()