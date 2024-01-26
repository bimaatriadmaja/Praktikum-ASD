import time
import random
import timeit
import matplotlib.pyplot as plt

def a(n):
    sum = 0
    for i in range(n):
        if i % 3 == 0:
            for j in range(n//2):
                sum += j
        elif i % 2 == 0:
            for j in range(5):
                sum += j
        else:
            for j in range(n):
                sum += j

def ujia(n):
    ls=[]
    jangkauan = range(1,n+1)
    siap = "from __main__ import a"
    for i in jangkauan:
        t = timeit.timeit("a(" + str(i) +")",setup=siap, number=1)
        ls.append(t)
    return ls

n = 100
LS = ujia(n)

plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1,n+1)])
plt.show()
print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')

