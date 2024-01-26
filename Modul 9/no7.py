#NO.7
class SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

def tinggiPohon(akar, count=0):
    if akar is None:
        return 0
    else:
        return max(tinggiPohon(akar.kiri), tinggiPohon(akar.kanan))+1

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

print ('Tinggi maksimal dari Binary Tree adalah', tinggiPohon(a))
print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')


