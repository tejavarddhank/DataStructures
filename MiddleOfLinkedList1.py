# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        if head == None:
            return -1
        temp1 = head
        temp2 = head
        while temp2.next!=None and temp2.next.next != None:
            temp1=temp1.next
            temp2=temp2.next.next
    
        return temp1.data
#{ 
 # Driver Code Starts

       
