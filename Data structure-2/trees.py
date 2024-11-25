class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


def bfs_max(root):
    if root is None:
        return None  # Return None if the tree is empty

    # Initialize a queue for BFS
    queue = [root]
    max_value = -1
    while queue:
        current = queue.pop(0)  
        max_value = max(max_value, current.val)

        # Enqueue the left and right children if they exist
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return max_value

def dfs_max(root):
    if root is None:
        return -1  

    # Recursively find the maximum in the left and right subtrees
    left_max = dfs_max(root.left)
    right_max = dfs_max(root.right)

    # Return the maximum value among the current node, left subtree, and right subtree
    return max(root.val, left_max, right_max)

# Create the binary tree
root = Node(45)
firstNode = Node(36)
secondNode = Node(74)
thirdNode = Node(46)
fourthNode = Node(99)

root.left = firstNode
root.right = secondNode
secondNode.left = thirdNode
secondNode.right = fourthNode

# Call bfs_max and dfs_max and print the results
print("Maximum value in the tree (BFS):", bfs_max(root))
print("Maximum value in the tree (DFS):", dfs_max(root))

