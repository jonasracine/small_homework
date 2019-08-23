import numpy as np
import matplotlib.pyplot as plt
pi = 3.141592653589793

x=np.linspace(-pi, pi, 100)

p1 =plt.plot(x,np.sin(x),'r-')#red line
p2 =plt.plot(x,np.cos(x),'b-')
plt.legend((p1[0], p2[0]), ('sin(x)', 'cos(x)'))
plt.xlabel('x')
plt.show()
