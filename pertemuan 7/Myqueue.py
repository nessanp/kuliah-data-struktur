class Myqueue:
    def __init__(self):
        self.items = []
    def enQueue(self, item):
        self.items.append(item)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0 
    def front(self):
        return self.items[0]
    def show(self):
        print(self.items)
queue = Myqueue()
print(queue.isEmpty())        
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)
queue.show()
print(f"antrian terdepan adalah: {queue.front()}")
queue.deQueue()
print(f"antrian terdepan adalah: {queue.front()}")