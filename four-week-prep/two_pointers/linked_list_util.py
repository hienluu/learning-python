class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(vals:list[int]) -> ListNode:
    if not vals:
        return None

    tmp = None
    head = None
    for idx, val in enumerate(vals):
        
        if idx == 0:
            tmp = ListNode(val)
            head = tmp
        else:
            tmp.next = ListNode(val)
            tmp = tmp.next        

    return head

def print_linked_list(head:ListNode) -> None:
    tmp = head
    while tmp:
        print(f"{tmp.val}", end="->")
        tmp = tmp.next
    print("null")
