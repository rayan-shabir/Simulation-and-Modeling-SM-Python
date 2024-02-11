import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

x1 = [1, 7, 11]
y1 = [2, 9, 27]

x2 = [3, 5, 8]
y2 = [2, 9, 28]

x3 = [1, 2, 3, 4, 5]
y3 = [5, 6, 7, 8, 9]

x4 = [1, 4, 7, 9, 10]
y4 = [2, 3, 4, 4, 8]

plt.subplot(3, 1, 1)
plt.scatter(x1, y1, label = "x ok", linewidth = 4)
plt.hist(x2, label = "y ok", linewidth = 4)

plt.axis([0, 15, 0, 30])

plt.title("GRAPH", color = 'r', fontsize = 20)

plt.subplot(3, 1, 2)
plt.plot(x1, y1, "y3:", label = "x line", linewidth = 2)
plt.plot(x2, y2, "b*--", label = "y line", linewidth = 2)

plt.axis([0, 20, 0, 30])

plt.ylabel("Y-axis", color = 'b', fontsize = 16)

plt.subplot(3, 1, 3)
plt.plot(x3, y3, color = 'y', linewidth = 1.5, label = 'x de')
plt.plot(x4, y4, "g*-.", linewidth = 2, label = 'y de')

plt.axis([0, 15, 0, 15])


plt.xlabel("X-axis", color = 'g', fontsize = 16)

plt.legend()
plt.show()