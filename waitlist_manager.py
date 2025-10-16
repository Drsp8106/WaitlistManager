# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None



# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        print(f"{name} added to the front of the waitlist.")

    def add_end(self, name):
        new_node = Node(name)
        if self.head is None:
            self.head = new_node
            print(f"{name} added as the first customer in the waitlist.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"{name} added to the end of the waitlist.")

    def remove(self, name):
        if self.head is None:
            print("The waitlist is empty.")
            return
        if self.head.name == name:
            self.head = self.head.next
            print(f"{name} has been removed from the waitlist.")
            return
        current = self.head
        while current.next and current.next.name != name:
            current = current.next
        if current.next is None:
            print(f"{name} not found in the waitlist.")
        else:
            current.next = current.next.next
            print(f"{name} has been removed from the waitlist.")

    def print_list(self):
        if self.head is None:
            print("The waitlist is empty.")
            return
        current = self.head
        while current:
            print(current.name)
            current = current.next



def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")


waitlist_generator()


'''
Design Memo:

This program implements a simple linked list to manage a customer waitlist. 
Each customer is stored in a the object. The LinkedList class manages these nodes using a 
"head" pointer that always refers to the first customer in line. From the head, 
the program works through adding and removing customers.

The beginning is the big part of the program, beginning th elist.
entire list. If the head is None, the list is empty. When a new customer is 
added to the front, the new node becomes the new head. When a customer is 
removed from the front, the head is reassigned to the next node.

A real engineer might need a custom linked list like this when working with 
dynamic, unpredictable data where items are frequently added and removed — 
such as task scheduling systems, operating system queues, or customer service 
waitlists. 
'''
