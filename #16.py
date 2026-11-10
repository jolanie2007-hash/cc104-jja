class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
a = Node(10)
b = Node(20)
a.next = b
print(a.next.value)