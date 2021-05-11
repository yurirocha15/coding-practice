#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1839. Longest Substring Of All Vowels in Order
URL: https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/description/
"""
from typing import Dict, Set


class Solution:
    def longest_beautiful_substring(self, word: str) -> int:
        allowed: Dict[str, str] = {
            "a": "ae",
            "e": "ei",
            "i": "io",
            "o": "ou",
            "u": "u",
        }
        last_c = word[0]
        last_idx = 0
        letters: Set[str] = set(last_c)
        ret = 0
        for i in range(1, len(word)):
            if word[i] not in allowed[last_c]:
                if len(letters) == 5:
                    ret = max(ret, i - last_idx)
                last_idx = i
                letters.clear()
            last_c = word[i]
            letters.add(word[i])
        if len(letters) == 5:
            ret = max(ret, len(word) - last_idx)
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert (
        solution.longest_beautiful_substring(word="aeiaaioaaaaeiiiiouuuooaauuaeiu")
        == 13
    )
    assert solution.longest_beautiful_substring(word="aeeeiiiioooauuuaeiou") == 5
    assert solution.longest_beautiful_substring(word="a") == 0
