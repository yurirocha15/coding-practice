# @l2g 1869 python3
# [1869] Longer Contiguous Segments of Ones than Zeros
# Difficulty: Easy
# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros
#
# Given a binary string s,
# return true if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s in s.
# Return false otherwise.
#
# For example,in s = "110100010" the longest contiguous segment of 1s has length 2,
# and the longest contiguous segment of 0s has length 3.
#
# Note that if there are no 0s,
# then the longest contiguous segment of 0s is considered to have length 0.
# The same applies if there are no 1s.
#
# Example 1:
#
# Input: s = "1101"
# Output: true
# Explanation:
# The longest contiguous segment of 1s has length 2: "1101"
# The longest contiguous segment of 0s has length 1: "1101"
# The segment of 1s is longer, so return true.
#
# Example 2:
#
# Input: s = "111000"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 3: "111000"
# The longest contiguous segment of 0s has length 3: "111000"
# The segment of 1s is not longer, so return false.
#
# Example 3:
#
# Input: s = "110100010"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 2: "110100010"
# The longest contiguous segment of 0s has length 3: "110100010"
# The segment of 1s is not longer, so return false.
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s[i] is either '0' or '1'.
#
#


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ret = [0, 0]
        cnt = [0, 0]
        for c in s:
            cnt[1 - int(c)] = 0
            cnt[int(c)] += 1
            ret = [max(ret[x], cnt[x]) for x in range(2)]
        return ret[1] > ret[0]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1869.py")])
