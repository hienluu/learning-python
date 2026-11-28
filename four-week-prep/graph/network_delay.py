"""
The problem: n nodes are joined by one-way edges (directed graph), each with a travel time (with a weight). 
A signal leaves node k. How long until every node has it? Return -1 if some node never hears it.

Summary: the time for a signal starting at k to reach every node, which is the slowest node's 
  shortest arrival time, or -1 if some node can't be reached from k

Pattern signals
- Weighted, directed edges, and every weight is zero or more.
- "Time until all nodes receive it" is the shortest path from k to every node, then the largest of those.
- One source and many targets is the classic job for Dijkstra.

Plan of attack
- Ask first: Can weights be negative? (No, and that rules Dijkstra in.) Can the graph have cycles? (Yes.) Are nodes 1 to n? (Yes.)
- Brute force: try every path from k with DFS and keep the best time per node. Cycles and repeat visits make this exponential.
- Better: plain BFS finds fewest hops, not least time, so it fails as soon as weights differ.
- Key insight: if you always expand the closest node you haven't settled yet, its distance is final. With no negative edges, no later path can beat it.
- A min-heap of (time, node) hands you that closest node cheaply. 
- Pop it, settle it, push its neighbours with time plus edge weight.
- Answer: the largest settled time if all n nodes got settled, otherwise -1.

Options explored
- Dijkstra with a heap: O(E log V). The interview answer, short and expected.
- Bellman-Ford: relax every edge n-1 times, O(V·E). Easiest to write and copes with negative weights, but slower, and it signals you missed the cue.
- Floyd-Warshall: all pairs in O(V³). Fine here since n is at most 100, but it's overkill when there's a single source.

From brute force to optimal
- The DFS repeats the same relaxation, dist[u] + w < dist[v], in an uncontrolled order. Bellman-Ford imposes an order: relax every edge, and repeat n-1 times, 
  because a shortest path has at most n-1 edges. Dijkstra goes further: with non-negative weights, the closest unfinalized node can never be improved, 
  so each node is processed once.

Pitfalls and edge cases
- Skip a node popped a second time with a stale, larger time. This "lazy deletion" check is the bug people most often forget.
- Nodes are 1-indexed, so watch for off-by-one errors if you use arrays.
- Unreachable node: return -1, not the max of what you did reach.
- Edges are one-way. Don't add the reverse edge.
- n = 1 with no edges should return 0.
- A weight of 0 is allowed and must still work.

Complexity
- Time O(E log V): each edge can push one heap entry, so the heap holds at most E items. 
  Each push or pop costs log E, and log E ≤ 2·log V. Building the adjacency list adds O(E).
- Space O(V + E): the adjacency list holds E edges, the heap holds up to E entries and the dist map holds V nodes.
- Bellman-Ford: O(V·E) time, O(V) space.
- Dijkstra: O(E log V) time, O(V + E) space.

"""
from collections import defaultdict
import heapq
from math import inf

"""
#1 (Eager): Updates dist[v] the moment a shorter path to v is discovered during neighbor exploration. 
# Because dist holds tentative values, #1 requires a separate done set to know which nodes have been permanently settled
"""
def cal_network_delay_dijkstra_eager(times: list[list[int]], num_nodes: int, start_node: int) -> int:
    directed_graph = defaultdict(list)
    for u,v,w in times:
        directed_graph.get[u].append((v,w)) # value is a list of v and w

    # bookkeeping stuff
    dist: dict[int,int] = {start_node, 0}
    parent: dict[int, int] = {}
    done:set[int] = set()

    # queue
    heap:heapq = [(0, start_node)] # distance, start_node

    while heap:
        curr_time, curr_node = heapq.heappop(heap)
        if curr_node in done:
            continue

        done.add(curr_node)

        for v, w in directed_graph[curr_node]:
            if curr_time + w < dist.get(v, inf):
                dist[v] = curr_time + w
                heapq.heappush(heap, (curr_time + w, v))

    #return max(dist.values()) if len(done) == n else -1
    if len(dist) == num_nodes:
        return max(dist.values()) 
    else: 
        return -1

