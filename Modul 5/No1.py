#No.1
class Manusia(object):
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("salaam, namaku",self.nama)
    def makan(self, s):
        print("Saya baru saja makan", s)
        self.keadaan = 'kenyang'
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self,n):
        return n*2

class Mahasiswa(Manusia):
    listKuliah = []
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + ', berasal dari ' + self.kotaTinggal \
            + ', mempunyai Rp ' + str(self.uangSaku) \
            + ' perbulan.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        print("Saya baru saja makan",s)
        self.keadaan = 'kenyang'
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self,kota):
        self.kotaTinggal = kota
    def tambahUangSaku(self,nom):
        self.uangSaku += nom
    def ambilKuliah(self, matkul):
        self.listKuliah.append(matkul)
    def hapusMatkul(self, matkul):
        self.listKuliah.remove(matkul)
        
class MhsTIF(Mahasiswa):      
    def katakanPy(self):
        print('Python is cool.')

def insertionSort(a):
    n = len(a)
    for i in range(1,n):
        nilai = a[i]
        pos = i
        while pos > 0 and nilai.NIM < a[pos - 1].NIM:
            a[pos] = a[pos - 1]
            pos = pos - 1
        a[pos] = nilai

def cekNIM(a):
    for i in a:
        print(i)

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

print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')

