#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1823. Find the Winner of the Circular Game
URL: https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/
"""
from collections import deque


# Time O(n*k) / Space O(n)
class Solution:
    def find_the_winner(self, n: int, k: int) -> int:
        friends = deque(range(1, n + 1))
        while len(friends) > 1:  # O(n)
            friends.rotate(1 - k)  # O(k)
            friends.popleft()
        return friends[0]


if __name__ == "__main__":
    solution = Solution()
    assert solution.find_the_winner(n=5, k=2) == 3
    assert solution.find_the_winner(n=6, k=5) == 1
