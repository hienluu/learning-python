"""
This function finds the length of the longest substring without repeating characters.

The problem
- You get a string s and return the length of the longest contiguous substring where no character shows up twice. "abcabcbb" gives 3 ("abc"), and "pwwkew" gives 3 ("wke", not "pwke", because that's a subsequence, not a substring).

Pattern signals
- "Longest contiguous substring" is the classic sliding window cue.
- The validity rule (no repeats) is monotonic: if a window is valid, every smaller window inside it is too, so you can grow the right edge and only ever move the left edge forward.
- You need fast "have I seen this char in the window?" checks, which points to a set or a char to index map.

Plan of attack
- Questions to ask first: what's the character set (ASCII, letters only, Unicode)? Can s be empty? Is it case sensitive? Do they want the length or the substring itself?

Brute force: check every start i, extend j until you hit a repeat, track the best. That's O(n²) with a set per start, or O(n³) if you recheck each substring from scratch.
- Key observation: when you hit a repeat at j, every start before the earlier copy of s[j] is also doomed. So don't restart from i+1; jump the left edge just past that earlier copy and keep j moving.
- That gives one pass: right pointer adds chars, left pointer only moves forward, and you record the window size at each step.

Options explored
- Set + shrink loop: on a repeat, pop from the left until the duplicate leaves. O(n) time, since each char enters and leaves once. Easiest to get right and to explain.
- Last seen index map: store each char's latest index and jump left straight to last[c] + 1. Still O(n), fewer steps, but has one sneaky bug (below). Great follow up answer.
- Fixed array of size 128 instead of a dict: same idea, slightly faster, but bakes in an ASCII assumption, so say so out loud.

Pitfalls and edge cases
- With the index map, only jump when the old index is inside the current window: left = max(left, last[c] + 1). Without the max, "abba" makes left go backwards and you get 3 instead of 2.
- Window length is right - left + 1, and the off by one bites often.

Test "", "a", "bbbbb", "abba", "pwwkew", "dvdf" and a string with spaces or symbols.

Complexity of the optimal approach
- Time O(n): right visits each index once, and left only moves forward, so total pointer movement is at most 2n. Each map lookup and update is O(1).
- Space O(min(n, k)), where k is the alphabet size: the map holds at most one entry per distinct char, and never more than n entries.


"""

def longest_substring(str : str) -> int:
    
    max_length = 0
    left = 0

    # use this dict to keep track of the count as the window is widen
    seen: dict[str,int] = {}

    # iterate through the string with the right pointer start at 0
    for right, char in enumerate(str):
        # have we seen the character before? If so, we need to shrink the window from the left until we remove the duplicate
        if char in seen:
            # move the left pointer to the right of the last seen index of the character
            left = max(left, seen[char] + 1)

        # update the last seen index of the character
        seen[char] = right

        # update the max length if the current window is larger
        max_length = max(max_length, right - left + 1)

    return max_length


def test_longest_substring(s: str, expected: int):
    print(f"\nTesting longest_substring with input '{s}'")
    result = longest_substring(s)
    print(f"Result: {result}, Expected: {expected}")
    assert result == expected, f"Expected {expected}, but got {result} for input '{s}'"


if __name__ == "__main__":
    print("====> testing longest_substring <====")
    test_longest_substring("", 0)
    test_longest_substring("a", 1)
    test_longest_substring("bbbbb", 1)
    test_longest_substring("abba", 2)
    test_longest_substring("pwwkew", 3)
    test_longest_substring("dvdf", 3)
    test_longest_substring("abcabcbb", 3)
    test_longest_substring(" ", 1)
    test_longest_substring("abcdefghijklmnopqrstuvwxyz", 26)