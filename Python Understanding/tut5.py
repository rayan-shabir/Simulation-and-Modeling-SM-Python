import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

s = 2

months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July']
farenhite = [26.4, 28, 35.8, 46.6, 56.3, 65.8, 71.2]
cel = np.arange(1, 8)
celcius = [(r**s)+1 for r in range(7)]

# print(cel)

plt.plot(farenhite, months, "r*--", linewidth = 2, label = 'Farenhite')
plt.scatter(celcius, months, color = 'blue', linewidth = 2, label = 'Celcius')

plt.title("AVERAGE MONTHLY TEMPERATURE", color = 'purple', fontsize = 24)
plt.xlabel("Temperature", color = 'yellow', size = 16)
plt.ylabel("Months", color = 'brown', size = 16)

plt.xlim([0, 100])

# plt.xticks(cel, ["a", "b", "c", "d", "e", "f", "g"])


plt.legend()
plt.show()