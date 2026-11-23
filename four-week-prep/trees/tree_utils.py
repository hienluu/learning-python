class Node:
    def __init__(self, val: int, left: "Node | None" = None, right: "Node | None" = None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(edges: dict[int, tuple[int | None, int | None]]) -> tuple[Node, dict[int, Node]]:
    """Build any binary tree from {parent: (left, right)}. Returns (root, {value: node})."""
    # every value that appears as a child
    children = {c for pair in edges.values() for c in pair if c is not None}
    nodes: dict[int, Node] = {v: Node(v) for v in set(edges) | children}

    for parent, (l, r) in edges.items():
        nodes[parent].left = nodes[l] if l is not None else None
        nodes[parent].right = nodes[r] if r is not None else None

    # the root is the only parent that is never someone's child
    root_val = next(v for v in edges if v not in children)
    return nodes[root_val], nodes


def insert_bst(root: Node | None, val: int) -> Node:
    """Insert val into the BST rooted at root and return the root. Duplicates are ignored."""
    if root is None:
        return Node(val)
    curr = root
    while True:
        if val < curr.val:
            if curr.left is None:
                curr.left = Node(val)
                return root
            curr = curr.left
        elif val > curr.val:
            if curr.right is None:
                curr.right = Node(val)
                return root
            curr = curr.right
        else:
            return root  # already in the tree


def create_bst(values: list[int]) -> tuple[Node | None, dict[int, Node]]:
    """Build a BST by inserting values in the given order. Returns (root, {value: node}).

    The order controls the shape:
      [8, 4, 12, 2, 6, 10, 14] -> balanced
      [1, 2, 3, 4]             -> skewed right (like a linked list)
    """
    root = None
    for v in values:
        root = insert_bst(root, v)
    return root, _index_nodes(root)


def create_balanced_bst(values: list[int]) -> tuple[Node | None, dict[int, Node]]:
    """Build a height-balanced BST from any values by always picking the middle as the root."""
    vals = sorted(set(values))

    def build(lo: int, hi: int) -> Node | None:
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        node = Node(vals[mid])
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    root = build(0, len(vals) - 1)
    return root, _index_nodes(root)


def _index_nodes(root: Node | None) -> dict[int, Node]:
    """Map each value to its node, so tests can pass real nodes as p and q."""
    nodes: dict[int, Node] = {}
    stack = [root] if root else []
    while stack:
        node = stack.pop()
        nodes[node.val] = node
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return nodes


def inorder(root: Node | None) -> list[int]:
    """In-order values. For a BST this is sorted, which makes a handy sanity check."""
    out: list[int] = []

    def dfs(node: Node | None) -> None:
        if node:
            dfs(node.left)
            out.append(node.val)
            dfs(node.right)

    dfs(root)
    return out
