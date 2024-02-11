import matplotlib.pyplot as plt


# countries = ['Pakistan', 'India', 'Afghanistan', 'China', 'Iran']
# pop = [216, 1405, 39, 1414, 89]
# plt.barh(countries, pop)
# plt.xlabel("Values along x axis", fontsize = 14, color = 'g')
# plt.ylabel("Values along y axis", fontsize = 14, color = 'r')

# plt.axis([0, 15, 0, 2000])
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

BW = 0.25
wheat = [58, 70, 60, 65, 75]
rice = [35, 48, 42, 50, 65]
corn = [12, 20, 25, 35, 25]
# bar1 = np.arange(1, len(wheat)+1)
# bar1 = np.arange(len(wheat))
# bar1 = [np.arange(len(wheat))]
bar1 = [x+1 for x in range(len(wheat))]
# print(bar1)

bar2 = [x+BW for x in bar1]
# print(bar2)

bar3 = [x + BW for x in bar2]
# print(bar3)

plt.bar(bar1, wheat, width = BW, color = 'r', label = "Wheat")
plt.bar(bar2, rice, width = BW, color = 'y', label = "Rice")
plt.bar(bar3, corn, width = BW, color = 'g', label = "Corn")
# plt.legend()
# plt.show()


ticks = [r+1 + BW for r in range(len(wheat))]
print(ticks)
values = ['2015', '2016', '2017', '2018', '2019']

# plt.xticks(ticks, values, color = 'purple', fontsize = 10)
# plt.xticks(ticks, values, color = 'purple', size = 'xx-large', rotation = 135)
# plt.yticks(ticks, values, color = 'purple', size = 'xx-large', rotation = 135)

# TO DISABLE TICKS
# plt.yticks([])


# plt.grid(True)
# plt.show()

