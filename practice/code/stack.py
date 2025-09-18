class Stack:
    def __init__(self):
        self._a = []
    
    def push(self, x):
        self._a.append(x) #O(1)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._a.pop() #O(1)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._a[-1]
    
    def is_empty(self):
        return len(self._a) == 0

if __name__ == "__main__":
    s = Stack()
    s.push(10); s.push(20)
    print(s.peek()) #20
    print(s.pop()) #20
    print(s.pop()) #10