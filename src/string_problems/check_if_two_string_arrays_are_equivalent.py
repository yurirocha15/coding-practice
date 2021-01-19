#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1662. Check If Two String Arrays are Equivalent
URL: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

Description:
Given two string arrays word1 and word2,
return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

Constraints:

1 <= word1.length, word2.length <= 10^3
1 <= word1[i].length, word2[i].length <= 10^3
1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3
word1[i] and word2[i] consist of lowercase letters.

Complexity:
Time: O(max(W1, W2)) | W1 = sum(len(w1 in word1)), W2 = sum(len(w2 in word2))
Space: O(1)
"""
from typing import List


class Solution:
    def array_strings_are_equal(self, word1: List[str], word2: List[str]) -> bool:
        i = j = k = m = 0
        while i < len(word1) or j < len(word2):
            if i == len(word1) or j == len(word2) or word1[i][k] != word2[j][m]:
                return False
            k += 1
            m += 1
            if k == len(word1[i]):
                i += 1
                k = 0
            if m == len(word2[j]):
                j += 1
                m = 0
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.array_strings_are_equal(["ab", "c"], ["a", "bc"])
    assert not solution.array_strings_are_equal(["a", "cb"], ["ab", "c"])
    assert solution.array_strings_are_equal(["abc", "d", "defg"], ["abcddefg"])
