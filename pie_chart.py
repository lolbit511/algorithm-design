import matplotlib.pyplot as plt

#defining different labels that would be used in the pie
activities = ['eat','sleep','work','play']


slices = [3,7,8,6]
colors = ['r','y','g','b']

# this uses plt.pie instead of plt.plot or plt.bar, shadow will add a shadow under the graph labels, startangle rotates and
# tilts the graph, explode can offset a section of the graph, in this case the green section gets offset, autopct is used to
# format the value of each label, in this case we set it so it shows the percentage value up to only 1 decimal place
plt.pie(slices, labels=activities, colors=colors, startangle=90, shadow=True, explode=(0,0,0.1,0),radius=1.2, autopct='%1.1f%%')

plt.legend()

plt.show()