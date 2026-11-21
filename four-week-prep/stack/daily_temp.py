"""
The problem: you get a list of daily temperatures. For each day, return how many days you'd wait until a strictly warmer one, or 0 if none comes.

Pattern signals
- "For each element, find the next element that is bigger" is the classic monotonic stack signal.
- You need the answer for every index, and a naive scan forward for each one looks quadratic.
- This morning's problem was held back as a repeat, so this one stands alone. Compared with yesterday's sliding window, the window there moved in order; here an element waits on a stack until a later element "resolves" it.

Plan of attack
- Ask yourself: what does "warmer" mean for ties? (Strictly greater, so equal temperatures don't count.) What should a day with no answer get? (0.)

Brute force: for each day i, scan j = i+1 onward until temps[j] > temps[i]. That's O(n²), too slow for n up to 10⁵.
- Key insight: when you reach a warm day, it answers every earlier colder day that's still waiting, all at once.
- So keep the unanswered days on a stack. Because any colder day below a warmer one would already have been answered, the waiting temperatures are always decreasing from bottom to top.
- On each new day, pop while the top is colder, record the gap, then push today.

Options explored
- Brute force scan: O(n²) time, O(1) space. Easy to write, but times out. Fine to mention, not to submit.
- Monotonic stack, forward pass: O(n) time, O(n) space. Short, standard, low interview risk. This is the one to master.
- Backward pass with jumps: go right to left and use answers you already computed to hop ahead (j += answer[j]). O(n) amortized time, O(1) extra space. Clever, but harder to explain and easier to get wrong under pressure.

Pitfalls and edge cases
- Using <= instead of < in the pop condition, which treats equal days as warmer.
- Pushing temperatures instead of indices; you need indices to compute the gap.
- Test: a single day, all equal temps, strictly decreasing (stack never pops, all zeros), strictly increasing (every day answered by the next), and [73,74,75,71,69,72,76,73].
Days left on the stack at the end keep their default 0, so no cleanup is needed.

Complexity
- Time O(n): each index is pushed once and popped at most once, so the inner while loop does at most n pops across the whole run, not per day.
- Space O(n): the answer array, plus a stack that can hold every index when temperatures only fall.

"""

def daily_temp(temps:list[int]) -> list[int]:
    n:int = len(temps)
    solution:list[int] = [0] * n
    # we can access the temp using index using temps list,
    # so we can store the index of the temp in stack as we iterate through the temps list
    stack:list[int] = []

    for idx, temp in enumerate(temps):

        # if the temp of prev days are less than the current temp, 
        # we pop the index of the prev day from stack and calculate the difference between the current index 
        # the popped index to get the number of days until a warmer temp
        #  s[-1] gets the last element of the list, similar to peeking the top of the stack w/o popping it      
        while stack and temps[stack[-1]] < temp:
            prev_idx = stack.pop()
            solution[prev_idx] = idx - prev_idx

        stack.append(idx)

    return solution

def test_daily_temp(temps:list[int], expected:list[int]) -> None:
    print(f"\nTesting daily_temp({temps})")
    result = daily_temp(temps)
    print(f"\result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == "__main__":
    print(f"\n{'*' * 6} Daily Temperatures {'*' * 6}")

    test_daily_temp([], [])
    test_daily_temp([73], [0])
    test_daily_temp([73, 73, 73], [0, 0, 0])
    test_daily_temp([73, 72, 71, 0 ], [0, 0, 0, 0])
    test_daily_temp([73, 74, 75, 76], [1,1,1,0])
    test_daily_temp([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0])