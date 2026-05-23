# #Box plot
# import matplotlib.pyplot as plt

# marks=[87,99,67,89,160]
# plt.boxplot(marks)
# plt.show()

# #Outlier Detection
# import matplotlib.pyplot as plt

# marks = [45, 50, 55, 60, 65, 70, 150]

# plt.boxplot(marks)

# plt.show()

# #Multiple Box Plot
# import matplotlib.pyplot as plt

# maths = [70, 75, 80, 85]
# science = [60, 65, 70, 90]

# plt.boxplot([maths, science])

# plt.show()

#Adding Names
import matplotlib.pyplot as plt

maths = [70, 75, 80, 85]
science = [60, 65, 70, 90]

plt.boxplot([maths, science])

# plt.xticks([1, 2], ["Maths", "Science"])

plt.show()

#Horizontal Box Plot
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 150]

plt.boxplot(marks, vert=False)

plt.show()