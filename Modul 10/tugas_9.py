import time
import random
import timeit
import matplotlib.pyplot as plt

def cari(lis, target):
    n = len(lis)
    for i in range(n):
        if lis[i] == target:
            return True
        return False

def timee():
    n = 200
    lis = [1,6,7,8,3,2,11]
    awal = time.time()
    U = cari(lis, n)
    akhir = time.time()
    print("Jumlah adalah %d, memerlukan %8.7f detik" % (U, akhir-awal))
timee()

def a(n):
    a = [1,6,7,8,3,2,11]
    U = cari(a,n)

def ujia(n):
    ls=[]
    jangkauan = range(1,n+1)
    for i in jangkauan:
        t = timeit.timeit("a(" + str(i) +")", "from __main__ import a", number=1)
        ls.append(t)
    return ls

n = 10
LS = ujia(n)

plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1,n+1)])
plt.show()
print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')

