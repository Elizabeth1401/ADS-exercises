class Queue:
    def __init__(self):
        self._d = deque()
    
    def enqueue(self, x):
        self._d.append(x) #O(1)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._d.popleft() #O(1)
    
    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._d[0]
    
    def is_empty(self):
        return len(self._d) == 0

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.front()) #1
    print(q.dequeue()) #1
    print(q.dequeue()) #2