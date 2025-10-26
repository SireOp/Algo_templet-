from typing import Optional, Set, Dict, List


# --------------------------- TREE DFS ---------------------------

class TreeNode:
    """Simple binary tree node."""
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def dfs_tree(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    """
    Depth-First Search for a binary tree.
    Returns the node whose value == target, or None if not found.
    """
    if root is None:
        return None

    if root.val == target:
        return root

    # Search left subtree
    left = dfs_tree(root.left, target)
    if left is not None:
        return left

    # Search right subtree
    return dfs_tree(root.right, target)


# --------------------------- GRAPH DFS ---------------------------

def get_neighbors(node: int, graph: Dict[int, List[int]]) -> List[int]:
    """Helper to get neighbors from adjacency list."""
    return graph.get(node, [])


def dfs_graph(root: int, visited: Set[int], graph: Dict[int, List[int]]) -> None:
    """
    Depth-First Search for a graph.
    Prints nodes in DFS order.
    """
    print(root, end=" ")
    for neighbor in get_neighbors(root, graph):
        if neighbor in visited:
            continue
        visited.add(neighbor)
        dfs_graph(neighbor, visited, graph)


# --------------------------- MAIN TESTS ---------------------------

if __name__ == "__main__":
    print("TREE DFS Example:")
    # Build sample tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    target = 5
    result = dfs_tree(root, target)
    if result:
        print(f"Found node with value {result.val}")
    else:
        print("Target not found")

    print("\n\n🕸️ GRAPH DFS Example:")
    # Graph represented as adjacency list
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [],
        5: [],
        6: []
    }

    visited = {1}
    print("DFS traversal starting from node 1:")
    dfs_graph(1, visited, graph)
    print()  # newline