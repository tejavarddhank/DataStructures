class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        res = collections.deque()
        while stack:
            u = stack.pop()
            res.appendleft(u.val)
            if u.left:
                stack.append(u.left)
            if u.right:
                stack.append(u.right)
        return list(res)
