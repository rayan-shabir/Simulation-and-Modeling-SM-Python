import matplotlib.pyplot as plt
from matplotlib import style
import  numpy as np

r1 = [r+1 for r in range(8)]
r2 = np.arange(1, 8+1)
ownShip = [8000, 1500, 1300, 1000, 900]
pets = ['F', 'R', 'T', 'P', 'H']

# print(r1)
# print(r2)
# print(len(pets))

plt.bar(pets, ownShip, color = 'red', width = 0.5)
plt.title("PETS OWNSHOP CHART", color = 'black', fontsize = 22)
plt.xlabel("PETS", color = 'red', size = 14)
plt.ylabel("OWNING", color = 'green', size = 14)

plt.xticks(range(len(pets)), ["Fish", "Rabbits", "Turtle", "Poultry", "Hamsters"], color = 'grey')
plt.yticks(range(len(ownShip)), ["a", "b", "c", "d", "e"])

plt.grid()
plt.show()

