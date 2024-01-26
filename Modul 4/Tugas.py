#NO.1
class Mahasiswa(object):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        
c0 = Mahasiswa('Ika',10,'Sukoharjo',240000)
c1 = Mahasiswa('Budi',51,'Sragen',230000)
c2 = Mahasiswa('Ahmad',2,'Surakarta',250000)
c3 = Mahasiswa('Chandra',18,'Surakarta',235000)
c4 = Mahasiswa('Eka',4,'Boyolali',240000)
c5 = Mahasiswa('Fandi',31,'Salatiga',250000)
c6 = Mahasiswa('Deni',13,'Klaten',245000)
c7 = Mahasiswa('Galuh',5,'Wonogiri',245000)
c8 = Mahasiswa('Janto',23,'Klaten',245000)
c9 = Mahasiswa('Hasan',64,'Karanganyar',270000)
c10 = Mahasiswa('Khalid',29,'Purwodadi',230000)

Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

target = 'Klaten'
for i in Daftar:
    if i.kotaTinggal == target:
        print([6,8])
        
def searching(koleksi,target):
    output = []
    index = 0
    for i in koleksi:
        if i.kotaTinggal == target:
            output.append(index)
            index += 1
        else:
            index += 1
    return output        

#NO.2
def cariUangSakuTerkecil(kumpulan):
    terkecil = kumpulan[0].uangSaku
    for i in kumpulan:
        if i.uangSaku < terkecil:
            terkecil = i.uangSaku
    return terkecil #kembali ke yang terkecil

#NO.3
def cariDaftarUangSakuTerkecil(kumpulan):
    n = []  
    terkecil = kumpulan[0].uangSaku
    for i in kumpulan:
        if i.uangSaku < terkecil:
            terkecil = i.uangSaku
            n.append(kumpulan.index(i))
    return n

#NO.4
def cariDaftarUangSakuKurang(kumpulan):
    b = []  
    for i in kumpulan:
        if i.uangSaku < 250000:
            terkecil = i.uangSaku
            b.append(kumpulan.index(i))
    return b
   
#NO.6
def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) -1
    data = []

    while low <= high:
        mid = (high + low) //2
        if kumpulan[mid] == target:
            data.append(kumpulan.index(target))
            return True
        elif target < kumpulan[mid]:
            high = mid -1
        else :
            low = mid +1
    return False

#NO.7
def binSearch(kumpulan, target):
    low = 0
    high = len(kumpulan) -1
    data = []
    
    while low != high:
        mid = (high + low) //2
        if kumpulan[mid] == target:
            break
        elif target < kumpulan[mid]:
            high = mid -1
        else :
            low = mid +1
    for i in range (low, high):
        if target == kumpulan[i]:
            data.append(i)
    return data

a = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]

print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')
