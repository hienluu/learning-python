# 4-Week Coding Interview Plan

Oct 17, 2026 · @Hien

## Strategy and reality check

The plan learns about 15 patterns, not 500 problems: 4 weeks, roughly 55 core problems in Python, from Sun Oct 18 to Sat Nov 14, ending with three timed mock interviews.

Starting rusty with 1–2 hours a day gives you about 45 hours total. That is enough to solve most unseen mediums if you study patterns deliberately, and to attempt some hards. No plan can promise 99.9%: the problem you draw and the interviewer both vary. The goal is that a medium feels familiar, so a bad draw costs you one round, not the loop.

Three rules make the hours count:

- **Pattern first, problem second.** Every problem gets tagged with the pattern it uses. In the interview you will recognize the pattern, not the problem.
- **25-minute cap.** Stuck after 25 minutes means read the solution, understand it, close it, and re-code it from memory. Struggling for 2 hours teaches less.
- **Redo beats new.** A problem you failed is redone after 1, 3 and 7 days. Most gains come from these redos.

If you can stretch weekends to 3 hours, do the Stretch column in the weekly plan. If the interview date can move 1–2 weeks later, take it; the extra time would go to more timed mixed practice.

## Daily routine (90 minutes)

Each session runs the same five steps, so you never spend time deciding what to do.

1. **Warm-up redo (10 min).** Re-solve one problem due for review from scratch, with no peeking.
2. **Pattern primer (10 min).** Read today's pattern in the cheat sheet below. Write its template once from memory.
3. **Problem 1 (25 min max).** Talk out loud as if an interviewer were listening. State brute force and its Big-O before coding.
4. **Problem 2 (25 min max).** Same pattern, harder variant. On weekends, add a third.
5. **Log (5 min).** Record each problem in the tracker: green (solved alone), yellow (needed a hint), red (needed the solution). Set its redo date.

When stuck at 25 minutes:

1. Read only the approach, not the code, and try again for 10 minutes.
2. Still stuck: read the full solution until you can explain *why* it works.
3. Close it and write it from memory. Mark it red.

On a 60-minute day, skip step 4. On a 2-hour day, add a second redo or a Stretch problem.

## Week-by-week plan

Topics build on each other: arrays and hash maps first, then linear structures, then trees and graphs, then design and mocks. Numbers are LeetCode problem IDs, and each problem links to its page. (Premium) marks problems that need LeetCode Premium; free versions of most are on neetcode.io.

### Week 1 (Oct 18–24): Arrays, Hash Tables, Strings, Sorting

