class Node:
    def __init__(self, key:int, value:int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1) # dummy head
        self.tail = Node(-1, -1) # dummy tail
        # initialize the head and tail to point to each other
        self.head.next = self.tail
        self.tail.prev = self.head

    def _move_to_head(self, node: Node) -> None:
        # add new node right after dummyhead
        """Insert a node right after the dummy head."""        
        node.next = self.head.next
        node.prev = self.head        
        self.head.next.prev = node
        self.head.next = node
        

    def _remove_node(self, node: Node) -> None:
        # remove an existing node from the linked list
        #print(f"Removing node with key: {node.key}, value: {node.value}")
        prev_node = node.prev
        next_node = node.next
        #print(f"next_node - expacting tail: {next_node.key if prev_node else None})")
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = None
        node.next = None

    def _pop_tail(self) -> Node:
        # remove the node right before the dummy tail, this is the lest recently used node
        """Remove and return the node right before the dummy tail."""
        if self.tail.prev != self.head:
            tail_node = self.tail.prev                    
            self._remove_node(tail_node)
            return tail_node
        return None

    def walk_head_to_tail(self) -> None:
        # helper function to walk through the linked list from head to tail, for debugging purposes
        print("--- Walking through the linked list from head to tail ---")
        current = self.head.next       
        while current != self.tail:
            print(f"Key: {current.key}, Value: {current.value}")
            current = current.next

        print("--- End of linked list ---")


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        #print(f"get({key})")
        node = self.cache[key]
        self._remove_node(node)
        self._move_to_head(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        #print(f"put({key}, {value})")
        # if the key already exists, update the value and move it to the head
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._move_to_head(node)
        else:
            # if the key does not exist, create a new node and add it to the head
            new_node = Node(key,value)
            self.cache[key] = new_node            
            self._move_to_head(new_node)

        # evict if exceeds capacity
        if len(self.cache) > self.capacity:
            # get the tail node, this is why the doubled linked list node needs
            # both key and value, because we need the key to remove it from the cache
            tail = self._pop_tail()
            if tail:
                #print(f"Evicting key: {tail.key}, value: {tail.value}")
                del self.cache[tail.key]




def test2():
    print("\n======== Test 2: Updating existing keys and checking LRU order...\n")
    cache = LRUCache(2)
    
    cache.put(1, 1)
    #print(f"expecting get(1) = 1, got: {cache.get(1)}") # returns 1
    cache.walk_head_to_tail() # should show key 3 as most recent, then key 1    

    cache.put(2, 2)
    #print(f"expecting get(2) = 2, got: {cache.get(2)}") # returns 1
    cache.walk_head_to_tail() # should show key 3 as most recent, then key 1
    
    print(f"expecting get(1) = 1, got: {cache.get(1)}") # returns 1
 
    cache.put(3, 3) # evicts key 1    
    cache.walk_head_to_tail() # should show key 3 as most recent, then key 1
    print(f"expecting get(2) = 2, got: {cache.get(2)}") # returns 2
 
    cache.put(4, 4) # evicts key 2

    print(f"expecting get(1) = -1, got: {cache.get(1)}") # returns -1
    print(f"expecting get(3) = 3, got: {cache.get(3)}") # returns -1
    print(f"expecting get(3) = 4, got: {cache.get(4)}") # returns -1

    cache.walk_head_to_tail()
 

def test1():
    print("\n======== Test 1: Updating existing keys and checking LRU order...\n")
    cache = LRUCache(2)
    cache.put(1, 10)
    print(f"expecting get(1) = 10, got: {cache.get(1)}") # returns 10

    cache.put(2, 20)
    cache.put(3, 30) # evicts key 1

    print(f"expecting get(2) = 20, got: {cache.get(2)}") # 

    print(f"expecting get(1) = -1, got: {cache.get(1)}") # returns -1 (not found)

if __name__ == "__main__":
    test1()
    test2()
    