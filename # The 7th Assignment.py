                                    #   Name  : -     Mena Monir Helal
                                    #   Course: -       Python & AI
                                    #             The 7th Assignment (Plt - Data Visualization)

# Task No.(1) Create a line plot showing the temperature variation over a week
#             The (x-axis) should represent the days of the week
#             The (y-axis) should represent the temperature in degrees Celsius
#             Add appropriate labels and a title to the plot.

print("---/Creating a line plot showing the temperature variation over a week/---")

import matplotlib.pyplot as plt
print("importing matplotlib.pyplot as plt")
x = ["13-Jul","14-Jul","15-Jul","16-Jul","17-Jul","18-Jul"]
y = [28,28.5,30.3,28.4,34.8,30]


plt.plot(x,y, marker = 'o', linestyle = '-', color = 'b')          #linestyle = '-' straight line , '--' Dotted line
plt.title('AVG Tempeartue for this week')                                     # Name your plot
plt.xlabel('X-axis')
plt.ylabel('y-axis')
plt.show()