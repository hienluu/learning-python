
"""
You get the root of a binary tree and return whether it's a valid BST. Every node in a left subtree must be strictly less than the node above it, and every node in a right subtree strictly greater. That holds for the whole subtree, not just the direct children.

Pattern signals
- A recursive definition ("every node in the subtree") points to DFS that passes information down.
- "BST" plus "ordering" hints at in-order traversal, which visits a BST's values in sorted order.

Plan of attack
- Ask first: are duplicates allowed? (Here, no: strictly less and strictly greater.) Can values hit the 32-bit limits? (Yes, so don't use the int min/max as sentinels.)
- Brute force: for each node, scan its entire left subtree for the max and its right subtree for the min, then compare. That's O(n²) on a skewed tree.

The insight: instead of looking down, pass the allowed range down. The root can be anything. Going left tightens the upper bound to the parent's value, and going right tightens the lower bound.
- Each node then checks itself against (low, high) in O(1), and the whole tree takes one pass.

Options explored
- DFS with bounds: O(n) time, O(h) stack. It's clean, and most interviewers expect it.
- In-order traversal: values must strictly increase, so track the previous value. Also O(n), and the iterative version avoids the recursion limit. It's slightly easier to get wrong with the prev state.
- Collect in-order into a list, then check sorted: simplest to reason about, but it uses O(n) extra space. Fine as a warm-up, weaker as a final answer.

Pitfalls and edge cases
- Comparing only a node with its children. [5,4,6,null,null,3,7] passes that check but fails, because the 3 sits under the 5's right side.
- Using <= instead of <: [2,2,2] must return False.
- Sentinels: use float('-inf') and float('inf'), or None, not ±2³¹.

Test a single node, a fully skewed tree (the recursion depth), and a tree with values at the 32-bit extremes.

Complexity (DFS with bounds)
- Time O(n): each node is visited once and does constant work.
- Space O(h): the call stack holds one frame per level. That's O(log n) when the tree is balanced and O(n) when it's skewed.
"""
from tree_utils import Node, create_bst

"""
Every node in left subtree must be strictly less than the node above it.
Every node in a right subtree strictly greater

"""
def isBST(node: Node) -> bool:
    def dfs(node:Node, lo:int, hi:int) -> bool:
        if not node:
            return True

        # at current node, make sure it is within range > low and < hi
        if not (lo < node.val < hi):
            return False

        # left side: values must stay below this node
        # right side: values must stay above this node
        # both must be true for this BST to be valid
        return dfs(node.left, lo, node.val) and dfs(node.right, node.val, hi)

    return dfs(node, float('-inf'), float('inf'))

def test_isbst(node: Node, expected: bool) -> None:
    print(f"\n{'=' * 6} test_isbst: root: {node.val} {'='* 6}")
    result = isBST(node)
    print(f"result: {result} expected: {expected}")

if __name__ == "__main__":
    print(f"\n{'>' * 6} BST Validation {'<'* 6}")
    

    root, values = create_bst([8, 4, 12, 2, 6, 10, 14])
    test_isbst(root, True)

    root, nodes = create_bst([1, 2, 3, 4])
    test_isbst(root, True)
