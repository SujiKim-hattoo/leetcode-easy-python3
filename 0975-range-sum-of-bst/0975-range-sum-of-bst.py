# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        total_sum = 0
       
        # Step 1: Create a temporary list (stack) to explore TreeNode.
        # Even though we can directly write [root], we assign it to a variable (stack) for clarity.
        stack = [root]  # Start with the root node only.

         # Step 2: Loop until there are no more nodes left to visit
        while stack:
            node = stack.pop()  # Get the most recent node (LIFO: last in, first out)
            # case1) None value
            if node is None:
                continue  # Skip if the node is null (e.g., root.right might be None)

            # case2) Value existed
            # If node value is within [low, high] -> add to total_sum
            if low <= node.val <= high:
                total_sum += node.val

            # Step 3: Add left and right children to the stack if they exist.
            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return total_sum