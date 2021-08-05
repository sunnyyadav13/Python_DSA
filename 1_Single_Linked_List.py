class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def add_after(self, data, x):    # node ke beech mein kisi node ke baad new node insert karna hai
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("node is not presesnt in LL")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    # node ke beech mein kisi node ke pehle new node insert karna hai
    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is empty!")
    
        elif self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                if n.next.data == x:
                    break
                n = n.next
            if n.next is None:
                print("Node is not found!")
            else:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node

    def insert_empty(self, data):  # video 18 # Amulya academy practice
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")

    def delete_begin(self):  # V19
        if self.head is None:
            print("Linked List is empty can't delete!")
        else:
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("Linked List is empty can't delete!")
        elif self.head.next is None:
            self.head = None
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None

    def delete_by_value(self, x):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.data == x:    # for single node
            self.head = self.head.next
        else:
            n = self.head
            while n.next is not None:
                if n.next.data == x:
                    break
                n = n.next
            if n.next is None:
                print("Node is not found")
            else:
                n.next = n.next.next


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.delete_by_value(50)
LL1.print_LL()