"""
This is the (Lazy) implementation: Only writes to dist[node] when node is popped from the heap for the first time. 
# Because Dijkstra guarantees the first pop of any node with non-negative edge weights is optimal, 
# dist simultaneously acts as the distance map and the visited/done set.
"""
def cal_network_delay_dijkstra_lazy(times: list[list[int]], num_nodes: int, start_node: int) -> int:
    # build the adjency list u -> [(v,w)...]
    directed_graph = defaultdict(list)
    for u,v,w in times:
        directed_graph[u].append((v, w)) # value is a list of v and w

    # dijkstra initialization block - distance and heap
    dist: dict[int, int] = {} # settled node -> shortest time for k
    parent: dict[int, int] = {} # node -> node it came from
    heap:heapq = [(0,start_node, None)] # (time so far, node, came_from_node)

    # w/ heap, loop until no more nodes to process
    while heap:
        curr_time, curr_node, prev = heapq.heappop(heap) #pop the head of the heap, including prev
        if curr_node in dist:  # stale entry, a shorter time already settled it
            continue
        dist[curr_node] = curr_time
        parent[curr_node] = prev # record the parent node
        

        for neighbor, weight in directed_graph[curr_node]:  # iterating through the list of values of each key
            if neighbor not in dist:
                heapq.heappush(heap, (curr_time + weight, neighbor, curr_node)) # curr_node is the prev node


    # now try to print the path
    largest_shortest_node = max(dist, key=dist.get)
    print_path(parent, largest_shortest_node, dist) 

    # every node must be reached; the last one to hear it sets the answer
    """
    What it does

    When the while heap: loop finishes, dist holds an entry only for nodes the signal actually reached, each
    mapped to its shortest arrival time from start_node. The block then asks two things.

    1. Did every node get the signal? (len(dist) == n)
    A node gets into dist only when it's popped off the heap, and it only gets onto the heap if some path
    leads to it from the start. Any node with no path from start_node never shows up in dist. So if dist has
    fewer than n entries, at least one node never heard the signal, and the problem says to return -1.

    2. If so, when did the last node get it? (max(dist.values()))
    The signal spreads along all paths at once. "Every node has it" happens when the slowest node finally
    receives it. That moment is the largest of the shortest arrival times, not their sum.

    Example

    Take the LeetCode case [[2,1,1],[2,3,1],[3,4,1]], n=4, k=2:
    - dist = {2: 0, 1: 1, 3: 1, 4: 2} has 4 entries, which equals n → max = 2

    Take [[1,2,1],[2,3,2]], n=4, k=1:
    - dist = {1: 0, 2: 1, 3: 3} has 3 entries, but n is 4. Node 4 was never reached → -1

    Why the count check matters

    Without the length check you'd return 3 in the second example, which is wrong. That's the pitfall your
    docstring calls out: "return -1, not the max of what you did reach." Dijkstra on its own only tells you
    about the nodes it reached. It says nothing about the ones it missed, so you have to check that yourself.
    """
    if len(dist) == num_nodes:
        return max(dist.values()) 
    else: 
        return -1

def print_path(parent:dict[int,int], target:int, dist:dict[int,int]) -> None:
    print("\n============= parent path =========")
    if target not in parent:
        print(f"target: {target} not in parent dictionary")
        return
    
    path:list[int] = []
    node = target
    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    print(f"target: {target}: path: {path} (time {dist[target]}) ")
    print("============= parent path =========\n")


#def cal_network_delay_bellman_ford(times: list[list[int]], num_nodes: int, start_node: int) -> int:
    # converto directed graph

def test_cal_network_delay_dijkstra(times:list[list[int]], num_nodes:int, start_node:int, expected:int):
    print(f"{'***' * 6} testing network delay {'***' * 6}")
    print(f"times: {times}")
    print(f"num_nodes: {num_nodes} start_node: {start_node}")
    actual = cal_network_delay_dijkstra_lazy(times, num_nodes, start_node)
    print(f"expected: {expected} actual: {actual}")
    assert actual == expected, f"expected: {expected} actual: {actual}"

if __name__ == "__main__":
    print(f"\n{'>>' * 6} network delay {'<<' * 6}")

    cases = [
        ([[1, 2, 1]], 2, 2, -1),                        # edge points into the source
        ([[1, 2, 1], [2, 3, 2]], 4, 1, -1),             # node 4 has no edges
        ([[1, 2, 1], [2, 1, 3]], 3, 1, -1),             # cycle, but node 3 isolated
        ([[3, 2, 1], [2, 1, 1]], 3, 1, -1),             # source has only incoming edges
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),   # standard LeetCode example
        ([], 1, 1, 0),                                  # single node, no edges
        ([[1, 2, 10], [1, 3, 1], [3, 2, 2]], 3, 1, 3),  # two-hop path beats direct edge
        ([[1, 2, 5], [1, 2, 2], [2, 3, 1]], 3, 1, 3),   # duplicate edges, cheaper wins
        ([[1, 2, 0], [2, 3, 0]], 3, 1, 0),              # zero-weight edges
        ([[1, 2, 1], [2, 3, 1], [3, 1, 1]], 3, 3, 2),   # cycle, source at highest label
    ]
    for i, (times, n, k, expected) in enumerate(cases):
        print(f"\n========= test case #{i} ==========")
        test_cal_network_delay_dijkstra(times, n, k, expected)
        