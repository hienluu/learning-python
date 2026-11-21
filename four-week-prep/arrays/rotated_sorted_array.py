"""
The problem: a sorted array of distinct integers was rotated at some unknown pivot, like [4,5,6,7,0,1,2]. Given a target, return its index or -1, in O(log n) time.

Pattern signals
- "Sorted" plus "O(log n)" almost always means binary search.
- The twist is that the array is only sorted in pieces. This morning's slot repeated a stack problem, so this is your first binary search of the day. It stretches the plain template: each step you first decide which half is sorted, then whether the target lives there.

Plan of attack

Questions to ask yourself first:
- Are values distinct? (Yes here. Duplicates are #81 and break the guarantee.)
- Could the array be unrotated, or have one element?
- What invariant do my lo and hi keep?

Brute force: scan for the target, O(n). Correct, but misses the log n requirement.
- From brute force to optimal:
- Split at mid. At least one half, [lo..mid] or [mid..hi], must be fully sorted, because the rotation point can only sit in one of them.
- Spot the sorted half: if nums[lo] <= nums[mid], the left is sorted; otherwise the right is.
- In a sorted half you can check membership by range alone: is nums[lo] <= target < nums[mid]?
- If yes, search there. If no, the target can only be in the other half. Either way you discard half.

Options explored
- One-pass modified binary search: O(log n), O(1) space, one loop. 
- The interview is my favorite, but the comparisons are easy to get off by one.
- Find the pivot, then binary search one side: two clean standard searches. Also O(log n), and easier to reason about, at the cost of more code.
- Linear scan: trivial, O(n). Mention it only as the baseline.

Pitfalls and edge cases
- Use <= in nums[lo] <= nums[mid]. When lo == mid, a strict < misjudges the left half.
- Keep the range checks half-open against mid (target < nums[mid]), since you already checked mid itself.

Test: one element (hit and miss), no rotation, rotation by one ([2,1]), target at the pivot, target at either end, target absent.

Complexity
- Time O(log n): each loop does constant work and throws away half the range, so at most about log2(n) iterations.
- Space O(1): only lo, hi and mid, no recursion.

"""

def search_rotated_sorted_array(nums:list[int], target:int) -> int:
    lo, hi = 0, len(nums) - 1

    # since hi is inclusive, we need to check lo <= hi, not lo < hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid

        # left half is sorted
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]: # target is in the middle of the sorted left half
                hi = mid - 1
            else: # target is in the right half
                lo = mid + 1
        else: # right half is sorted
            if nums[mid] < target <= nums[hi]: # target is in the middle of the sorted right half
                lo = mid + 1
            else: # target is in the left half
                hi = mid - 1

    return -1

"""
How it works: the minimum is where the values suddenly drop, the rotation point. 
Comparing nums[mid] with nums[hi] tells you which side of mid

  the drop is on:
  - nums[mid] > nums[hi]: the values go down somewhere between mid and hi, so the minimum is to the right of mid.
  - nums[mid] <= nums[hi]: mid..hi is in sorted order, so nothing to the right of mid is smaller. mid itself could be the minimum,
    so you keep it
    with hi = mid rather than mid - 1.
"""
def min_rotated_sorted_array(nums:list[int]) -> int:
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]: # min is in the right half
            lo = mid + 1
        else: # min is in the left half
            hi = mid

    return nums[lo]

"""
find maximum in rotated sorted array: the maximum is where the values suddenly drop, the rotation point.
"""
"""Return the maximum value in a rotated sorted array of distinct values."""
def find_max(nums: list[int]) -> int:
    if not nums:
        return -1

    # Step 1: binary search for the index of the minimum (the rotation point)
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1   # the drop is to the right of mid
        else:
            hi = mid       # mid..hi is sorted, so the min is at mid or to its left
    min_index = lo

    # Step 2: the maximum is just before the minimum, wrapping around
    # Python's % returns the remainder r that makes this true
    max_index = (min_index - 1) % len(nums)
    return nums[max_index]
      


def test_search_rotated_sorted_array(nums:list[int], target:int, expected:int) -> None:
    print(f"\nTesting search_rotated_sorted_array({nums}, {target})")
    result = search_rotated_sorted_array(nums, target)
    print(f"Result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"


def test_min_rotated_sorted_array(nums:list[int], expected:int) -> None:
    print(f"\nTesting min_rotated_sorted_array({nums})")
    result = min_rotated_sorted_array(nums)
    print(f"Result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

def test_find_max(nums:list[int], expected:int) -> None:
    print(f"\nTesting find_max({nums})")
    result = find_max(nums)
    print(f"Result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == "__main__":
    print(f"\n {'*' * 6} Search in Rotated Sorted Array {'*' * 6}")

    test_search_rotated_sorted_array([], 1, -1)
    test_search_rotated_sorted_array([1], 1, 0)
    test_search_rotated_sorted_array([1], 2, -1)

    # no rotation
    test_search_rotated_sorted_array([1,3,7,20,25, 50], 20, 3)
    test_search_rotated_sorted_array([1,3,7,20,25, 50], 99, -1)
    test_search_rotated_sorted_array([1,3,7,20,25, 50], 1, 0)
    test_search_rotated_sorted_array([1,3,7,20,25, 50], 50, 5)

     # rotation by 1
    test_search_rotated_sorted_array([2,1], 1, 1)
    test_search_rotated_sorted_array([2,1], 2, 0)

    
    # rotation by 2
    test_search_rotated_sorted_array([4,5,6,7,0,1,2], 4, 0)
    test_search_rotated_sorted_array([4,5,6,7,0,1,2], 2, 6)
    test_search_rotated_sorted_array([4,5,6,7,0,1,2], 0, 4)
    test_search_rotated_sorted_array([4,5,6,7,0,1,2], 7, 3)


    test_search_rotated_sorted_array([3,1,2], 1, 1)
    test_search_rotated_sorted_array([2,3,1], 1, 2)
    test_search_rotated_sorted_array([2,3,1], 2, 0)

    # test min_rotated_sorted_array
    print(f"{'[' * 6} test min {']' * 6}")
    test_min_rotated_sorted_array([4,5,6,7,0,1,2], 0)
    test_min_rotated_sorted_array([3,4,5,1,2], 1)
    test_min_rotated_sorted_array([2,3,4,5,1], 1)


    # test find_max
    print(f"{'(' * 6} test max {')' * 6}")
    test_find_max([4,5,6,7,0,1,2],7)
    test_find_max([3,4,5,1,2], 5 )
    
