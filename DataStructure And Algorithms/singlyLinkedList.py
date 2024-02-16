# AIM: Write a menu driven program to implement following
# operations on the singly linked list.
# {a) Insert a node at the front of the linked list
# (b) Insert a node at the end of the linked list
# (©) Insert a node such that linked list is in ascending
# order
# (d) Delete a First node of the linked list
# (e) Delete a node before specified position
# (f) Delete a node after specified position

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    def insertAtFront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insertInOrder(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        if curr.data > new_data:
            new_node.next = self.head
            self.head = new_node
            return
        while curr.next is not None and curr.next.data < new_data:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def deleteFirstNode(self):
        if self.head is None:
            return
        temp = self.head
        self.head = self.head.next
        temp = None

    def deleteBeforePos(self, pos):
        if self.head is None:
            return
        if pos == 1:
            return
        temp = self.head
        count = 1
        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1
        if temp is None:
            return
        temp.next = temp.next.next

    def deleteAfterPos(self, pos):
        if self.head is None:
            return
        temp = self.head
        count = 1
        while temp is not None and count < pos:
            temp = temp.next
            count += 1
        if temp is None or temp.next is None:
            return
        temp.next = temp.next.next

if __name__ == '__main__':

    llist = LinkedList()

    while True:
        print("1. Insert a node at the front of the linked list")
        print("2. Insert a node at the end of the linked list")
        print("3. Insert a node such that linked list is in ascending order")
        print("4. Delete a First node of the linked list")
        print("5. Delete a node before specified position")
        print("6. Delete a node after specified position")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter the data to be inserted: "))
            llist.insertAtFront(data)
            print("Node inserted successfully")
        elif choice == 2:
            data = int(input("Enter the data to be inserted: "))
            llist.insertAtEnd(data)
            print("Node inserted successfully")
        elif choice == 3:
            data = int(input("Enter the data to be inserted: "))
            llist.insertInOrder(data)
            print("Node inserted successfully")
        elif choice == 4:
            llist.deleteFirstNode()
            print("Node deleted successfully")
        elif choice == 5:
            pos = int(input("Enter the position: "))
            llist.deleteBeforePos(pos)
            print("Node deleted successfully")
        elif choice == 6:
            pos = int(input("Enter the position: "))
            llist.deleteAfterPos(pos)
            print("Node deleted successfully")
        elif choice == 7:
            break
        else:
            print("Invalid Choice")