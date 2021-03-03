#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1758. Minimum Changes To Make Alternating Binary String
URL: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/
"""
# O(N)/O(1)


class Solution:
    def min_operations(self, s: str) -> int:
        # check considering first number = 0
        last_char = "1"
        cnt_1 = 0
        for c in s:
            if c == last_char:
                cnt_1 += 1
            last_char = "1" if last_char == "0" else "0"
        # check considering first number = 1
        last_char = "0"
        cnt_2 = 0
        for c in s:
            if c == last_char:
                cnt_2 += 1
            last_char = "1" if last_char == "0" else "0"
        return min(cnt_1, cnt_2)


if __name__ == "__main__":
    solution = Solution()
    assert solution.min_operations(s="0100") == 1
    assert solution.min_operations(s="10") == 0
    assert solution.min_operations(s="1111") == 2
