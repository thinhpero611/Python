from matplotlib import pyplot as plt
import numpy as np


x = [1, 1.2, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 11, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y = [13, 12, 10, 11, 8, 6, 5, 4, 3.5, 3, 2.5, 2.6, 2.4, 2.3, 2.5, 3, 5, 7, 8.5, 10, 12, 12.7]
plt.subplot(1, 2, 1)
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('data curve')
N = len(x)
x = np.array(x).reshape(-1, 1)
y = np.array(y).reshape(-1, 1)
x = np.hstack((np.ones((N, 1)), x, x**2))
w = np.array([14.5, -2.4, .1]).reshape(-1, 1)
numOfIteration = 200
cost = np.zeros((numOfIteration ,1))
learning_rate = 0.000001
for i in range(numOfIteration):
    r = np.dot(x, w) -y
    cost[i] = np.sum(r*r)*0.5
    w[0] -= learning_rate*np.sum(r)
    w[1] -= learning_rate*np.sum(np.multiply(r, x[:, 1].reshape(-1, 1)))
    w[2] -= learning_rate*np.sum(np.multiply(r, x[:, 2].reshape(-1, 1)))

v = np.arange(0, 30)
print(w)
print(cost.reshape(1, -1))
plt.plot(v, w[0] + w[1]*v + w[2]*v*v, 'red')
plt.subplot(1, 2, 2)
plt.plot(np.arange(numOfIteration), cost)
plt.xlabel('Iter')
plt.ylabel('Loss')
plt.title('Control_Overflow')
plt.show()
