#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1739. Building Boxes
URL: https://leetcode.com/problems/building-boxes/

Description:
You have a cubic storeroom where the width, length, and height of the room are all equal to n units.
You are asked to place n boxes in this room where each box is a cube of unit side length.
There are however some rules to placing the boxes:

You can place the boxes anywhere on the floor.
If box x is placed on top of the box y, then each side of the four vertical sides of the box
y must either be adjacent to another box or to a wall.
Given an integer n, return the minimum possible number of boxes touching the floor.


Example 1:
Input: n = 3
Output: 3
Explanation: The figure above is for the placement of the three boxes.
These boxes are placed in the corner of the room, where the corner is on the left side.

Example 2:
Input: n = 4
Output: 3
Explanation: The figure above is for the placement of the four boxes.
These boxes are placed in the corner of the room, where the corner is on the left side.

Example 3:
Input: n = 10
Output: 6
Explanation: The figure above is for the placement of the ten boxes.
These boxes are placed in the corner of the room, where the corner is on the back side.

Constraints:
1 <= n <= 10^9
"""


class Solution:
    def minimum_boxes(self, n: int) -> int:
        stacked = 0
        next_batch = i = 1
        while stacked + next_batch < n:
            stacked += next_batch
            i += 1
            next_batch += i

        ret = next_batch - i
        i = 1
        remaining = n - stacked
        while remaining > 0:
            remaining -= i
            i += 1
            ret += 1

        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.minimum_boxes(3) == 3
    assert solution.minimum_boxes(4) == 3
    assert solution.minimum_boxes(10) == 6
