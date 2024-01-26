from timeit import timeit
import random

print("\nHasil sorted average case")

for i in range(5):
    g = list(range(3000))
    random.shuffle(g)
    t = timeit("sorted(g)",setup = "from __main__ import g", number=1)
    print("Menggunakan %d bilangan, memerlukan %8.7f detik" %(len(g), t))

print("\nHasil sorted best case")

for i in range(5):
    g = list(range(3000))
    t = timeit("sorted(g)",setup = "from __main__ import g", number=1)
    print("Menggunakan %d bilangan, memerlukan %8.7f detik" %(len(g), t))

print("\nHasil sorted worst case")

for i in range(5):
    g = list(range(3000))
    g = g[::-1]
    t = timeit("sorted(g)",setup = "from __main__ import g", number=1)
    print("Menggunakan %d bilangan, memerlukan %8.7f detik" %(len(g), t))
print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')
