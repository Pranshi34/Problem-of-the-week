class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countUnivalSubtrees(root):
    count = [0]   

    def isUnival(node):
        if not node:
            return True   

        left_unival = isUnival(node.left)
        right_unival = isUnival(node.right)

        if not left_unival or not right_unival:
            return False

        if node.left and node.left.val != node.val:
            return False

        if node.right and node.right.val != node.val:
            return False
        count[0] += 1
        return True

    isUnival(root)
    return count[0]
