#NO.6
class Mahasiswa:
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.UangSaku = us

    def __str__(self):

        return ("Nama {}, NIM {}, Kota {}, Uang Saku {}"
                .format(self.nama,self.NIM,self.kotaTinggal,self.UangSaku))
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
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
        print(i)

def quickSort(arr):
    kurang = []
    pivotList = []
    lebih = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i.ambilNIM() < pivot.ambilNIM():
                kurang.append(i)
            elif i.ambilNIM() > pivot.ambilNIM():
                lebih.append(i)
            else:
                pivotList.append(i)
        kurang = quickSort(kurang)
        lebih = quickSort(lebih)
        return kurang + pivotList + lebih

print("---------------------- Sebelum diurutkan ----------------------")
cetak(Daftar)
print("\n---------------------- Setelah diurutkan ----------------------")
quickSort(Daftar)
cetak(Daftar)

print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')
