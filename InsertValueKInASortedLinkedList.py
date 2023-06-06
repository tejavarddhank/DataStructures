#insertValueKInASortedLinkedList

#defining node class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
#defining LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    #function to insert at end
    def insert_node_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        
        curr.next = new_node
        
    #function to print a linked list
    def print(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
    
    # function to insert a node with value k in a sorted linked list
    def InsertValueKInASortedLinkedList(self, data):
        new_node = Node(data)
        if self.head == None or data<self.head.data :
            new_node.next = self.head
            self.head = new_node
            return
        temp=self.head
        while temp.next != None and temp.next.data < data:
            temp = temp.next
            
        new_node.next=temp.next
        temp.next=new_node
        
                
            

linked_list = LinkedList()
for i in range(10):
    linked_list.insert_node_at_end(i)

linked_list.print()

linked_list.InsertValueKInASortedLinkedList(3)
linked_list.print()
linked_list.InsertValueKInASortedLinkedList(-1)
linked_list.print()
linked_list.InsertValueKInASortedLinkedList(10)
linked_list.print()
    
