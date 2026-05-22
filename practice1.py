#Matplotlib Line
import matplotlib.pyplot as plt
import numpy as np

y=np.array([3,8,1,10])
plt.plot(y,linestyle='dotted')
plt.show()

#Example
import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10])
plt.plot(ypoints,linestyle='dashed')
plt.show()

#Line Color
import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10])
plt.plot(ypoints,color='r')
plt.show()

#Line Width
import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,8,1,10])
plt.plot(ypoints,linewidth='20.5')
plt.show()

#Multiple Lines
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()