#DeleteValueKInASortedLinkedList

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
    
    # function to delete a node with value k in a sorted linked list
    def DeleteValueKInASortedLinkedList(self, data):
        if self.head == None or data<self.head.data :
            print("K doesnt exist")
            return
        if self.head.data ==data:
            self.head=self.head.next
        temp = self.head
        while temp!=None and temp.next!=None:
            curr=temp
            temp=temp.next
            if temp.data==data:
                curr.next=temp.next
                return
            

linked_list = LinkedList()
for i in range(10):
    linked_list.insert_node_at_end(i)

linked_list.print()

linked_list.DeleteValueKInASortedLinkedList(3)
linked_list.print()
linked_list.DeleteValueKInASortedLinkedList(0)
linked_list.print()
linked_list.DeleteValueKInASortedLinkedList(9)
linked_list.print()
    
