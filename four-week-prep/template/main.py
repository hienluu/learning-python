


"""
 longest window substring without repeating characters
"""
def longest_window_substring(s: str) -> int:
    seen = {}
    left = longest = 0

    # maintain a sliding window of characters in the string
    # right is the index and right pointer of the sliding window
    # char is the character at the right pointer of the sliding window
    for right, char in enumerate(s): 
        seen[char] = seen.get(char, 0) + 1
        # if the character has been seen more than once
        # that means we have a duplicate character in the current window
        # the window is not longest anymore, so we need to shrink the window from the left
        while seen[char] > 1:
            # invalidating the window by removing the leftmost character from the seen dictionary
            # start shrinking the window from the left
            left_char = s[left]
            # remove the bookkeeping of the leftmost character from the seen dictionary
            seen[left_char] -= 1
            # make sure to advancing the left pointer to shrink the window
            left += 1

        longest = max (longest, right - left + 1)

    return longest

def me(s: str) -> int:
    seen = {}
    left = longest = 0

    for right, char in enumerate(s):
        seen[char] = seen.get(char, 0) + 1
        while seen[char] > 1:
            left_char = s[left]
            seen[left_char] -= 1
            left += 1

        longest = max(longest, right - left + 1)

    return longest


def test_longest_window_substring(str:str, expected:int):
    print(f"Testing longest_window_substring('{str}')"  )
    assert me("abcabcbb") == 3
    assert longest_window_substring("bbbbb") == 1
    assert longest_window_substring("pwwkew") == 3
    assert longest_window_substring("") == 0
    assert longest_window_substring(" ") == 1
    assert longest_window_substring("au") == 2
    assert longest_window_substring("dvdf") == 3

if __name__ == "__main__":
    test_longest_window_substring("abcabcbb",3)  # Output: 3
    test_longest_window_substring("bbbbb",1)     # Output: 1
    test_longest_window_substring("pwwkew",3)    # Output: 3
    test_longest_window_substring("",0)           # Output: 0
    test_longest_window_substring(" ",1)          # Output: 1
    test_longest_window_substring("au",2)         # Output: 2
    test_longest_window_substring("dvdf",3)       # Output: 3