| Day | Pattern | Core | Stretch |
| --- | --- | --- | --- |
| Sun Oct 18 | Python toolkit, Big-O, hash map basics | [1 Two Sum](https://leetcode.com/problems/two-sum/), [217 Contains Duplicate](https://leetcode.com/problems/contains-duplicate/), [242 Valid Anagram](https://leetcode.com/problems/valid-anagram/) | [49 Group Anagrams](https://leetcode.com/problems/group-anagrams/) |
| Mon Oct 19 | Hash map counting | [49 Group Anagrams](https://leetcode.com/problems/group-anagrams/), [347 Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | [128 Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) |
| Tue Oct 20 | Prefix sums | [238 Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/), [560 Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | [303 Range Sum Query](https://leetcode.com/problems/range-sum-query-immutable/) |
| Wed Oct 21 | Two pointers | [167 Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/), [15 3Sum](https://leetcode.com/problems/3sum/) | [11 Container With Most Water](https://leetcode.com/problems/container-with-most-water/) |
| Thu Oct 22 | Sliding window | [121 Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/), [3 Longest Substring Without Repeating](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [424 Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) |
| Fri Oct 23 | Sorting + heaps | [75 Sort Colors](https://leetcode.com/problems/sort-colors/), [215 Kth Largest Element](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Write merge sort from memory |
| Sat Oct 24 | Strings + review | [438 Find All Anagrams](https://leetcode.com/problems/find-all-anagrams-in-a-string/), [271 Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Premium), redo all reds | [76 Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (hard) |

### Week 2 (Oct 25–31): Lists, Stack/Queue, Intervals, Binary Search

| Day | Pattern | Core | Stretch |
| --- | --- | --- | --- |
| Sun Oct 25 | Linked list basics | [206 Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/), [21 Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/), [141 Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | [2 Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) |
| Mon Oct 26 | Fast/slow pointers, dummy node | [19 Remove Nth Node From End](https://leetcode.com/problems/remove-nth-node-from-end-of-list/), [143 Reorder List](https://leetcode.com/problems/reorder-list/) | [138 Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) |
| Tue Oct 27 | Stack | [20 Valid Parentheses](https://leetcode.com/problems/valid-parentheses/), [155 Min Stack](https://leetcode.com/problems/min-stack/) | [150 Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) |
| Wed Oct 28 | Monotonic stack, deque | [739 Daily Temperatures](https://leetcode.com/problems/daily-temperatures/), [394 Decode String](https://leetcode.com/problems/decode-string/) | [239 Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) (hard) |
| Thu Oct 29 | Intervals | [56 Merge Intervals](https://leetcode.com/problems/merge-intervals/), [57 Insert Interval](https://leetcode.com/problems/insert-interval/) | [435 Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) |
| Fri Oct 30 | Intervals + heap | [253 Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (Premium), [23 Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | [986 Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) |
| Sat Oct 31 | Binary search + review | [704 Binary Search](https://leetcode.com/problems/binary-search/), [33 Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/), redo all reds | [153 Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) |

### Week 3 (Nov 1–7): Trees, Tries, Graphs

| Day | Pattern | Core | Stretch |
| --- | --- | --- | --- |
| Sun Nov 1 | Tree DFS (recursion) | [104 Max Depth](https://leetcode.com/problems/maximum-depth-of-binary-tree/), [226 Invert Tree](https://leetcode.com/problems/invert-binary-tree/), [543 Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [110 Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) |
| Mon Nov 2 | Tree BFS, BST | [102 Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/), [98 Validate BST](https://leetcode.com/problems/validate-binary-search-tree/) | [199 Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/), [230 Kth Smallest in BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) |
| Tue Nov 3 | Tree problems that return info upward | [236 Lowest Common Ancestor](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/), [105 Construct Tree from Preorder/Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [124 Max Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) (hard) |
| Wed Nov 4 | Tries | [208 Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/), [211 Add and Search Words](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | [212 Word Search II](https://leetcode.com/problems/word-search-ii/) (hard) |
| Thu Nov 5 | Grid graphs (DFS/BFS) | [200 Number of Islands](https://leetcode.com/problems/number-of-islands/), [994 Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | [417 Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) |
| Fri Nov 6 | Adjacency lists, topological sort | [133 Clone Graph](https://leetcode.com/problems/clone-graph/), [207 Course Schedule](https://leetcode.com/problems/course-schedule/) | [210 Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) |
| Sat Nov 7 | Union-find + mock 1 | [323 Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) (Premium), **Mock 1** (2 unseen mediums, 45 min) | [261 Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) (Premium) |

### Week 4 (Nov 8–14): API Design, hard patterns, mocks

| Day | Pattern | Core | Stretch |
| --- | --- | --- | --- |
| Sun Nov 8 | Shortest paths | [127 Word Ladder](https://leetcode.com/problems/word-ladder/) (BFS), [743 Network Delay Time](https://leetcode.com/problems/network-delay-time/) (Dijkstra) | [787 Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) |
| Mon Nov 9 | API design: hash map + linked list | [146 LRU Cache](https://leetcode.com/problems/lru-cache/), [981 Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | [460 LFU Cache](https://leetcode.com/problems/lfu-cache/) (hard) |
| Tue Nov 10 | API design: counters and randomness | [380 Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/), [359 Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) (Premium), [362 Design Hit Counter](https://leetcode.com/problems/design-hit-counter/) (Premium) | [355 Design Twitter](https://leetcode.com/problems/design-twitter/) |
| Wed Nov 11 | Design with heaps and trees | [295 Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/), [297 Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [642 Design Search Autocomplete](https://leetcode.com/problems/design-search-autocomplete-system/) (Premium) |
| Thu Nov 12 | **Mock 2** | 45-min timed mock, then redo everything you missed | — |
| Fri Nov 13 | Red list | Redo every problem still red or yellow | — |
| Sat Nov 14 | **Mock 3**, then rest | 45-min mock in the morning; light review of the cheat sheet only | — |

For mocks, use a friend, Pramp or interviewing.io, or a random unseen medium from the topic list with a timer running and your voice recorded.

## Pattern cheat sheet

Read the problem, find the signal in the left column, and you usually have the approach.

| Signal in the problem | Pattern | Core idea | Typical time |
| --- | --- | --- | --- |
| "Have I seen this before?", pairs summing to a target, counting | Hash map / set | Trade memory for O(1) lookups | O(n) |
| Sum of a subarray, range queries | Prefix sums | sum(i..j) = pre\[j+1\] − pre\[i\]; store prefix counts in a map | O(n) |
| Sorted array, pairs/triplets, palindromes | Two pointers | Move left/right inward based on a comparison | O(n) |
| Longest/shortest contiguous substring or subarray with a condition | Sliding window | Expand right; shrink left while the window is invalid | O(n) |
| Top K, Kth largest, merge K sorted things, running median | Heap | heapq keeps the smallest on top; size-K heap for top K | O(n log k) |
| Sorted input, or "minimum value that works" | Binary search | Halve the search space; watch the loop bounds | O(log n) |
| Linked list middle, cycle, Nth from end | Fast/slow pointers | Fast moves 2, slow moves 1; dummy head avoids edge cases | O(n) |
| Matching brackets, nested structure, undo | Stack | Push opens, pop on close | O(n) |
| "Next greater/smaller element" | Monotonic stack | Keep the stack sorted; pop while the new item breaks the order | O(n) |
| Overlapping ranges, meetings, merging | Intervals | Sort by start; compare with the last merged end | O(n log n) |
| Tree depth, paths, subtree properties | Tree DFS | Recursive function returns info from children to parent | O(n) |
| Level by level, nearest, minimum steps | BFS | Queue (deque); process one level at a time | O(V + E) |
| Prefix lookups, autocomplete, word dictionaries | Trie | Node = dict of children + end-of-word flag | O(word length) |
| Islands, regions, connected parts | Graph DFS/BFS or union-find | Mark visited; count starts of new searches | O(V + E) |
| Prerequisites, ordering with dependencies | Topological sort | Kahn's algorithm: repeatedly take nodes with in-degree 0 | O(V + E) |
| Shortest path with weights | Dijkstra | Min-heap of (distance, node) | O(E log V) |
| Design a class with O(1) operations | API design | Pick one structure per operation; combine (hash map + linked list, hash map + array) | Per method |

### Templates to write from memory

Sliding window:

```python
def longest_window(s):
    seen = {}
    left = best = 0
    for right, ch in enumerate(s):
        seen[ch] = seen.get(ch, 0) + 1
        while seen[ch] > 1:          # window invalid -> shrink
            seen[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```

Binary search (first index where condition is true):

```python
def first_true(lo, hi, ok):
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

BFS on a grid:

```python
from collections import deque

def bfs(grid, sr, sc):
    rows, cols = len(grid), len(grid[0])
    q = deque([(sr, sc, 0)])
    seen = {(sr, sc)}
    while q:
        r, c, d = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and grid[nr][nc] != '#':
                seen.add((nr, nc))
                q.append((nr, nc, d + 1))
```

Topological sort (Kahn's):

```python
from collections import defaultdict, deque

def topo(n, edges):
    graph, indeg = defaultdict(list), [0] * n
    for a, b in edges:          # a must come before b
        graph[a].append(b)
        indeg[b] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nxt in graph[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return order if len(order) == n else []   # [] means a cycle
```

Union-find:

```python
parent = list(range(n))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]   # path compression
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    parent[ra] = rb
    return True
```

## Python toolkit

Know these cold by the end of day 1; fumbling syntax burns interview minutes.

| Tool | Use it for | Gotcha |
| --- | --- | --- |
| `collections.Counter(s)` | Character/word counts, anagrams | `c1 == c2` compares counts directly |
| `collections.defaultdict(list)` | Graphs, grouping | No KeyError on a missing key |
| `collections.deque` | BFS queues, sliding window max | `popleft()` is O(1); `list.pop(0)` is O(n) |
| `heapq.heappush / heappop` | Top K, Dijkstra, merge K lists | Min-heap only; push `-x` for a max-heap; ties compare the next tuple item |
| `bisect.bisect_left` | Binary search on a sorted list | Returns the insertion point, not "found" |
| `sorted(x, key=lambda i: i[0])` | Intervals, custom order | `list.sort()` sorts in place and returns None |
| `tuple(sorted(word))` | Hashable keys (group anagrams) | Lists can't be dict keys |
| `@functools.cache` | Memoized recursion | Arguments must be hashable |
| `float('inf')` | Min/max initial values | — |
| `enumerate`, `zip`, `reversed` | Clean loops | — |
| `sys.setrecursionlimit(10**6)` | Deep tree/graph DFS | Prefer an explicit stack for very deep input |
| `OrderedDict.move_to_end` | Quick LRU Cache | Interviewers often want the hand-built linked list too |

Strings are immutable: build with a list and `''.join(parts)`, never `+=` in a loop.

## In the interview: the 45-minute framework

Interviewers score communication and process, not only a passing solution. A candidate who explains clearly and nearly finishes often beats one who codes silently.

1. **Clarify (3–5 min).** Restate the problem. Ask about input size, empty input, duplicates, negatives, sorted or not. Work one example by hand.
2. **Brute force (2 min).** Say it and its Big-O out loud, even if it's slow. It proves you understand the problem.
3. **Optimize (5–8 min).** Name the pattern ("this looks like a sliding window"). Explain the approach and confirm before coding.
4. **Code (15–20 min).** Narrate as you go. Use clear names. Write small helper functions rather than one long block.
5. **Test (5 min).** Walk through your example line by line. Then try edge cases: empty, one element, all duplicates.
6. **Complexity (1 min).** State time and space, and one possible improvement.

For **API design** questions (LRU Cache, rate limiter):

- List the operations and their required complexity first.
- Write the class and method signatures before any logic.
- Choose one data structure per operation, then combine them.
- Expect follow-ups: thread safety (a lock around shared state), memory limits, scaling to many users.

When stuck: say what you're thinking, try a smaller example, or ask "would sorting help?" Hints are normal and cost little when you use them well.

## Tracker and readiness checklist

Log every attempt here. The redo dates drive your daily warm-up.

| Date | Problem | Pattern | Result (green/yellow/red) | Time (min) | Redo on |
| --- | --- | --- | --- | --- | --- |
| Oct 18 | 1 Two Sum | Hash map |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

You're ready when you can tick all of these:

- [ ] Write every template in the cheat sheet from memory in under 3 minutes each
- [ ] Name the pattern for an unseen medium within 5 minutes
- [ ] Solve an unseen medium in 30 minutes, talking the whole time
- [ ] Code LRU Cache from scratch (hash map + doubly linked list) in 25 minutes
- [ ] State time and space complexity for every solution without hesitation
- [ ] No problem in the tracker still marked red
- [ ] Pass at least 2 of the 3 mock interviews

If a mock goes badly, don't add new topics. Redo that topic's core problems and its pattern template instead.
