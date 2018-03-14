import numpy as np
import math
from matplotlib import pyplot as plt
import random

a = 0
for i in range(1,1537):
    a += 1536.0/i
print(a)
print((math.log(384))*384)
a = 0
cont = 0.99
t = 500.0
x = (math.log(0.1)/math.log(0.9957))
print(x)
print(0.9957**550)
for i in range(1, 150):
    b = 1/(cont**i)
    a += math.ceil(b)
print('期望是{}'.format(a))
#print('{}'.format(cont*a))
print('tolerance={}'.format(cont**a))

'''
n = np.linspace(1, 201, 200)
r1 = np.random.random(200)*2.0+1.0
r2 = np.random.random(200)*2.0+1.0
r3 = np.random.random(200)*2.0+1.0
print(r1)
print(r2)
print(r3)
a2 = 0.5 * np.power(0.9, n)
a3 = 0.5 * 1.0/np.power(n,2)
a1 = 0.5 * np.ones(200)
plt.subplot(121)
y1 = r1 * (1-np.power(1-a1, n))
y2 = r2 * (1-np.power(1-a2, n))
y3 = r3 * (1-np.power(1-a3, n))
plt.plot(n, y1, n, y2, n, y3)
plt.xlabel('Trial Number')
plt.ylabel('Q Value')
plt.legend(labels=['$\\alpha=0.5$', '$\\alpha=0.5×0.9^n$', '$\\alpha=\\frac{0.5}{n^2}$'])

plt.subplot(122)
plt.plot(n, a1, n, a2, n, a3)
plt.xlabel('Trial Number')
plt.ylabel('$\\alpha$')
plt.legend(labels=['$\\alpha=0.5$', '$\\alpha=0.5×0.9^n$', '$\\alpha=\\frac{0.5}{n^2}$'])
plt.show()
'''
'''
#print(math.exp(np.log(0.01)/700))
#print(math.log(0.01)/700)
n = np.linspace(1, 1001, 1000)
y1 = np.power(0.993, n)
y2 = np.power(n, -2)
y3 = np.exp(-1.0 * 0.006 *n)
y4 = np.fabs(np.cos(0.002 * n))

plt.figure()
plt.plot(n, y1, n, y2, n, y3, n, y4)
plt.xlabel('Trial Number')
plt.ylabel('$\epsilon$')
plt.legend(labels=['$0.99^n$', '$n^{-2}$', '$e^{-0.9n}$', '$cos(0.002n)$'])
plt.show()
'''