"""
The problem
- Given exchange rates between n currencies, decide whether some sequence of trades starts and 
  ends in the same currency with more money than it began. A common follow-up is to return that sequence.

Pattern signals
- "Cycle whose product exceeds 1" becomes, after taking logs, a cycle whose sum is negative.
- Negative-cycle detection is the one thing Bellman-Ford does that Dijkstra cannot.
- No source is given, so the cycle can be anywhere and you need a way to reach all nodes.

Plan of attack
- Build edges with weight -log(rate) because
  - current exchange is performed via multiplication
  - bellman-ford only support additions
  - to convert multiplication into additions, we use log, where
    - log(rate1 x rate2) = log(rate1) + log(rate2)
  - why negative log(rate)?
    - log(rate > 1) is a postive number (gaining)
    - log(rate < 1) is a negative number (losting)
    - a cycle is profitable when it "gaining" edges outweight is "losing" ones
    - Bellman-ford detects a cycle when sum is negative, therefore
      - turn "gaining" edges into negative by negating the value
      - when sum is negative indicates "arbitrage exists", aka, negative cycle
- Initialize every cost to 0. This acts as a virtual source connected to all currencies.
- Relax all edges for n rounds. If the n-th round still improves something, a negative cycle exists.
- To recover the cycle, keep a parent array. From the last relaxed node, step back n times to land inside the cycle, 
  then follow parents until the node repeats.

Example:
- Take USD→EUR at 0.9, EUR→GBP at 0.9, GBP→USD at 1.3.

Brute force
- Enumerate every simple cycle (every ordered subset of currencies), multiply the rates, and check for a product above 1. That is O(n!) cycles.

From brute force to optimal
- You don't need every cycle, only whether a profitable one exists. If no negative cycle exists, costs settle within n-1 rounds. 
- Any improvement in round n therefore proves a cycle. The log transform is only there to turn products into sums; 
- you can equally keep the products and relax on amount[u] * rate > amount[v] with all values starting at 1.

Complexity
- Time: O(V·E), which is O(V³) when every pair has a rate
- Space: O(V + E)

What to say in the interview:
- Why −ln? A loop is profitable when its rates multiply to more than 1. 
  - Taking −ln turns that into "edge weights sum to less than 0", which is a negative cycle
- Why n − 1 passes? A shortest path without cycles uses at most n − 1 edges. 
  - If an edge still relaxes after that, some path keeps getting shorter forever, so a negative cycle exists.
- ∞ or zeros? Starting from one source only finds loops that source can reach. 
  - Starting every cost at 0 acts like a virtual source with a free edge to each currency, so every loop is found. Try both on the third market above.
- Cost. O(V·E) time, O(V) space. With a full rate matrix E = V², so O(V³). 
  - Compare floats with a small epsilon so rounding noise is not reported as profit.
"""
import math
from typing import Optional

"""rates: list of (from_currency, to_currency, rate), e.g. ("USD", "EUR", 0.9).
    Returns a cycle like ["USD", "EUR", "GBP", "USD"], or None.
"""

