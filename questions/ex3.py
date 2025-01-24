# to revers a doubled linked list 

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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
        new_node.prev = current
    
    def display_list(self):
        current = self.head
        while(current):
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def reverse_linkedlist(lst):
    if lst.head == None:
        return None 
        
    current = lst.head
    prev = None
    while(current):
        next_node = current.next
        current.next = prev
        current.prev = next_node
        prev = current
        current = next_node

    lst.head = prev     


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
      