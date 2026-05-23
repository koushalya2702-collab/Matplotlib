#Matplotlib Pie Charts
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 

#Labels
import matplotlib.pyplot as plt
import numpy as np
y=np.array([35,25,25,15])
mylabels=["Apple","Orange","Grapes","Watermelon"]
plt.pie(y, labels=mylabels)
plt.show()

#Start Angle
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 
