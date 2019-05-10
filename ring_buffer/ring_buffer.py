class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        try:
            self.storage[self.current] = item
        except:
            self.current = 0
            self.storage[self.current] = item

        self.current = self.current + 1

    def get(self):
        itemlist = [item for item in self.storage if item != None]
        return(itemlist)


buffer = RingBuffer(5)
buffer.append(1)
buffer.append(6)
buffer.append(7)
buffer.get()
