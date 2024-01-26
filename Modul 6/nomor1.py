#NO.1
class Mahasiswa(object):
    def __init__(self, nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

c0 = Mahasiswa('Bima','L200210137','Sukoharjo', 240000)
c1 = Mahasiswa('Triadmaja','L200210351','Sragen', 230000)
c2 = Mahasiswa('Risma','L200210302','Surakarta', 250000)
c3 = Mahasiswa('Nanda','L200210318','Surakarta', 235000)
c4 = Mahasiswa('Fatika','L200210304','Boyolali', 240000)
c5 = Mahasiswa('Sari','L200210331','Salatiga', 250000)
c6 = Mahasiswa('Dimas','L200210313','Klaten', 245000)
c7 = Mahasiswa('Cahyo','L200210305','Wonogiri', 245000)
c8 = Mahasiswa('Vikki','L200210323','Klaten', 245000)
c9 = Mahasiswa('Gilang','L200210364','Karanganyar', 270000)
c10 = Mahasiswa('Eko','L200210329','Purwodadi', 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]
    
        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i=0 ; j=0 ; k=0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
                A[k] = separuhKiri[i]
                i = i + 1
            else:
                A[k] = separuhKanan[j]
                j = j + 1
            k = k+1

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i = i + 1
            k = k + 1
        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j = j + 1
            k = k + 1

def convert(arr, obj):
    hasil = []
    for x in range (len(arr)):
        for i in range (len(arr)):
            if arr[x] == obj[i].NIM:
                hasil.append(obj[i])
    return hasil

A = []
for x in Daftar:
    A.append(x.NIM)

print("---------- Merge Sort ----------")
mergeSort(A)
for i in convert(A, Daftar):
    print(i.nama, i.NIM, i.kotaTinggal, i.uangSaku)
print()

def partisi(A, awal, akhir):
    nilaiPivot = A[awal]

    penandaKiri = awal + 1
    penandaKanan = akhir

    selesai = False
    while not selesai:

        while penandaKiri <= penandaKanan and \
              A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1

        while A[penandaKanan] >= nilaiPivot and \
              penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan - 1

        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp

    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp

    return penandaKanan

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)

def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)

def convert(arr, obj):
    hasil = []
    for x in range (len(arr)):
        for i in range (len(arr)):
            if arr[x] == obj[i].NIM:
                hasil.append(obj[i])
    return hasil

A = []
for x in Daftar:
    A.append(x.NIM)

print("---------- Quick Sort ----------")
quickSort(A)
for i in convert(A, Daftar):
    print(i.nama, i.NIM, i.kotaTinggal, i.uangSaku)

print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')
