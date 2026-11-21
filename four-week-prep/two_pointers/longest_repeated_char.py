"""
The problem
- You get a string s of uppercase letters and an integer k. You may change up to k characters to any other letter. Return the length of the longest substring that can be made of one repeated letter. "AABABBA" with k = 1 gives 4 (turn one B or A to make "AAAA" or "BBBB").

Pattern signals
- "Longest contiguous substring" plus a budget (k changes) points to a variable size sliding window.
- This morning's window was valid when it had no repeats, a simple yes or no check. Here validity is a count: a window is fine when the letters that aren't its most common letter number k or fewer. So you're tracking frequencies, not just presence.
- The stretch: the condition depends on the window's max frequency, and keeping that exact as the window shrinks is the tricky part.

Plan of attack
Questions to ask yourself first:
- What makes a window valid? window length minus count of its most frequent letter ≤ k.
- Does validity shrink nicely? Yes: shrinking a valid window keeps it valid, so the two pointer window works.
- Alphabet size? 26 uppercase letters, so counting is constant space.

Brute force: try every substring, count letters, check the rule. O(n²) with a running count, O(n³) if you recount.
- From brute force to optimal:
- Instead of restarting at every left index, grow right one step at a time and keep a count map.
- When the window breaks the rule, move left forward and decrement its count until it's valid again.
- Track max_freq as you add letters. The key insight: you never need to lower max_freq when shrinking. The answer only gets bigger when some letter reaches a new higher frequency, so a stale max_freq can only keep the window the same size, never report a wrong larger answer.

Options explored
- Recompute max over the 26 counts each step: O(26n), exact and easy to defend in an interview. Low risk.
- Stale max_freq trick: O(n), shortest code, but you must be able to explain why it's still correct. Medium risk if you can't justify it.
- Try each target letter separately (26 passes, each "longest window with ≤ k non-target letters"): O(26n), very intuitive, a nice fallback if you get stuck.

Pitfalls and edge cases
- Forgetting that the window size is right − left + 1.
- Using max_freq of the whole string instead of the window.
- k = 0 (longest run of one letter), k ≥ len(s) (answer is len(s)), single character string, all same letters.
- Lowercase or other characters if the interviewer changes the input; ask.

Complexity
- Time O(n): right moves n times, left moves at most n times overall, and each step is constant work.
- Space O(1): at most 26 keys in the count map

The core idea
- A window s[left..right] is valid if you can make it all one letter within budget. The cheapest way is to keep the most common letter and replace everything else, so:
replacements needed = window size - count of most common letter.
- If that number is at most k, the window is valid.

"""

from collections import defaultdict

# You get a string s of uppercase letters and an integer k. 
# You may change up to k characters to any other letter. 
# Return the length of the longest substring that can be made of one repeated letter.
def longest_repeated_char(s : str, k: int) -> int:
    char_count:dict[str, int] = defaultdict(int)

    left = 0
    max_freq = 0
    max_length = 0
    best_start = 0
    best_length = 0

    for right, char in enumerate(s):
        char_count[char] += 1
        max_freq = max(max_freq, char_count[char])

        # if the window size minus the count of the most frequent letter is greater than k, 
        # shrink the window from the left
        window_size = right - left + 1
        # Letters we'd need to replace = window size - most common letter.
        # If that's over budget, slide left forward by one.
        # (An if works here because the window only ever grows by 1.)
        if window_size - max_freq > k:
            char_at_left = s[left]
            char_count[char_at_left] -= 1
            left += 1
            # recalculate the window size after shrinking
            window_size = right - left + 1

        # update the max_length
        max_length = max(max_length, window_size)

        if window_size > best_length:
            best_start = left
            best_length = window_size
    
    print(f"Best substring: '{s[best_start:best_start + best_length]}' starting at index {best_start} with length {best_length}")
    if len(s) > 0:
            # Track where the best window starts, not just how long it is, and slice at the end.     
            substring = s[best_start:best_start + best_length]
            common_char = max(set(substring), key=substring.count)
            print(f"Most common character in the best substring: '{common_char * best_length}'")
        
    
    return max_length



def test_longest_repeated_char(s: str,  expected: int, k:int = 1):
    print(f"\nTesting longest_repeated_char with input '{s}'")
    result = longest_repeated_char(s, k)
    print(f"Result: {result}, Expected: {expected}")
    assert result == expected, f"Expected {expected}, but got {result} for input '{s}'"

if __name__ == "__main__":
    print("====> testing longest_repeated_char <====")
    test_longest_repeated_char("", 0)
    test_longest_repeated_char("a", 1)
    test_longest_repeated_char("aa", 2)
    test_longest_repeated_char("aab", 3)
    test_longest_repeated_char("abb", 3)
    test_longest_repeated_char("abbb",4)
    test_longest_repeated_char("aabbcc", 3)
    test_longest_repeated_char("abcde", 2)
    test_longest_repeated_char("aaabbbcccaaa", 4)

    test_longest_repeated_char("aabbcc", 4,2)
    test_longest_repeated_char("aaabbbcccaaa", 5,2)
    test_longest_repeated_char("aaabbbcccaaa", 6,3)

    test_longest_repeated_char("abbcccaaa", 4,1)