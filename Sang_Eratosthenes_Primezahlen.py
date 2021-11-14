import numpy as np
n = [True]*1000
print(n[999])
count = 0
prime = []
x1 = x = int(input('Nhap vao mot so Nguyen Duong: '))

fact = ''
for i in range(2, 1001):
    if n[i-2]:
        #Dung dang Eratosthenes de loc ra so nguyen to:
        for j in range(2, 1001):
            if i == j : continue
            elif (j % i) == 0:
                n[j-2] = False
        # loc ra so nguyen to
        prime.append(i)
        
        #factorial tach ra thua so nguyen to
        while x %i == 0: 
            fact += str(i)+'*'
            x //=i
        count +=1
        
print('So Vong Lap: ', count)
print('So Nguyen To', np.array(prime))
print('Tach ra Thua So Nguyen To: ', fact[:-1])
#Tinh giai thua
def giaiThua(x):
    s = 1
    giaithua = ''
    for i in range(x):
        s *=i+1
        giaithua += str(i+1)+'*'
    if x< 100:
        print(f'giaithua cua {x} :{giaithua[:-1]}={s}')
    else:
        return s
print(giaiThua(x1))
