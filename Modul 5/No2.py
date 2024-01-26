#No.2
def urutkan(a,b):
    c = a + b
    for x in range(len(c)):
        terkecil = x
        for y in range(x+1, len(c)):
            if c[terkecil] > c[y]:
                terkecil = y
        c[x], c[terkecil] = c[terkecil], c[x]
    return c

print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')

     
