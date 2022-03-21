import matplotlib.pyplot as plt

# x => number of requests
# y1 => response time
# y2 => requests per seconds

# us worker 1
#x = [1, 10, 30, 50, 75, 100, 125, 150, 175, 200, 300, 400, 500]
#y1 = [0.384, 0.683, 0.431, 0.424, 0.545, 0.684, 1.180, 1.920, 3.5, 4.51, 6.3, 6.773, 6.5]
#y2 = [0.4, 3.4, 10.5, 17.9, 25.5, 32.5, 35.8, 38.2, 33.8, 34.5, 40, 46.8, 44]
# 500 - RemoteDisconnected('Remote end closed connection without response')

# asia worker 1
#x = [1, 10, 30, 50, 75, 100, 125, 150, 175, 200, 300, 400, 500]
#y1 = [0.519, 0.530, 0.552, 0.585, 0.638, 0.717, 0.761, 1.3, 1.382, 1.871, 3.977, 5, 5.2]
#y2 = [0.4, 3.4, 10.2, 16.4, 24.5, 32.4, 37.5, 41.3, 43.9, 46.7, 47.7, 45.7, 46.7]
# 500 - RemoteDisconnected('Remote end closed connection without response')

# emea worker 0
x = [1, 10, 30, 50, 75, 100, 125, 150, 175, 200, 300, 400, 500]
y1 = [0.263, 0.283, 0.29, 0.3, 0.361, 0.435, 0.530, 0.821, 1.282, 1.784, 3.871, 5.483, 7.5]
y2 = [0.3, 3.9, 10.3, 18.1, 27.2, 34.3, 41.8, 45.6, 46.9, 47.2, 46.6, 46.5, 45.8]
# 500 - RemoteDisconnected('Remote end closed connection without response')

figure, axis = plt.subplots(1, 2)
axis[0].plot(x,y1)
axis[0].set_ylabel("average response time")
axis[0].set_xlabel("number of parallel requests")
axis[0].set_title("Average response time in region emea, machine 0")

axis[1].plot(x,y2)
axis[1].set_ylabel("average rquest per second")
axis[1].set_xlabel("number of parallel requests")
axis[1].set_title("Average requests per second in region emea, machine 0")

plt.show()

