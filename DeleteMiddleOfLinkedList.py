#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''
    
    #code here
    temp1 = head
    temp2 = head
    prev = None
    
    while temp2!= None and temp2.next!=None:
        prev=temp1
        temp1=temp1.next
        temp2=temp2.next.next
    
    prev.next = temp1.next
    return head



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n=int(input())
        arr1 = [int(x) for x in input().split()]
        ll = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll.insert(nodeData, tail)

        res=deleteMid(ll.head)
        printList(res)
# } Driver Code Ends
