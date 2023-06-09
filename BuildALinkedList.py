#defining node class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
#defining LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        
    #function to insert at beginning
    def insert_node_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    #function to delete at beginning
    def delete_node_at_beginning(self):
        if self.head is None:
            print("LinkedList is empty")
            return

        self.head = self.head.next
    
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
        
    #function to delete at end 
    def delete_node_at_end(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        
        curr = self.head
        while curr.next is not None:
            curr = curr.next

        curr.next = None

    def print(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next

linked_list = LinkedList()
linked_list.print()
linked_list.insert_node_at_beginning(0)
linked_list.print()
linked_list.insert_node_at_beginning(1)
linked_list.print()
linked_list.insert_node_at_end(3)
linked_list.print()
linked_list.delete_node_at_beginning()
linked_list.print()
linked_list.delete_node_at_end()
linked_list.print()
