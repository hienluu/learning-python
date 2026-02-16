# Max Stack implementation using a doubly linked list and treemap (sorted_dict)
from sortedcontainers import SortedDict

class DoublyLinkedNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self) -> str:
        return f"DoublyLinkedNode(value={self.value}, next={self.next}, prev={self.prev})"

class MaxStack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sorted_dict: SortedDict[int, list[DoublyLinkedNode]] = SortedDict()

    def push(self, value: int):
        node = DoublyLinkedNode(value)
        # if the stack is empty, set the head and tail to the new node
        # otherwise, add the new node to the end of the stack and update the tail
        if self.head is None:
            self.head = node
            self.tail = node            
        else:
            self.tail.next = node # connect prev. tail to new tail
            node.prev = self.tail # connect new tail to prev. tail
            self.tail = node      # update the tail to the new node

        

        # if the value is already in the sorted_dict, add the new node to the list
        if value in self.sorted_dict:
            self.sorted_dict[value].append(node)
        else:
            self.sorted_dict[value] = [node]

    def pop(self) -> int:
        if self.tail is None:
            raise Exception("Stack is empty")
        # disconnect the tail node from the list
        node = self.tail
        self.tail = self.tail.prev # update the tail to the previous node
        self.tail.next = None # disconnect the tail from the list
        # remove the node from the sorted_dict
        self.sorted_dict[node.value].remove(node)
        if len(self.sorted_dict[node.value]) == 0:
            del self.sorted_dict[node.value]
        return node.value

    def popMax(self) -> int:
        # what happens when nothing has been pushed yet?
        if self.tail is None:
            raise Exception("Stack is empty")

        # need to find the max value in the sorted_dict first - O(log n) operation
        max_value = self.sorted_dict.keys()[-1]
        # then we need to find the node with the max value in the list
        max_node = self.sorted_dict[max_value][-1] # the last node in the list is the max node
        # remove the node from the list
        self.sorted_dict[max_value].remove(max_node)

        if len(self.sorted_dict[max_value]) == 0:
            del self.sorted_dict[max_value]

        # if the node is the tail, update the tail to the previous node
        if max_node == self.tail:
            self.tail = max_node.prev
            if self.tail is not None: # if stack is empty as this point
                self.tail.next = None
        elif max_node == self.head:
            self.head = max_node.next
            if self.head is not None: # if stack is empty as this point
                self.head.prev = None
        else:
            # disconnect the node from the doubly linked list
            # the previous node's next should point to the next node        
            max_node.prev.next = max_node.next
            # the next node's previous should point to the previous node
            max_node.next.prev = max_node.prev


        # update the tail to the previous node
        return max_node.value
    def peek(self) -> int:
        return self.tail.value

    def peekMax(self) -> int: # O(log n) operation
        return self.sorted_dict.keys()[-1] # the last key in the sorted_dict is the max value

if __name__ == "__main__":
    print("Testing Max Stack")

    max_stack = MaxStack()
    max_stack.push(1)
    max_stack.push(3)
    max_stack.push(2)
    max_stack.push(5)
    max_stack.push(3)
    max_stack.push(4)
    max_stack.push(5)
    max_stack.push(2)

    print(" --- peek and peekMax ---")
    print("peek() -> 2: ", max_stack.peek())
    print("peekMax() -> 5:", max_stack.peekMax())

    print(" pop and the examine the peek and peekMax")
    print("pop() -> 2: ", max_stack.pop())
    print("peek() -> 5: ", max_stack.peek())
    print("peekMax() -> 5:", max_stack.peekMax())

    print(" pop and the examine the peek and peekMax")
    print("pop() -> 5: ", max_stack.pop())
    print("peek() -> 4: ", max_stack.peek())
    print("peekMax() -> 5:", max_stack.peekMax())

    print("push 6 and examine the peek and peekMax")
    max_stack.push(6)
    print("peek() -> 6: ", max_stack.peek())
    print("peekMax() -> 6:", max_stack.peekMax())

    print("popMax 6 and examine the peek and peekMax")
    print("popMax() -> 6: ", max_stack.popMax())
    print("peek() -> 4: ", max_stack.peek())
    print("peekMax() -> 5:", max_stack.peekMax())

    print("popMax 5 and examine the peek and peekMax")
    print("popMax() -> 5: ", max_stack.popMax())
    print("peek() -> 4: ", max_stack.peek())
    print("peekMax() -> 4:", max_stack.peekMax())





