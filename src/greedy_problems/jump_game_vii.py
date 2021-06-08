#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1871. Jump Game VII
URL: https://leetcode.com/problems/jump-game-vii/description/
"""


class Solution:
    def can_reach(self, s: str, minJump: int, maxJump: int) -> bool:
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
    solution = Solution()
    assert solution.can_reach(s="011010", minJump=2, maxJump=3)
    assert not solution.can_reach(s="01101110", minJump=2, maxJump=3)
