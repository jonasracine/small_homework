#Part 1--------------
import matplotlib.pyplot as plt
import json
with open('data.json', 'r') as f:
    data= json.load(f)
x=[]
y=[]
for element in data['values']:#100 points
    x.append(element['x'])
    y.append(element['y'])
plt.plot(x,y,'r-')#red line
plt.ylabel('y')
plt.xlabel('x')
plt.title('data')
plt.show()
#---------------------
