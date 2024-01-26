#NO.5
class Mahasiswa:

    def __init__(self,nama,NIM,kota,us):

        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.UangSaku = us

    def __str__(self):

        return ("Nama {}, NIM {}, Kota {}, Uang Saku {}".
                format(self.nama,self.NIM,self.kotaTinggal,self.UangSaku))
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.UangSaku 

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


c0.next = c1
c1.next = c2
c2.next = c3
c3.next = c4
c4.next = c5
c5.next = c6
c6.next = c7
c7.next = c8
c8.next = c9
c9.next = c10


Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def cetak(A):
    for i in A:
        print (i)

def mergeSort2(A, awal, akhir):
    mid = (awal+akhir)//2
    if awal < akhir:
        mergeSort2(A, awal, mid)
        mergeSort2(A, mid+1, akhir)

    a, y, l = 0, awal, mid+1
    tmp = [None] * (akhir - awal + 1)
    while y <= mid and l <= akhir:
        if A[y].ambilNim() < A[l].ambilNim():
            tmp[a] = A[y]
            y += 1
        else:
            tmp[a] = A[l]
            l += 1
        a += 1

    if y <= mid:
        tmp[a:] = A[y:mid+1]

    if l <= akhir:
        tmp[a:] = A[l:akhir+1]

    a = 0
    while awal <= akhir:
        A[awal] = tmp[a]
        awal += 1
        a += 1

def mergeSort(A):
    mergeSort2(A, 0, len(A)-1)

print("---------------------- Sebelum diurutkan ----------------------")
cetak(Daftar)
mergeSort(Daftar)
print("\n---------------------- Setelah diurutkan ----------------------")
cetak(Daftar)

print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')
