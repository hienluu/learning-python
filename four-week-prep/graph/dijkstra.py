import heapq

# Every heapq function keeps that rule true:
#   - heapq.heappush(heap, item) appends the item to the end. It then swaps the item with its parent until the parent is smaller ("sift up").
#   - heapq.heappop(heap) takes out heap[0], moves the last item to the front, and swaps it with its smaller child until the rule holds again
#     ("sift down"). Both operations take O(log n) time.
#   - heapq.heapify(lst) is the only function that converts an arbitrary list into a heap, in O(n) time.


def dijkstra(graph: dict[str, list[(str, int)]] , start: str) -> tuple[dict[str, int], dict[str, str]]:
    # distance from start to each node in the graph, initialize to infinity for each node
    dist: dict[str, int] = {node: float('inf') for node in graph}
    dist[start] = 0  # distance from start to itself is 0

    # previous node in the optimal path from source, initialize to None for each node
    prev: dict[str, str] = {node: None for node in graph} 

    # priority queue to store (distance, node) pairs
    heap: list[tuple[int, str]] = [(0, start)] 
    visited: set[str] = set() # set to keep track of visited nodes

    while heap:
        # get the node with the smallest distance
        curr_dist, curr_node = heapq.heappop(heap) 

        # have we already visited this node? If so, skip it
        if curr_node in visited:
            continue

        # mark the current node as visited
        visited.add(curr_node) 

        # iterate through the neighbors of the current node
        for neighbor, neighbor_dist in graph[curr_node]:
            if neighbor in visited:
                continue

            new_dist:int    = curr_dist + neighbor_dist
            # if the new distance is smaller than the previously recorded distance, update it
            if new_dist < dist[neighbor]:
                # update the distance and previous node for the neighbor
                dist[neighbor] = new_dist
                # keep track of the previous node for the neighbor to reconstruct the shortest path later
                prev[neighbor] = curr_node
                # add the neighbor to the priority queue with the updated distance
                heapq.heappush(heap, (new_dist, neighbor))
    
    return dist, prev


if __name__ == "__main__":
    graph: dict[str, list[tuple[str, int]]] = {
        "S": [("B", 2), ("A", 4)],
        "A": [("D", 2), ("C", 5)],
        "B": [("D", 8), ("A", 1)],
        "C": [("T", 3)],
        "D": [("T", 1), ("C", 1)],
        "T": [],
    }
    start_node = 'S'
    distances, previous = dijkstra(graph, start_node)
    print(distances)
    print(previous)

    # having fun with heapq.
    import heapq

    h = []
    for x in [5, 7, 9, 1, 3]:
        heapq.heappush(h, x)

    
    print(f"after pushing elements to heap: {h}")
    print("=====> popping elements from heap:")
    while h:
        print(heapq.heappop(h))

    print("=====> after popping elements from heap:")
    print(h)