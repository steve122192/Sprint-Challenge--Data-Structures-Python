class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.count = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage.pop(self.count)
            self.storage.insert(self.count,item)
            self.count += 1
            if self.count == self.capacity:
                self.count = 0
            
    
    def get(self):
        return self.storage