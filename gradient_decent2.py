from matplotlib import pyplot as plt

#Nhap du lieu dau vao
x = [1, 1.2, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 11, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y = [13, 12, 10, 11, 8, 6, 5, 4, 3.5, 3, 2.5, 2.6, 2.4, 2.3, 2.5, 3, 5, 7, 8.5, 10, 12, 12.7]
n = len(x)

#set up for prediction
w = [1, 2, 3]
iteration = 800
learning_step = 0.00001

# Tao ham prediction
def prediction(x, y):
    
    return w[0] + w[1]*x + w[2]*x*x - y

#gradient_decent
loss = f0 = f1 = f2 = [0]*iteration
for i in range(iteration):
    for j in range(n):
        loss[i] += (prediction(x[j], y[j]))**2
        f0[i] += prediction(x[j], y[j])
        f1[i] += prediction(x[j], y[j])*x[j]
        f2[i] += prediction(x[j], y[j])*x[j]*x[j]
    loss[i] = loss[i]*0.5*1/n
    w[0] -= learning_step*f0[i]
    w[1] -= learning_step*f1[i]
    w[2] -= learning_step*f2[i]

# tra ve ket quA Hoi QQuy:

print(w)
print('Phuong trinh hoi quy du doan la: ')
print(f'y={w[0]} + {w[1]}x + {w[2]}x^2')
input('Press Enter Key !')

#Kiem tra Ham J(w)
for i in range(50):
    print(f'{f0[i]}__{f1[i]}__{f2[i]}__{loss[i]}')
for i in range(780, iteration):
    print(f'{f0[i]}__{f1[i]}__{f2[i]}__{loss[i]}')
# dao ham = 0 thi dat  dinh cua no

plt.subplot(1, 2, 1)

plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data Curve')

#du doan gia tri x va y:
x_predict = eval(input('Nhap vao x ma ban muon du doan: '))
print('Y prediction = ', prediction(x_predict, 0))
plt.scatter(x_predict, prediction(x_predict, 0), label='Prediction Point')

# ve duong parabol
x_plot = [ i for i in range(-500, 500)]
y_plot = [ prediction(i, 0) for i in x_plot]
plt.plot(x_plot, y_plot, 'r')

plt.subplot(1, 2, 2)

#Bieu dien gia tri Loss:
plt.plot(list(range(iteration)), loss)
plt.xlabel('step')
plt.ylabel('loss')
plt.title('Control Overflow')
         
plt.show()

def mean(x):
    s = 0
    n = len(x)
    for i in range(n):
        s += x[i]
    return s/n
def standardDevitation(x):
    s = 0
    n = len(x)
    for i in range(n):
        s += (x[i] - mean(x))**2
    return (s/n)**2
def normalization(x):
    n = len(x)
    z = [0] *n
    for i in range(n):
        z[i] = (x[i] - mean(x))/standardDevitation(x)
    return z
print('z-score normalization: ')
print(normalization(x))
print(normalization(y))



        

