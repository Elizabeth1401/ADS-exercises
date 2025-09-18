class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push_front(self, value):
        self.head = Node(value, self.head)

    def pop_front(self):
        if not self.head:
            raise IndexError("pop from empty list")
        val = self.head.value
        self.head = self.head.next
        return val 

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next
if __name__ == "__main__":
    ll = LinkedList()
    ll.push_front(3)
    ll.push_front(2)
    ll.push_front(1)
    print(list(ll)) # [1,2,3]
    print(ll.pop_front()) #1