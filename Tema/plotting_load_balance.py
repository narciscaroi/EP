import matplotlib.pyplot as plt

# policies -> name of the policy
# x -> requests
# y -> repond time for an "n" requests

policies = ['Random', 'Round Robin', 'Weighted Round Robin', 'Least Connection', 'Fastest Time']

x = [1, 10, 30, 50, 100, 200, 300, 400, 500]
random_y = [0.32, 2.1, 2.71, 4.1, 8.2, 15.5, 23.4, 31, 37.8]

roundRobin_y = [0.5, 1.8, 2.3, 3.9, 7.34, 14.5, 21.6, 28.9, 36.1]

weightedRoundRobin_y = [0.3, 2, 2.4, 3.6, 7, 13.9, 20.6, 27.2, 33.7]

leastConnection_y = [0.4, 1.5, 2.3, 3.7, 7.4, 14.4, 21.7, 29, 35.8]

fastestTime_y = [2.4, 2.9, 4.1, 4.9, 7.6, 13, 19, 24, 29.5]

plt.plot(x, random_y)
plt.plot(x, roundRobin_y)
plt.plot(x, weightedRoundRobin_y)
plt.plot(x, leastConnection_y)
plt.plot(x, fastestTime_y)
plt.legend(policies)
plt.xlabel("number of requests")
plt.ylabel("average time to finish requests")
plt.show()
