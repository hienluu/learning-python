"""
The problem: given the head of a singly linked list L0 → L1 → … → Ln, rearrange it in place to L0 → Ln → L1 → Ln-1 → L2 → … You can't change node values, only the links, and you return nothing.

Pattern signals
- "Singly linked list" plus "in place": no random access, so the tools are pointer moves, not indexing.
You need the last node next to the first, which means walking from the end. That hints at reversing part of the list.
"Alternate from front and back" is a merge of two halves.

Plan of attack
- Questions to ask first: can I use extra memory? What about 0, 1 or 2 nodes? Is the list length even or odd, and where does the middle node end up?

Brute force: copy every node into a Python list, then use two indices (i from the front, j from the back) to relink them alternately. That's O(n) time and O(n) space, and it's a fine first answer to say out loud.
- From there to optimal: the array only exists so you can reach the back. Instead, 
- split the list at the middle, 
- reverse the second half so its "back" becomes a "front", 
- weave the two halves together. 

Each of those is a classic linked list move you already know:
- Find the middle with slow and fast pointers.
- Cut the list there and reverse the second half.
- Merge the two halves by alternating nodes.

Options explored
- Array of nodes + two pointers: O(n) time, O(n) space. Simplest to code and easy to get right, but an interviewer will likely ask for O(1) space next.
- Stack of the second half: push nodes, pop to interleave. Still O(n) space, and no simpler than the array, so it's mostly a stepping stone.
- Middle, reverse, merge: O(n) time, O(1) space. The expected answer. More code, so the risk is pointer bugs, not the idea.

Pitfalls and edge cases
- Forgetting to cut the first half (slow.next = None). This creates a cycle and the merge loops forever.
- Off by one at the middle: with fast starting at head, the first half keeps the extra node on odd lengths, which is what you want.
- Losing the rest of a list during the merge. Save both .next pointers before relinking.
- Test with: empty list, 1 node, 2 nodes, odd length [1,2,3,4,5], even length [1,2,3,4].

Complexity
- Time O(n): finding the middle is about n/2 steps, reversing the second half is n/2, and the merge is n/2. Constant passes over the list add up to O(n).
- Space O(1): only a handful of pointers, no matter how long the list is. (The array approach pays O(n) for the copy.)


"""
from typing import Optional

from linked_list_util import ListNode, create_linked_list, print_linked_list

def reorder_linked_list(head:ListNode) -> None:
    # two nodes or less, no need to redorder (edge case)
    if not head or not head.next:
        return head # 0 or 1 node

    # find the middle by using two pointers where one moves at 2x speed of the other
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # cut the list and reverse the second half
    second = slow.next
    slow.next = None

    # reversing the second
    prev = None
    while second:
        next = second.next
        second.next = prev
        prev = second
        second = next

    # prev points the new head
    second = prev
    print(f" print out the second (starting from the middle) after reversing")
    print_linked_list(second)

    # weave
    """
      Why: after the split, the first half has the same number of nodes as the second half, or one more:
        ┌───────────┬────────────┬────────────────────────┐
        │   List    │ First half │ Second half (reversed) │
        ├───────────┼────────────┼────────────────────────┤
        │ [1,2,3,4] │ 1 → 2      │ 4 → 3                  │
        ├───────────┼────────────┼────────────────────────┤
        │ [1,5,10]  │ 1 → 5      │ 10                     │
        └───────────┴────────────┴────────────────────────┘

        Each pass of the weave loop uses one node from each half, so the loop has to stop 
        when the shorter half runs out. **That's always second**
    """
    first = head
    while second:
        # save the next nodes first
        tmp1, tmp2 = first.next, second.next
        # weave
        first.next = second
        second.next = tmp1
        # update the first and second to next nodes
        first, second = tmp1, tmp2

    return

"""
The standard approach is iterative and uses three pointers: prev, curr and nxt. 
You walk the list once and flip each next pointer so it points back instead of forward.

  Steps

  1. Start: prev = None and curr = head. None will become the new tail's next.
  2. Loop while curr is not None:
     a. Save the next node: nxt = curr.next. 
        - Do this before changing anything, or you lose the rest of the list.
     b. Reverse the pointer: curr.next = prev.
     c. Move prev forward: prev = curr.
     d. Move curr forward: curr = nxt.
  3. Return prev. When the loop ends, 
     - curr is None and prev is the old tail, which is now the new head.
"""
def reverse_linked_list(head:ListNode) -> ListNode:
    prev, current = None, head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev





def test_reorder_linked_list(vals:list[int]) -> None:
    print(f"{'>' * 6} test_reorder_linked_list: {vals}  {'<' * 6}")
    ll1 = create_linked_list(vals)
    print(f"{'>' * 6} before ordering")
    print_linked_list(ll1)
    reorder_linked_list(ll1)
    print(f"{'>' * 6} after reordering")
    print_linked_list(ll1)
    print("\n")

if __name__ == "__main__":
    print(f"\n{'>' * 6} Reorder Linked List {'<'* 6}")

    test_reorder_linked_list([1,5,10,15])
    test_reorder_linked_list([1,5,10])
    test_reorder_linked_list([1,5,10,15,25])

    