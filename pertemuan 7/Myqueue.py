class Myqueue:
    def __init__(self):
        self . item = []
    def enQueue(self, item):
        self.item.append (item)
    def deQueu(self):
        return self.item.pop(0)
    def isEmpty(self):
        return self.item == []
    def front(self):
        return self.item(0)
    def show(self):
        print(self.item)
queue = Myqueue()
print(queue.isEmpty())
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)
queue.show()
print(f"antrian terdepan adalah: [quwuw.front()]")
queue.deQueu
print(f"antrian terdepan adalah: [queue.front()]")

