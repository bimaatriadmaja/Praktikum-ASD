class Manusia(object):
    keadaan="lapar"
    def __init__(self,nama):
        self.nama=nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self,s):
        print("Saya baru saja makan", s)
        self.keadaan="kenyang"
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan="lapar"
    def mengalikanDenganDua(self,n):
        return n*2

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisialisasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangsaku = us
    def __str__(self):
        s = self.nama+", NIM"+str(self.NIM)\
            +". Tinggal di" +self.kotaTinggal \
            +". Uang saku Rp."+str(self.uangsaku)\
            +" tiap bulannya."
        return s
    def ambilNama(self):
        print (self.nama)
    def ambilNIM(self):
        print (self.NIM)
    def ambilUangSaku(self):
        print (self.uangsaku)
    def makan(self,s):
        """Metode ini menutupi makan -nya class Manusia. Mahasiswa kalau makan sambil belajar"""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan="Kenyang"
        
    def ambilKotaTinggal(self): #NO.2A
        print (self.kotaTinggal)
        
    def perbaruiKotaTinggal(self, baru): #NO.2B
        self.kotaTinggal = baru
        
    def tambahUangSaku(self, uang): #NO.2C
        self.uangsaku = self.uangsaku + uang

    listKuliah = []
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)

    def hapusKuliah(self, item):
        self.listKuliah.remove(item)

class SiswaSMA(Manusia):
    """Class SiswaSMA yang dibangun dari class Manusia"""
    def __init__(self,nama,no_induk,kelas,alamat):
        """Metode inisialisasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.no = no_induk
        self.kelas = kelas
        self.alamat = alamat
    def __str__(self):
        a = "Nama : "+self.nama+'\n'+"No Induk : "+str(self.no)+'\n'+"Tinggal di : "+self.alamat+'\n'+"Kelas : "+str(self.kelas)
        print (a)
    def ambilNama(self):
        print (self.nama)
    def ambilNoInduk(self):
        print (self.no)
    def ambilKelas(self):
        print (self.kelas)
    def ambilAlamat(self):
        print (self.alamat)

class MhsTIF(Mahasiswa):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanpeta(self):
        print('Python adalah core of the core,ahlinya ahli .')

m7 = Mahasiswa("Adnan","L200170021","Klaten",90000)
s1 = SiswaSMA("Adnan",17021,5,"Klaten")

        
print('\n--- Oleh L200210137 ---')
print('---- Bima Triadmaja ---') 

