#NO.4 Metode 1
class Queue():
    def __init__(self):
        self.qlist=[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self,data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.isEmpty()
        return self.qlist.pop(0)
    def getFrontMost(self):
        return self.qlist[0]
    def getRearMost(self):
        return self.qlist[len(self.qlist)-1]
 
q = Queue()
q.enqueue(1)
q.enqueue(12)
q.enqueue(56)
q.enqueue(69)
print("queue front = ", q.getFrontMost())
print("queue rear = ", q.getRearMost())
print('')
print('Sudah selesai.')

print('\n--- Oleh L200210137 ---')























    
    
