import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

x1 = [1, 7, 11]
y1 = [2, 9, 27]

x2 = [3, 5, 8]
y2 = [2, 9, 28]

# plt.scatter(x1, y1, label = "x line", linewidth = 12)
# plt.hist(x2, label = "y line", linewidth = 4)

plt.plot(x1, y1, color = 'y', label = "x line", linewidth = 3)
plt.plot(x2, y2, color = 'b', label = "y line", linewidth = 3)

plt.title("GRAPH", color = 'r', fontsize = 20)
plt.xlabel("X-axis", color = 'g', fontsize = 16)
plt.ylabel("Y-axis", color = 'b', fontsize = 16)

plt.axis([0, 20, 0, 30])

plt.legend()

plt.grid(True, color = 'k')
plt.show()