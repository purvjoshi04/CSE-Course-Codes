# AIM:Write a menu driven program to implement following
# operations on the singly linked list.
# (a) Insert a node at the front of the linked list
# (b) Insert a node at the end of the linked list
# (c) Insert a node such that linked list is in ascending order
# (d) Delete a First node of the linked list
# (e) Delete a node before specified position
# (f) Delete a node after specified position.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
    def insert_at_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
 
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
 
    def insert_in_order(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        elif data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        elif data >= self.tail.data:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next != self.head and current.next.data < data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
 
    def delete_first_node(self):
        if self.head is None:
            print("The linked list is empty.")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
 
    def delete_before_position(self, pos):
        if self.head is None:
            print("The linked list is empty.")
        elif pos == 1:
            print("Cannot delete before the first node.")
        else:
            current = self.head
            while current.next != self.head and pos > 2:
                prev = current
                current = current.next
                pos -= 1
            if pos > 2:
                print("Invalid position.")
            else:
                if current == self.head:
                    self.head = self.head.next
                    self.tail.next = self.head
                else:
                    prev.next = current.next
 
    def delete_after_position(self, pos):
        if self.head is None:
            print("The linked list is empty.")
        elif pos == 0:
            print("Cannot delete after the last node.")
        else:
            current = self.head
            while current.next != self.head and pos > 0:
                current = current.next
                pos -= 1
            if pos > 0:
                print("Invalid position.")
            else:
                if current.next == self.head:
                    self.tail = current
                current.next = current.next.next
 
    def display(self):
        if self.head is None:
            print("The linked list is empty.")
        else:
            current = self.head
            while current.next != self.head:
                print(current.data, end=" -> ")
                current = current.next
            print(current.data, end=" -> ")
            print("...")
 

cll = CircularLinkedList()
 
while True:
    print("\nCircular Linked List Operations")
    print("==================================")
    print("1.Insert a node at the front of the linked list")
    print("2. Insert a node at the end of the linked list")
    print("3. Insert a node in ascending order")
    print("4. Delete the first node of the linked list")
    print("5. Delete a node before a specified position")
    print("6. Delete a node after a specified position")
    print("7. Display the linked list")
    print("8. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
      data = int(input("Enter the data to be inserted: "))
      cll.insert_at_front(data)
    elif choice == 2:
      data = int(input("Enter the data to be inserted: "))
      cll.insert_at_end(data)
    elif choice == 3:
      data = int(input("Enter the data to be inserted: "))
      cll.insert_in_order(data)
    elif choice == 4:
      cll.delete_first_node()
      print("First node deleted")
    elif choice == 5:
      pos = int(input("Enter the position before which the node has to be deleted: "))
      cll.delete_before_position(pos)
    elif choice == 6:
      pos = int(input("Enter the position after which the node has to be deleted: "))
      cll.delete_after_position(pos)
    elif choice == 7:
      cll.display()
    elif choice == 8:
      break
    else:
      print("Invalid choice.")

