#NO.6
class SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

def ukuranPohon(akar, count=0):
    if akar is None:
        return count

    return ukuranPohon(akar.kiri, ukuranPohon(akar.kanan, count+1))

a = SimpulPohonBiner('Klaten')
b = SimpulPohonBiner('Bekasi')
c = SimpulPohonBiner('Jakarta')
d = SimpulPohonBiner('Depok')
e = SimpulPohonBiner('Tanggerang')
f = SimpulPohonBiner('Solo')
g = SimpulPohonBiner('Surakarta')
h = SimpulPohonBiner('Cilacap')
i = SimpulPohonBiner('Trenggalek')
j = SimpulPohonBiner('Yogyakarta')

a.kiri = b; a.kanan = c
b.kiri = d; b.kanan = e
c.kiri = f; c.kanan = g
e.kiri = h;
g.kanan = i

print('Ukuran dari Binary Tree adalah',ukuranPohon(a))
print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')

