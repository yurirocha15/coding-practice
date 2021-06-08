#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1869. Longer Contiguous Segments of Ones than Zeros
URL: https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/description/
"""


class Solution:
    def check_zero_ones(self, s: str) -> bool:
        ret = [0, 0]
        cnt = [0, 0]
        for c in s:
            cnt[1 - int(c)] = 0
            cnt[int(c)] += 1
            ret = [max(ret[x], cnt[x]) for x in range(2)]
        return ret[1] > ret[0]


if __name__ == "__main__":
    solution = Solution()
    assert solution.check_zero_ones(s="1101")
    assert not solution.check_zero_ones(s="111000")
    assert not solution.check_zero_ones(s="110100010")
