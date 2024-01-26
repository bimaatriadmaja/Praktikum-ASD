from timeit import timeit
import random

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] - A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

for i in range(5):
    angka = list (range(3000))
    random.shuffle(angka)
    t = timeit("insertionSort(angka)","from __main__ import insertionSort, angka", number = 1)
    print("Menggunakan %d bilangan, memerlukan %8.7f detik" %(len(angka), t))
print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')
