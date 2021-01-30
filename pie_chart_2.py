import matplotlib.pyplot as plt

#defining different labels that would be used in the pie
activities = ['yes','no','neutral']


slices = [13,11,15]
colors = ['y','purple','c']

# this uses plt.pie instead of plt.plot or plt.bar, shadow will add a shadow under the graph labels, startangle rotates and
# tilts the graph, explode can offset a section of the graph, in this case the green section gets offset, autopct is used to
# format the value of each label, in this case we set it so it shows the percentage value up to only 1 decimal place
plt.pie(slices, labels=activities, colors=colors, startangle=270, shadow=True, explode=(0,0,0.2),radius=1.1, autopct='%2.1f%%')

plt.legend()
plt.title("do you like programming")
plt.show()