def find_arbitrage(rates: list[tuple[str, str, float]]) -> Optional[list[str]]:
   # build a set of currency names
   unique_names:set[str] = set()
   for u,v, _ in rates:
       unique_names.add(u)
       unique_names.add(v)
    
   currency_names:list[str] = sorted(unique_names)
   currency_indexes:dict[str, int] = {currency_name:i for i, currency_name in enumerate(currency_names)}

   # now build the edges using indexes
   edges: list[tuple[int,int, float]] = [
       (currency_indexes[from_curr_name], currency_indexes[to_curr_name], -math.log(rate)) for from_curr_name, to_curr_name, rate in rates if rate > 0
   ]

   # now the bellman-ford algorithm
   currency_no = len(currency_names)
   # cost[i] = -log(best amount of currency i reachable so far), starting from 1 unit
   # Lower cost = more of that currency. All start at 0.0 (log(1) = 0): we start holding 1 unit of each.
   cost: list[float] = [0.0] * currency_no
   # to keep track of the parent list so we can trace back the loop if there is one
   parent: list[int] = [-1] * currency_no
   # tolerance for float-rounding noise in the -log sums (see relaxation comment below)
   EPS: float = 1e-12

   last_node = -1
   for _ in range(currency_no): # n rounds: n-1 to settle, plus 1 to detect a cycle
       last_node = -1
       for from_index, to_index, weight in edges:   # weight = -log(rate)
           # Relaxation: is going to `to` through `from` cheaper than the best path found so far?
           # In currency terms: does converting via `from` give MORE units of `to`?
           #   (smaller sum of -log(rate)  <=>  larger product of rates)
           # EPS ignores float-rounding noise, so break-even cycles aren't reported as profit.
           # Any improvement in the final (n-th) round means a negative cycle, i.e. arbitrage.
           if cost[from_index] + weight < cost[to_index] - EPS:
               cost[to_index] = cost[from_index] + weight
               parent[to_index] = from_index
               last_node = to_index
       if last_node == -1:  # no changes, therefore no negative cyles
        return None

   # After the n-th round, last_node is the last node whose cost improved, that proves a negative cycle exists
   # last_node can hang off the cycle
   # step back until inside the cycle
   # make sure the cycle-tracing code starts from a node that's actually on the cycle
   for _ in range(currency_no):
      last_node = parent[last_node]

   cycle: list[int] = [last_node]
   curr: int = parent[last_node]

   while curr != last_node:
      cycle.append(curr)
      curr = parent[curr]

   cycle.append(last_node)
   # reverse the list in place, while cycle[::-1] builds a new list, this works for any sequence (lists, strings, tuples)
   # The choice usually comes down to whether you need the original list:
   cycle.reverse()

   return [currency_names[i] for i in cycle]


def same_cycle(a: Optional[list[str]], b: Optional[list[str]]) -> bool:
    print("^^^^^^^^^^^ same cycle ^^^^^^^^^^^^^")
    if a is None or b is None:
        return a == b
    # The returned cycles repeat the first currency at the end to show the loop closing
    a, b = a[:-1], b[:-1]          # drop the repeated closing node
    if len(a) != len(b):
        return False

    for i in range(len(a)):
        back_part = a[i:]
        front_part = a[:i]
        print(f"back part: {back_part} front part: {front_part}")
        if back_part + front_part == b:
           return True
    
    return False

    #return any(a[i:] + a[:i] == b for i in range(len(a)))

def test_find_arbitrage(rates:list[tuple[str, str, float]], expected:Optional[list[str]]) -> None:
   print(f"\n{'>>' * 6} test_find_arbitrage Arbitrage {'<<' * 6}")
   for from_curency, to_currency, rate in rates:
      print(f"{from_curency} -> {to_currency}: {rate}")
   print("\n")
   actual:Optional[list[str]] = find_arbitrage(rates)
   print(f"expected: {expected}\n  actual: {actual}")
   assert same_cycle(actual, expected), f"Expected {expected}, but got {actual}"
   

if __name__ == "__main__":
   print(f"\n{'*' * 6} Find Arbitrage {'*' * 6}")

   # there is an arbitrage
   test_find_arbitrage([("USD", "EUR", 0.9), ("EUR", "GBP", 0.9), ("GBP", "USD", 1.3)], 
                       ["USD", "EUR", "GBP", "USD"])

   # there is an arbitrage
   mispriced = [
        ("USD", "EUR", 0.92),
        ("USD", "JPY", 150),
        ("EUR", "GBP", 0.87),
        ("GBP", "USD", 1.27),
        ("GBP", "JPY", 189),
        ("EUR", "USD", 1.08),
        ("JPY", "USD", 0.0066),
   ]
   test_find_arbitrage(mispriced, ["USD", "EUR", "GBP", "USD"])

   # Fair market: same as above, but GBP -> USD is 1.24 (no arbitrage)
   fair = [
        ("USD", "EUR", 0.92),
        ("USD", "JPY", 150),
        ("EUR", "GBP", 0.87),
        ("GBP", "USD", 1.24),
        ("GBP", "JPY", 189),
        ("EUR", "USD", 1.08),
        ("JPY", "USD", 0.0066),
    ]
   test_find_arbitrage(fair, None)

   # Loop USD can't reach: GBP -> JPY -> EUR -> GBP = 1.0195
   unreachable = [
    ("EUR", "USD", 1.08),
    ("EUR", "GBP", 0.87),
    ("GBP", "JPY", 189),
    ("JPY", "EUR", 0.0062),
    ("JPY", "USD", 0.0066),
   ]
   test_find_arbitrage(unreachable, ["GBP","JPY","EUR","GBP"])