#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1647. Minimum Deletions to Make Character Frequencies Unique
URL: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

Description:
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string.
For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example 1:
Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:
Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Example 3:
Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.

Complexity:
Time: O(N)
Space: O(1)
"""

import collections


class Solution:
    def min_deletions(self, s: str) -> int:
        letter_freq = collections.Counter(s)
        freqs = set()
        ret = 0
        for _, f in letter_freq.items():
            while f in freqs and f > 0:
                f -= 1
                ret += 1
            freqs.add(f)
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.min_deletions("aab") == 0
    assert solution.min_deletions("aaabbbcc") == 2
    assert solution.min_deletions("ceabaacb") == 2
