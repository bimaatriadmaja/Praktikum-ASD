#NO.8
class Node():
    def __init__(self, data, tautan=None):
        self.data = data
        self.taut = tautan

def cetak(head):
    curr = head
    while curr is not None:
        try:
            print (curr.data)
            curr = curr.taut
        except:
            pass

a = Node(11)
b = Node(33)
c = Node(55)
d = Node(66)
e = Node(44)
f = Node(99)
g = Node(77)

a.taut = b
b.taut = c
c.taut = d
d.taut = e
e.taut = f
f.taut = g

def mergeSortLL(A):
    linked = A
    try:
        daftar = []
        curr = A
        while curr:
            daftar.append(curr.data)
            curr = curr.taut
        A = daftar
    except:
        A = A

    if len(A) > 1:
        mid = len(A) // 2
        separuhkiri = A[:mid]
        separuhkanan = A[mid:]

        mergeSortLL(separuhkiri)
        mergeSortLL(separuhkanan)

        i = 0;j=0;k=0
        while i < len(separuhkiri) and j < len(separuhkanan):
            if separuhkiri[i] < separuhkanan[j]:
                A[k] = separuhkiri[i]
                i = i + 1
            else:
                A[k] = separuhkanan[j]
                j = j + 1
            k=k+1
        while i < len(separuhkiri):
            A[k] = separuhkiri[i]
            i = i + 1
            k=k+1
        while j < len(separuhkanan):
            A[k] = separuhkanan[j]
            j = j + 1
            k=k+1
    for x in A:
        try:
            linked.data = x
            linked = linked.taut
        except:
            pass

mergeSortLL(a)
cetak(a)

print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')

