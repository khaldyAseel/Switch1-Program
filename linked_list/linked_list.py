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

# Recreating the linked list
linked_list = LinkedList()
elements = [3, 5, 15, 66, -6]

for element in elements:
    linked_list.append(element)

linked_list.display_list()
