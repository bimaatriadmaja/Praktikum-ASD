# Tugas nomor 11
def apakahKabisat(x):
    if x%4 and x%100 and x%400 == 0:
        return True
    elif x%4 == 0 and x%100 == 0 and x%400 != 0:
        return False
    elif x%4 and x%100 == 0:
        return False
    elif x%4 == 0:
        return True
    else:
        return False

print(apakahKabisat(1896))
print(apakahKabisat(1897))  
print(apakahKabisat(1900))
print(apakahKabisat(2000))
print(apakahKabisat(2004))
print(apakahKabisat(2100))
print(apakahKabisat(2400))
print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')
