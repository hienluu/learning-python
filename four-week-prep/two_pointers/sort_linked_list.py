"""
The problem: given the head of a singly linked list, return it sorted in ascending order. The follow-up asks for O(n log n) time, ideally with constant extra space. Values can repeat and be negative, and the list can be empty.  (integer value: negative, positive, 0, unique, repeated)

Pattern signals
- "Sort" plus "linked list": no random access, so quicksort's partitioning and heapsort are awkward. Merge sort only ever walks forward, so it fits.
- Merging two sorted lists is cheap and in place on linked lists, with no extra array like you'd need for arrays.
- It reuses this morning's tools. Reorder List found the middle with slow and fast pointers and then merged two halves. Here you do the same split and merge, but recursively, and the merge compares values instead of alternating.

Plan of attack
Questions to ask first:
- Can I change node values, or only links? Relinking is the clean answer either way.
- Does O(log n) recursion stack count as extra space? It decides top-down or bottom-up.
- Base case: what happens with 0 or 1 nodes? That's your base case.

Brute force: copy the values into a Python list, call sort(), then write them back. That's O(n log n) time and O(n) space. It's a fine opening line in an interview, but it dodges the point.
- From brute force to optimal:
- Merge sort needs two things: split in half, merge two sorted halves.
- Split: slow and fast pointers. Start fast at head.next so slow stops at the end of the left half on even lengths, then cut slow.next.
- Merge: a dummy head and a tail pointer, always attaching the smaller front node.
- Recurse on each half and merge the results. That gives O(n log n) with only the recursion stack.
- For true O(1) space, go bottom-up: merge runs of size 1, then 2, 4, 8 and so on, splicing them back together with a tail pointer.

Options explored
- Copy to array and sort: O(n log n) time, O(n) space, trivial code. Low risk to write, but likely marked as missing the point.
- Top-down merge sort: O(n log n) time, O(log n) stack. Short, readable and the usual expected answer. Pick this unless they press on the follow-up.
- Bottom-up merge sort: O(n log n) time, O(1) space. Meets the follow-up, but the split and splice bookkeeping is where people make mistakes under time pressure. Mention it, and code it if asked.

Pitfalls and edge cases
- Forgetting to cut the list at the middle, which recurses forever on the same list.
- Starting fast at head on a two-node list: slow never moves, so the split leaves one half empty and the other unchanged. Start fast at head.next.
- In the merge, forgetting to attach whichever list still has nodes left over.

Test: empty list, one node, two nodes in each order, all equal values, already sorted, reverse sorted, negatives.

Complexity
- Time O(n log n): halving gives log n levels of recursion, and each level does O(n) total work across its splits and merges.
- Space O(log n): only the recursion stack, one frame per level. The merge relinks existing nodes and allocates just a dummy node. Bottom-up drops this to O(1).

"""
from linked_list_util import ListNode, create_linked_list, print_linked_list


def sort_linked_list(head:ListNode) -> ListNode:
    # base case: handle empty or single node LL
    if not head or not head.next:
        return head

    # find the middle and split LL in half
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # cut in half
    right = slow.next
    slow.next = None

    left_sorted = sort_linked_list(head)
    right_sorted = sort_linked_list(right)

    # merging 
    dummy = ListNode()
    tail = dummy
    while left_sorted and right_sorted:
        if left_sorted.val <= right_sorted.val:
            tail.next = left_sorted
            left_sorted = left_sorted.next
        else:
            tail.next = right_sorted
            right_sorted = right_sorted.next
        # advance tail
        tail = tail.next

    # two lists might have different length
    tail.next = left_sorted or right_sorted
    return dummy.next


def test_sort_linked_list(vals:list[int]) -> None:
    print(f"\n{'>' * 10} test_sort_linked_list: {vals} {'<' * 10}")
    head = create_linked_list(vals)
    print(">>>> before sorting")
    print_linked_list(head)

    print(">>>> after sorting")
    new_head = sort_linked_list(head)
    print_linked_list(new_head)



if __name__ == "__main__":
    print(f"\n{'>' * 10} sort_linked_list {'<' * 10}")

    test_sort_linked_list([])
    test_sort_linked_list([1])
    test_sort_linked_list([1,5])
    test_sort_linked_list([5,1])
    test_sort_linked_list([1, 5, 3])
    test_sort_linked_list([5, 4, 3, 2, 1])
    test_sort_linked_list([2, 4, 3, 5, 1, 6])

    # all equals
    test_sort_linked_list([2, 2])
    test_sort_linked_list([2, 2,2])
    test_sort_linked_list([2, 2,2,2])
    test_sort_linked_list([5, 1, 3, 2, 1])
    test_sort_linked_list([1, 4, 3, 2, 1])

