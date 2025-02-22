# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        # Stack to keep track of nodes at each depth
        stack = []
        i = 0
        
        while i < len(traversal):
            # Count dashes to determine depth
            depth = 0
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1
            
            # Get node value
            value = 0
            while i < len(traversal) and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            
            # Create new node
            node = TreeNode(value)
            
            # Adjust stack based on depth
            while len(stack) > depth:
                stack.pop()
            
            # Connect node to its parent
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            stack.append(node)
        
        # Return root node (first node in traversal)
        return stack[0]
        