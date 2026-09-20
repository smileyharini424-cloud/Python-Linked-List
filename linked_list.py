class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:

    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def delete(self, data):
        if self.head is None:
            print("Linked List is empty.")
            return

        if self.head.data == data:
            self.head = self.head.next
            print("Element deleted successfully.")
            return

        current = self.head

        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                print("Element deleted successfully.")
                return

            current = current.next

        print("Element not found.")

    def display(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        current = self.head

        print("Linked List:", end=" ")

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

linked_list = LinkedList()

while True:
    print("\n1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        linked_list.insert_beginning(value)

    elif choice == 2:
        value = int(input("Enter element: "))
        linked_list.insert_end(value)

    elif choice == 3:
        value = int(input("Enter element to delete: "))
        linked_list.delete(value)

    elif choice == 4:
        linked_list.display()

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
