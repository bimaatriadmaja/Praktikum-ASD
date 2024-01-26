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
