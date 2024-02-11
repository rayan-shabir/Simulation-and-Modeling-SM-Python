import matplotlib.pyplot as plt

places = ['BARKAT MARKET', 'GUJRAT', 'LAHORE', 'PUCIT']
demand = [10, 20, 30, 40]

plt.bar(places, demand, color = 'r')

plt.xlabel("STRAWBERRY", fontsize = 14, color = 'b')
plt.ylabel("FANS", fontsize = 14, color = 'g')

plt.title("STRAWBERRY'S DEMAND", fontsize = 20, color = 'r')
plt.show()