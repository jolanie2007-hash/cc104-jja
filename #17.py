class Node:
    def __init__(self, v, next=None):
        self.v, self.next = v, next
head = Node(1, Node(2, Node(3)))
head = head.next
print(head.v)








