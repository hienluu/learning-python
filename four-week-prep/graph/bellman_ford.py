# bellman_ford algorithm implementation

from graph import Graph

"""
Bellman_ford template.

Variation of this problem:
For each problem, ask four questions:

- What is the initial value? It is the identity of the operation: 0 for sums, 1 for products.
- What is the relaxation? Either + with <, or * with >.
- How many rounds, and do they need to be isolated from each other? A round count is a limit on the number of edges only if each round reads from a snapshot.
- What does an extra round tell me? If anything still improves after n-1 rounds, there is a negative cycle.

"""
def bellman_ford(edges: dict[int, tuple[int,int]]) -> list[int]:
    n = len(edges)
    dist:list[int] = [float('inf')] * n

    for _ in range(n-1):  # outer loop: by n-1 times (n is # vertices)
        changed = False
        for u, v, w in edges: # inner loop: go through all vertices each time
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break


if __name__ == "__main__":
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

    g = Graph()
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    print(g.bellman_ford(0))