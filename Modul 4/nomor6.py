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

print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')
