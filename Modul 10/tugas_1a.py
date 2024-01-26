from timeit import timeit
import random

def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range(1,n+1):
        hasilnya = hasilnya + i
    return hasilnya

for i in range(5):
    a = jumlahkan_cara_1(1000000)
    b = timeit("jumlahkan_cara_1(1000000)","from __main__ import jumlahkan_cara_1", number = 1)
    print("Jumlah adalah %d, memerlukan %9.8f detik" %(a, b))
    print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')


