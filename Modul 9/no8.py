#NO.8
class simpulbiner(object):
    def __init__(self, data):
        self.data=data
        self.kiri=None
        self.kanan=None

    def __str__(self):
        return str(self.data)

A=simpulbiner('Klaten')
B=simpulbiner('Sukoharjo')
C=simpulbiner('Surakarta')
D=simpulbiner('Jakarta')
E=simpulbiner('Solo')
H=simpulbiner('Yogyakarta')


A.kiri=B; A.kanan=C
B.kiri=D; B.kanan=E
D.kiri=H; 

datalist=[A.data, B.data, C.data, D.data, E.data, H.data]
level=[]

def preorder(sub):
    if sub is not None:
        print(sub.data)
        preorder(sub.kiri)
        preorder(sub.kanan)
        
def inorder(sub):
    if sub is not None:
        inorder(sub.kiri)
        print(sub.data)
        inorder(sub.kanan)

def postorder(sub):
    if sub is not None:
        postorder(sub.kiri)
        postorder(sub.kanan)
        print(sub.data)
def traverse(root):
    lvlist=[]
    current_level = [root]
    lv=0
    while current_level:
        next_level = list()
        for n in current_level:
            if n.kiri:
                next_level.append(n.kiri)
                level.append(lv+1)
            if n.kanan:
                next_level.append(n.kanan)
                level.append(lv+1)
            current_level = next_level
            
        lv+=1
        lvlist.append(lv)
    return lvlist

def cetakDataDanLevel(root):
    traverse(A)
    print(root.data, ', Level 0')
    for i in range(len(level)):
          print(datalist[i+1], ', Level', level[i])
          
cetakDataDanLevel(A)
print('')
print("-"*10,"preorder traversal","-"*10)
preorder(A)
print("-"*10,"inorder traversal","-"*10)
inorder(A)
print("-"*10,"postorder traversal","-"*10)
postorder(A)
print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')


