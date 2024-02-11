import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4])
# plt.show()


#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = [x+1 for x in range(15)]

# print(x)

# # print(x)

y = [y**2 for y in x]

# print(y)

# # plt.plot(x, y)
# # plt.show()

# y1 = [y**3 for y in x]

# print(y1)

# plt.plot(x, y, x, y1)
# # plt.show()

# plt.axis([0, 15, 0, 1500])
# plt.show()

plt.xlabel("Values along x-axis")
# plt.show()


plt.ylabel("Values along y-axis")

plt.title("Square & cube of the value", fontsize = 14, color = "g")
# plt.show()


# plt.plot(x, x, "b+:")
# plt.show()

# plt.plot(x, x, "b*:", x, y, "rv:")
# plt.show()

# plt.plot(x, x, "b*-", x, y, "rv:")
# plt.show()

# plt.plot(x, x, "b*--", x, y, "rv:")
# plt.show()

# plt.plot(x, x, "b3-", x, y, "rv:")
# plt.show()

# plt.plot(x, x, "b3-.", x, y, "rv:")
# plt.show()

plt.subplot(3, 2, 2)
plt.plot(x, x, "b3-.", x, y, "rv:")
# plt.show()

# important :: to plot multiple windows in one window

plt.subplot(3, 2, 1)
plt.plot(x, x, "y4-.", x, y, "rv:")
plt.show()
