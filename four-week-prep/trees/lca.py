"""
The problem: you get the root of a binary tree (not a search tree) and two nodes p and q that are both in it. Return their lowest common ancestor, meaning the deepest node that has both p and q in its subtree. A node counts as its own ancestor, so if p sits under q, the answer is q.

Pattern signals
- "Ancestor", "subtree contains" and "deepest node such that" all point to a postorder DFS, where each node decides after hearing from its children.
- No ordering to use, so you can't steer left or right the way you would in a BST (#235). That's the stretch here: the answer has to bubble up from below.
- This morning's problem was a repeat of #143, so I held it back. This one opens Trees today, and it's a good first tree problem because the "what does my recursion return?" question is the whole game.

Plan of attack

Questions to ask before coding:
- Are p and q guaranteed to be in the tree? (Yes here, and that matters a lot.)
- Are values unique? Compare nodes, not values, to be safe.
- Can p equal q? Then the answer is that node.

Brute force: 
- find the root to p path and the root to q path with DFS, then walk both lists together until they split. 
- The last shared node is the answer. 
- That's O(n) time but two traversals plus O(h) to O(n) extra lists.

Getting to the optimal idea:
- Ask what each subtree could tell its parent: "I found p", "I found q", "I found both" or "nothing".
- Notice you can squash that into one return value: return the node if this subtree contains p or q, or None otherwise.
- If a node is p or q, return it right away. Anything below it doesn't change the answer, because either the other node is below it (so it's the LCA) or elsewhere (so a higher node will be).
- If the left and right calls both come back non-None, p and q are split across this node, so this node is the LCA.
- If only one side is non-None, pass it up. It's either one of the targets or an LCA already found lower down.

Options explored
- Recursive postorder (optimal): O(n) time, O(h) stack, about ten lines. Lowest interview risk once you can explain the return value.
- Parent pointers plus a set: BFS or iterative DFS to record each node's parent until p and q are both seen, then put p's ancestors in a set and walk up from q. O(n) time and space, no recursion depth issue, but more code and more bookkeeping.
- Two root paths (brute force): easy to reason about and fine as a fallback, but it's the most code and two passes.

Pitfalls and edge cases
- Returning early when root is p or q is correct only because both are guaranteed present. If that guarantee goes away (LeetCode #1644), you need to count how many you actually found.
- Comparing by .val instead of identity breaks with duplicate values.
- Python's default recursion limit (about 1000) can fail on a skewed tree with many nodes. Mention it, and offer the iterative parent-pointer version.
- Test: p is q's ancestor, p and q are siblings, p or q is the root, a fully skewed tree, and p equal to q.

Complexity
- Time O(n): each node is visited at most once, and each visit does constant work (two calls and a comparison).
- Space O(h): the call stack goes as deep as the tree. That's O(log n) for a balanced tree and O(n) for a skewed one. No other data structures.


"""
from tree_utils import Node, create_binary_tree

def lca(node:Node, p:Node, q:Node) -> Node:
    # base cases
    if not node:
        return node

    if node is p or node is q:
        return node

    left = lca(node.left, p, q)
    right = lca(node.right, p, q)

    # found lca when found both left and right are not None
    if left and right:
        return node

    # last case is when found either p or q
    """
    Python's or doesn't return True or False. It returns one of the two values it was given:
        - if left is truthy, it returns left
        - otherwise it returns right, whatever right is
    """
    return left or right
    
def test_lca(root:Node, p:Node, q:Node, expected:Node):
    print(f"\n{'>' * 6} test_lca: looking for(p: {p.val}, q:{q.val}) {'<'* 6}")
    result = lca(root, p, q)
    print(f"result: {result.val}, expected: {expected.val if expected is not None else None}")
    assert result == expected, f"Expected {expected}, but got {result}"



if __name__ == "__main__":
    print(f"\n{'>' * 6} LCA {'<'* 6}")

    edges:dict[int,tuple[int,int]] = {  # parent: (left, right)
              1: (2, 3),
              2: (4, 5),
              3: (6, 7),
              4: (8, 9),
              5: (10, None),
              6: (11, 12),
              7: (13, None),
              10: (14, None),
              12: (15, None),
    }
    
    root, nodes = create_binary_tree(edges)

    print(f"root: {root.val}")

    # p is q's ancestor
    test_lca(root, nodes[5], nodes[10], nodes[5])

    # p and q are sibling
    test_lca(root, nodes[8], nodes[9], nodes[4])

    # root is lca
    test_lca(root, nodes[9], nodes[15], nodes[1])

    # p is root 
    test_lca(root, nodes[1], nodes[15], nodes[1])

    # q is root 
    test_lca(root, nodes[13], nodes[1], nodes[1])

     # p and q are the same
    test_lca(root, nodes[13], nodes[13], nodes[13])

    # q doesn't exist in the tree
    #test_lca(root, nodes[13], Node(99), None)