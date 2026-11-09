"""
You get a list of strings and need to group together the ones that are anagrams of each other 
(same letters, same counts, any order). Return the groups in any order.

Pattern signals:
"Group together" items that are equal under some rule. That means you want a canonical key per item and a hash map from key to group.
Order of letters doesn't matter, only which letters and how many. That tells you what the key has to capture.

Plan of attack
Questions to ask first:

Only lowercase a to z? (Yes here, and it unlocks the counting key.)
Can strings be empty? Duplicates? (Both allowed, and both must still land in a group.)
Does output order matter? (No.)

Brute force: for each string, compare it to a representative of every existing group 
by sorting both or counting letters. That's O(n² · k) and it's the version that falls over on n = 10⁴.

From brute force to optimal:

The slow part is comparing each string against every group.
If equal anagrams always produce the identical "signature", you never compare. You just look the signature up.
A signature can be the sorted string, or a tuple of 26 letter counts.
Use a dict from signature to list, append each word, return the values. One pass.

Options explored

Sorted string as key: O(n · k log k) time, very short code, the easiest to get right under pressure. Great default.
26-count tuple as key: O(n · k) time, slightly more code. A nice follow-up to offer when they ask "can you beat k log k?"

Prime-product hashing: cute, but overflow and collision talk adds interview risk for no real gain. Mention it at most.

Pitfalls and edge cases

Lists aren't hashable. Convert the count list to a tuple, and turn sorted() output back into a string or tuple.
Empty string "" is a valid word and its own group (or groups with other "").
A single word in the input should give [[word]].
Duplicates like ["a", "a"] belong in the same group.
Building the key with str(counts) works but is slower and easy to get wrong. Prefer a tuple.

Complexity (count-key version)

Time O(n · k): n words, and for each you scan its k letters once to fill the counts. Building the 26-length tuple is O(26), which is constant. Dict lookups are O(1) on average, though hashing the tuple is that same constant 26.
Space O(n · k): every character ends up stored once in the output groups, plus at most n keys of 26 ints each.
With the sorted key, time becomes O(n · k log k) because of the sort per word.
"""

from collections import defaultdict
from typing import List

def group_anagrams(words : list[str]) -> list[list[str]]:
    # map each letter count signature to a list words
    # automatically provides a default value for a key that doesn't exist yet, 
    # preventing KeyError exceptions when retrieving or modifying missing keys
    groups = defaultdict(list)

    a_ord = ord('a')
    for word in words:
        # list is not hashable
        counts: list[int] = [0] * 26
        for char in word:
            counts[ord(char) - a_ord] += 1

        # that is the reason to convert list to tuple, which is immmutable and hashable
        signature = tuple(counts)
        print(f"Word: {word}, Signature: {signature}")
        groups[signature].append(word)

    return list(groups.values())


if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(words))    


            
