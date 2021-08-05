class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next =None 


class DoublyLL:
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
    
    def print_LL_reverse(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            while n is not None:
                print(n.data)
                n=n.prev
    
    def insert_empty(self, data):  # video 24 # Amulya academy practice
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")
                
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head=new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev=n

    def add_after(self, data, x):    # node ke beech mein kisi node ke baad new node insert karna hai
        if self.head is None:
            print("Linked List is empty!")
        else:
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
                new_node.prev = n
                if n.next is not None:
                    n.next.prev=new_node
                n.next = new_node

                                        # node ke beech mein kisi node ke pehle new node insert karna hai
    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.next
            if n is None:
                print("node is not presesnt in LL")
            else:
                new_node = Node(data)
                new_node.next=n
                new_node.prev=n.prev
                if n.prev is not None:
                    n.prev.next=new_node
                else:
                    self.head = new_node
                n.prev = new_node
                
     def delete_by_value(self,x):
        if self.head is None:      #LL is empty
            print("DLL is empty can't delte !")
            return
        if self.head.next is None:   #LL has only 1 node
            if x==self.head.data:
                self.head = None
            else:
                print("x is not present in DLL")
            return
        if self.head.data == x:    #  LL has more than 1 node but carefull in deleting of first node
            self.head = self.head.next
            self.head.prev = None
            return
        n = self.head                       #  LL has more than 1 node but carefull in deleting of middle node except last node
        while n.next is not None:         #yeh second last node tak ke dat ko check kar rha hai last node pe pahuchte hi loop break hoga
            if x==n.data:
                break
            n = n.next
        if n.next is not None:    #  middle element delete karega except last node
            n.next.prev = n.prev
            n.prev.next = n.next
        else:                               # last node element check karke delete karega
            if n.data==x:
                n.prev.next = None
            else:
                print("x is not present in dll!")
    

    


LL1 = DoublyLL()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.delete_by_value(50)
LL1.print_LL()
