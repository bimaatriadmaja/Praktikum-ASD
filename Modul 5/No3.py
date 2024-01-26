#No.3
from time import time as waktu
from random import shuffle as acak

def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def cariPosisiTerkecil(A, x, y):
    posisiTerkecil = x
    for i in range(x+1, y):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)
            
def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        posisi = i
        while posisi > 0 and nilai < A[posisi-1]:
            A[posisi] = A[posisi-1]
            posisi = posisi-1
        A[posisi] = nilai
        

ac = [i for i in range(1,6001)]
acak(ac)
u_bubble = ac[:]
u_select = ac[:]
u_insert = ac[:]

a = waktu();bubbleSort(u_bubble);b=waktu();print("~~~Bubble    : %g detik~~~"%(b-a));
a = waktu();selectionSort(u_select);b=waktu();print("~~~Selection : %g detik~~~"%(b-a));
a = waktu();insertionSort(u_insert);b=waktu();print("~~~Insertion : %g detik~~~"%(b-a));

print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')
