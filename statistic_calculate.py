def mean(a):
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s/len(a)

def variance(a):
    s = 0
    for i in range(len(a)):
        s += (a[i]-mean(a))**2
    return s /len(a) # do lech chuan tren mau sample /N-1
def standardDivetation(a):
    s = 0
    n = len(a)
    for i in range(n):
        s += (a[i]-mean(a))**2
    return (s /n)**0.5 # do lech chuan tren tong the population /N

def covariance(a, b):
    s = 0
    n = len(a)
    for i in range(n):
        s += (a[i] -mean(a))*(b[i] - mean(b))
    return s /n # Hiep phuog sai tren tong the population

def correlationCoefficient(a, b):
    return covariance(a,b)/ (standardDivetation(a)*standardDivetation(b))
def median(a):
    n = len(a)
    for i in range(n):
        return (a[n//2] +a[(n-1)//2])/2


