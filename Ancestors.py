class Solution:
    def Ancestors(self, root,target):
        '''
        :param root: root of the given tree.
        :return: None, print the space separated post ancestors of given target., don't print new line
        '''
        #code here
        m={}

        q=[]
        q.append(root
        while q:
            temp=q.pop()
            
            if temp.left:
                m[temp.left.data]=temp.data
                q.append(temp.left)
            
            if temp.right:
                m[temp.right.data]=temp.data
                q.append(temp.right)

        return m
