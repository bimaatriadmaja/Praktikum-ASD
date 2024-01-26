# Tugas nomor 7
def faktorPrima(n):
    i = 2
    list = []

    while i*i <= n:
        if n%i != 0:
            i += 1
        else:
            n //= i
            list.append(i)
    if n > 1:
        list.append(n)
    return list

print(faktorPrima(10))
print(faktorPrima(120))
print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')
