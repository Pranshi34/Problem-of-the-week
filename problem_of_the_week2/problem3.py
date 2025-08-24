from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

def maxPathSum(root):
    max_sum = float('-inf')

    def helper(node):
        nonlocal max_sum
        if not node:
            return 0
        
        left = max(helper(node.left), 0)
        right = max(helper(node.right), 0)

        current = node.val + left + right
        max_sum = max(max_sum, current)

        return node.val + max(left, right)

    helper(root)
    return max_sum

values = input().split()
arr = [int(x) if x != "None" else None for x in values]

root = build_tree(arr)
print(maxPathSum(root))
