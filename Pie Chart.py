import matplotlib.pyplot as plot
# set up your lists
numlist = [8, 5, 6, 9]
namelist = ['Pizza', 'Tacos', 'Burgers', 'Pasta']
colorlist = ['purple', 'teal', 'green', 'orange' ]
explodelist = [0.1, 0.1, 0.1, 0.3]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.0f%%', colors=colorlist,
    	explode = explodelist, startangle = 90)
plot.axis('equal')
plot.savefig('piechart.png')
