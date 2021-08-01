# @l2g 1871 python3
# [1871] Jump Game VII
# Difficulty: Medium
# https://leetcode.com/problems/jump-game-vii
#
# You are given a 0-indexed binary string s and two integers minJump and maxJump.In the beginning,
# you are standing at index 0,which is equal to '0'.
# You can move from index i to index j if the following conditions are fulfilled:
#
# i + minJump <= j <= min(i + maxJump, s.length - 1), and
# s[j] == '0'.
#
# Return true if you can reach index s.length - 1 in s, or false otherwise.
#
# Example 1:
#
# Input: s = "011010", minJump = 2, maxJump = 3
# Output: true
# Explanation:
# In the first step, move from index 0 to index 3.
# In the second step, move from index 3 to index 5.
#
# Example 2:
#
# Input: s = "01101110", minJump = 2, maxJump = 3
# Output: false
#
#
# Constraints:
#
# 2 <= s.length <= 10^5
# s[i] is either '0' or '1'.
# s[0] == '0'
# 1 <= minJump <= maxJump < s.length
#
#


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        available = [c == "0" for c in s]
        left = 1 - maxJump
        right = 1 - minJump
        cnt = 1 if left == 0 or right == 0 else 0
        for i in range(1, len(s)):
            if left < i - maxJump:
                if left >= 0 and available[left]:
                    cnt -= 1
                left += 1
            if right < i - minJump:
                right += 1
                if right >= 0 and available[right]:
                    cnt += 1
            if cnt <= 0:
                available[i] = False
        return available[-1]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1871.py")])
