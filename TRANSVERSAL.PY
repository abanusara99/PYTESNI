class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder_traversal(root):
    if not root:
        return []

    stack = []
    output = []

    current = root

    while current or stack:
        if current:
            if current.right:
                stack.append(current.right)
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            if stack and current.right == stack[-1]:
                stack.pop()
                stack.append(current)
                current = current.right
            else:
                output.append(current.value)
                current = None

    return output

# Create the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Perform post-order traversal
result = postorder_traversal(root)
print(result)
