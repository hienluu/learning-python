"""
The problem
Given an integer array nums, return an array where each position holds the product of every other element. 
You can't use division, and it has to run in O(n).

Pattern signals:

"Everything except me" means the answer at i splits into what's to the left of i and what's to the right. 
That's the prefix/suffix pattern.

"No division" closes the obvious shortcut and forces you to build the products up rather than divide them out.
Compared with Group Anagrams, the trick here isn't a hash key but precomputing running aggregates so each answer is O(1).

Plan of attack
Questions to ask first:

Can there be zeros? (Yes, and that's exactly what breaks the division idea.)
Does the output array count toward extra space? (Usually no, which unlocks the O(1) follow-up.)
Can products overflow? (Guaranteed to fit in 32 bits here, and Python wouldn't care anyway.)

Brute force: for each i, multiply every j ≠ i. That's O(n²) and too slow for n = 10⁵.

From brute force to optimal:

The brute force recomputes the same partial products over and over.
answer[i] = (product of nums[0..i-1]) × (product of nums[i+1..n-1]).
Build a prefix array left to right and a suffix array right to left, then multiply them pointwise.
Follow-up: write the prefix products straight into the output, then sweep from the right with one running suffix variable and multiply it in. No extra arrays.

Options explored

Division (total product ÷ nums[i]): O(n), but banned, and needs special handling for one zero versus two or more. Worth mentioning to show you saw it.
Prefix and suffix arrays: O(n) time, O(n) extra space, the clearest to explain.
Output array plus running suffix: O(n) time, O(1) extra space. 
Best answer, slightly easier to get an off-by-one in.

Pitfalls and edge cases

Off-by-one: the prefix for index 0 and the suffix for the last index are both 1, not nums[0].
Test [1,2,3,4] → [24,12,8,6], one zero [-1,1,0,-3,3] → [0,0,9,0,0], two zeros → all zeros, and length 2.
Update the running suffix after multiplying it in, not before.

Complexity
Two linear passes give O(n) time. The output array is required, so extra space is O(1): 
just the one running variable.
"""

def except_self_bf(nums: list[int]) -> list[int]:
    print(f"\n bf -Input: {nums}")
    # brute force approach: using two nested loops, skip i = j
    n = len(nums)
    answer = [1] * n

    for i in range(n):
        for j in range(n):
            if i != j:
                answer[i] *= nums[j]

    return answer

def except_self(nums: list[int]) -> list[int]:
    print(f"\n optimal -Input: {nums}")
    # store the size of 
    n = len(nums)

    # seed the answer with all 1s because we are doing multiplications
    answer = [1] * n

    # [1,2,3,4] as an example, prefix is [1,1,2,6]
    # build the prefix
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    print(f"Prefix products: {answer}")
    
    print# build the suffix - going from right to left
    suffix = 1
    # range(start, stop, step) where start = n-1, stop = -1 (exclusive), step = -1
    for i in range(n-1, -1, -1):
        answer[i] *= suffix # for the right most, the answer is just the prefix
        suffix *= nums[i] # build the suffix product as we move left

    return answer


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(f"from brute force: {except_self_bf(nums)}")
    print(f"from optimal: {except_self(nums)}")

    
    nums = [4,3,2, 1]
    print(f"from brute force: {except_self_bf(nums)}")
    print(f"from optimal: {except_self(nums)}")