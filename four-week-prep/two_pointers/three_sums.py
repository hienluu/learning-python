
"""
The problem
You're given an integer array. Return every unique triplet of values that adds up to zero. The triplets themselves can't repeat, though values inside a triplet can come from equal numbers at different positions.

Pattern signals
- "Find a group of elements with a target sum" plus "return all of them, no duplicates" is a strong hint to sort first.
- Once sorted, a pair sum is monotonic: moving the left pointer right raises the sum and moving the right pointer left lowers it. That's the classic two pointer setup.
The output asks for values, not indices, so sorting costs you nothing.

Plan of attack

Questions to ask before coding:
- Do I need indices or values? (Values, so sorting is fine.)
- How do I avoid duplicate triplets without a set of tuples?
-  Can I reduce this to a problem I already know? (Yes: fix one number, then solve Two Sum II on the rest.)

Brute force: three nested loops, check every triplet, dedupe with a set of sorted tuples. O(n³), too slow for n up to 3000.
From brute force to optimal:
- Fix the first element a = nums[i]. Now you need two numbers summing to -a.
- Inner loop as a hash set Two Sum gets you O(n²), but dedup is awkward.
- Sort the array. Now the inner search is two pointers on a sorted range: if the sum is too small move left up, too big move right down, equal means record it.
-  Sorting also makes dedup simple: skip i if it equals the previous value, and after a match skip over equal values on both pointers.
- Small bonus: once nums[i] > 0, every later sum is positive, so break.

Options explored
_ Sort plus two pointers: O(n²) time, O(1) extra beyond output (sort aside). Clean dedup. The interview favourite and lowest risk.
Fix one, hash set for the rest: O(n²) time, O(n) space. Works, but dedup needs a set of tuples or careful skipping, which is easy to get subtly wrong.
_ Brute force with a set: O(n³). Only worth mentioning as your starting point.

Pitfalls and edge cases
- Forgetting to skip duplicates for i, which produces repeated triplets like [-1, 0, 1] twice.
- Skipping duplicates for the pointers before recording the match, or forgetting to move both pointers after a match (infinite loop).
- Test: [0, 0, 0] → [[0, 0, 0]]; [0, 0, 0, 0] → still one triplet; [0, 1, 1] → []; fewer than three elements → []; [-2, 0, 1, 1, 2] → [[-2, 0, 2], [-2, 1, 1]].

Complexity
- Sorting is O(n log n).
- The outer loop runs n times, and each inner two pointer pass is O(n) because the pointers only move toward each other. That gives O(n²), which dominates the sort.
Space is O(1) extra besides the output, or O(n) if you count Python's sort (Timsort) buffer.

"""
def three_sums(nums: list[int]) -> list[list[int]]:
    nums_len = len(nums)
    

    # sort the array first, which makes deduplication easier and allows two pointers
    nums.sort()

    result:list[list[int]] = []

    for i in range(nums_len - 2):
        if nums[i] > 0:
            # since the array is sorted, no need to continue if the first number is > 0
            break  

        # this works because the array is sorted, so duplicates are adjacent by comparing current and previous numbers
        if i > 0 and nums[i] == nums[i - 1]:   # skip duplicate first numbers
          continue

        left, right = i + 1, nums_len - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0: # sum is too small, move left pointer to the right
                left += 1
            elif total > 0: # sum is too large, move right pointer to the left
                right -= 1
            else:
                # found a triplet
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # skip duplicates for left pointer
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # skip duplicates for right pointer
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return result
            
              



def test_three_sums(nums: list[int], expected: list[list[int]]):
    print(f"\n====> testing three_sums with nums: {nums} <====")
    
    result = three_sums(nums)
    print(f"result: {result}")

    assert result == expected, f"Expected {expected}, but got {result}"
    print(f"Test passed")


if __name__ == "__main__":
    print("====> testing three_sums <====")

    
    test_three_sums([0, 0, 0], [[0, 0, 0]])
    test_three_sums([0, 0, 0, 0], [[0, 0, 0]])
    test_three_sums([0, 1,1], [])
    test_three_sums([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]])
    test_three_sums([-2, 0, 0, 2, 2], [[-2,0,2]])

    