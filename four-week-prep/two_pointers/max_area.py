"""
The problem
- You get an array of non-negative heights, each one a vertical line at its index. 
- Pick two lines so that, together with the x-axis, they hold the most water. 
- Return that maximum area, which is the shorter line's height times the distance between them.

Pattern signals

- "Pick a pair from an array, maximize a score" with n up to 10^5 rules out checking every pair, so you need a way to throw candidates away safely.
- The score depends on both ends of a range (width) and the weaker end (height), which points to pointers starting at the two outer edges.
- How it differs from 3Sum: this morning you sorted so that moving a pointer had a predictable effect on the sum. Here you can't sort, because the positions are the width. The stretch is proving which pointer to move without that ordering.

Plan of attack
Questions to ask yourself before coding:

- Does order matter? (Yes, indices are the width, so no sorting.)
- Which line limits the area? (The shorter one, always.)
If I move a pointer inward, the width shrinks by 1. What would have to happen for the area to grow?

Brute force: try every pair i < j, compute min(h[i], h[j]) * (j - i), keep the max. That's O(n^2) and times out.

From brute force to optimal:

- Start with the widest container, l = 0 and r = n - 1. Every other pair is narrower.
- Say h[l] < h[r]. Any pair that keeps l and moves r inward is narrower and still capped at h[l], so its area can only be smaller. Every pair using l is now done, so drop l.
- That's the key move: always step the shorter side inward, since it's the only side whose move could find a taller limit.
- When heights are equal, moving either is safe, because neither can be part of a bigger container with the other still inside.
- Repeat until the pointers meet, tracking the best area seen.

Options explored

- Brute force over all pairs: O(n^2) time, O(1) space. Simple and a fine opener out loud, but it fails at scale.
- Two pointers from the edges: O(n) time, O(1) space, about 8 lines. Low code risk. The interview risk is the explanation, so be ready to say why moving the shorter side never skips the answer.
- Two pointers with a skip: after moving, keep advancing past lines no taller than the one you just left, since they can't help. Same O(n) bound and a bit faster in practice, but a little more code to get wrong. Mention it as a follow-up.

Pitfalls and edge cases

- Moving the taller pointer instead of the shorter one. It's the most common bug and gives wrong answers quietly.
- Using max instead of min for the height.
- Width is r - l, not r - l + 1.

Tesing:
- Test: two lines only, like [1, 1] gives 1.
- Test: all equal heights, like [5, 5, 5, 5] gives 15.
- Test: zeros mixed in, like [0, 2, 0] gives 0.
- Test: strictly increasing and strictly decreasing arrays.
- Test: the classic [1, 8, 6, 2, 5, 4, 8, 3, 7] gives 49.

Complexity

- Time O(n): each step moves exactly one pointer one place inward, and they start n - 1 apart, so the loop runs at most n - 1 times with O(1) work each.
- Space O(1): just two pointers and a running best, no extra structures, and no sort like this morning's O(n log n).
"""

def max_area(height:list[int]) -> int:
    left, right = 0, len(height) - 1
    max_so_far = 0

    while left < right:
        # compute the aresa with the current pair of lines
        width = right - left
        current_area = min(height[left], height[right]) * width

        # update the max are so far
        max_so_far = max(max_so_far, current_area)

        # move the shorter line inward, since it's the only one that could find a taller limit
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_so_far

def test_max_area(height: list[int], expected: int):
    print(f"\n====> testing max_area with height: {height} <====")
    result = max_area(height)
    print(f"result: {result}, expected: {expected}")
    assert result == expected, f"Test failed for input {height}. Expected {expected}, got {result}"


if __name__ == "__main__":
    print("====> testing max_area <====")
    test_max_area([1, 1], 1)
    test_max_area([5, 5, 5, 5], 15)
    test_max_area([0, 2, 0], 0)
    test_max_area([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)
    test_max_area([ 1, 2, 3, 4, 5], 6)