# to revers a linked list 

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def display_list(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

def reverse_linkedlist(lst):
    if lst.head == None:
        return None 
    
    prev = None 
    current = lst.head
    while(current):
        next_node = current.next 
        current.next = prev
        prev = current
        current = next_node

    lst.head = prev     

def reverse_recursive(self, curr=None, prev=None):
        if curr is None:
            self.head = prev
            return
        next_node = curr.next
        curr.next = prev
        self.reverse_recursive(next_node, curr)


lst = LinkedList()
lst.append(1)
lst.append(4)
lst.append(5)
lst.append(10)

print(f"Original linked list:")
lst.display_list()
reverse_linkedlist(lst)
print(f"Reversed linked list:")
lst.display_list()
      