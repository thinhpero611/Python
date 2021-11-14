from matplotlib import pyplot as plt
import statistic_calculate as stat
a = [[5, 2, 9, 21],
     [12, 23, 4, 10],
     [8, 6, 2, 12]]
b = [1, 4, 0 ,2]

def matrixDotVector(a, b):
    s = [0] * len(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            s[i] += a [i][j]*b[j]
    return s

print('vector(a) x vector(b) = ', matrixDotVector(a, b))
print()
x = [2, 6, 8, 8, 12, 16, 20, 20, 22, 26]
y = [58, 105, 88, 118, 117, 137, 157, 169, 149, 202]

def linearRegression(x, y):
    covariance = 0
    varianceOfX = 0
    for i in range(len(x)):
        covariance += (x[i] -stat.mean(x))*(y[i] - stat.mean(y))
        varianceOfX += (x[i] - stat.mean(x))**2
    return covariance/varianceOfX, stat.mean(y) - (covariance/varianceOfX)*stat.mean(x)
b1, b0 = linearRegression(x, y)    

print('phuong trinh hoi quy uoc luong: ',f'y={b0}+{b1}x')

plt.scatter(x, y, color='red')
plt.plot([-12, 50] , [b0 + b1*-12, b0 +b1* 50])
plt.show()
    






