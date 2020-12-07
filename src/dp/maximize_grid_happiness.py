#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1659. Maximize Grid Happiness
URL: https://leetcode.com/problems/maximize-grid-happiness/

Description:
You are given four integers, m, n, introvertsCount, and extrovertsCount. You have an m x n grid, and there are two types of people: introverts and extroverts.
There are introvertsCount introverts and extrovertsCount extroverts.

You should decide how many people you want to live in the grid and assign each of them one grid cell.
Note that you do not have to have all the people living in the grid.

The happiness of each person is calculated as follows:

Introverts start with 120 happiness and lose 30 happiness for each neighbor (introvert or extrovert).
Extroverts start with 40 happiness and gain 20 happiness for each neighbor (introvert or extrovert).
Neighbors live in the directly adjacent cells north, east, south, and west of a person's cell.

The grid happiness is the sum of each person's happiness. Return the maximum possible grid happiness.

Example 1:
Input: m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
Output: 240
Explanation: Assume the grid is 1-indexed with coordinates (row, column).
We can put the introvert in cell (1,1) and put the extroverts in cells (1,3) and (2,3).
- Introvert at (1,1) happiness: 120 (starting happiness) - (0 * 30) (0 neighbors) = 120
- Extrovert at (1,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
- Extrovert at (2,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
The grid happiness is 120 + 60 + 60 = 240.
The above figure shows the grid in this example with each person's happiness. The introvert stays in the light green cell while the extroverts live on the light purple cells.

Example 2:
Input: m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
Output: 260
Explanation: Place the two introverts in (1,1) and (3,1) and the extrovert at (2,1).
- Introvert at (1,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
- Extrovert at (2,1) happiness: 40 (starting happiness) + (2 * 20) (2 neighbors) = 80
- Introvert at (3,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
The grid happiness is 90 + 80 + 90 = 260.

Example 3:
Input: m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
Output: 240

Constraints:

1 <= m, n <= 5
0 <= introvertsCount, extrovertsCount <= min(m * n, 6)

Complexity:
Space:
Time:
"""
from typing import Callable, Dict, Tuple


# memoization decorator
# arguments should be hashable -> no lists (use tuples instead)
def memoization(func: Callable) -> Callable:
    memo = dict()

    def wrapper(*args: Tuple) -> Dict[Tuple, int]:
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]

    return wrapper


class Solution:
    def get_max_grid_happiness(
        self, m: int, n: int, introverts_count: int, extroverts_count: int
    ) -> int:
        self.up_row = [0] * n
        self.m = m
        self.n = n

        @memoization
        def dp(int_c: int, ext_c: int, i: int, j: int, row_tup: Tuple) -> int:
            # end condition -> when we get to the end of the grid or there are no more people to add
            if (i == (self.m)) or (not int_c and not ext_c):
                return 0

            # initialize the happiness for each case
            empty_ret = i_delta_happy = e_delta_happy = 0
            # calculate the next coordinates in the grid
            next_i = i if j + 1 < n else i + 1
            next_j = j + 1 if j + 1 < n else 0

            # introvert case
            if int_c > 0:
                # starting happyness
                i_delta_happy = 120

                # if there is a cell before the current position
                if j:
                    # if it is an introvert
                    if self.up_row[j - 1] == -1:
                        i_delta_happy -= 60
                    # if it is an extrovert
                    elif self.up_row[j - 1] == 1:
                        i_delta_happy -= 10
                # if there is an introvert above the current position
                if self.up_row[j] == -1:
                    i_delta_happy -= 60
                # if there is an extrovert above the current position
                elif self.up_row[j] == 1:
                    i_delta_happy -= 10
                # set the current cell as introvert
                self.up_row[j] = -1
                # perform DFS starting from the next position
                i_delta_happy += dp(
                    int_c - 1, ext_c, next_i, next_j, tuple(self.up_row)
                )
                # restore the original value of the current cell
                self.up_row[j] = row_tup[j]
            # extrovert case
            if ext_c > 0:
                # starting happyness
                e_delta_happy = 40
                # if there is a cell before the current position
                if j:
                    # if it is an introvert
                    if self.up_row[j - 1] == -1:
                        e_delta_happy -= 10
                    # if it is an extrovert
                    elif self.up_row[j - 1] == 1:
                        e_delta_happy += 40
                # if there is an introvert above the current position
                if self.up_row[j] == -1:
                    e_delta_happy -= 10
                # if there is an extrovert above the current position
                elif self.up_row[j] == 1:
                    e_delta_happy += 40
                # set the current cell as an extrovert
                self.up_row[j] = 1
                # perform DFS starting from the next position
                e_delta_happy += dp(
                    int_c, ext_c - 1, next_i, next_j, tuple(self.up_row)
                )
                # restore the original value of the current cell
                self.up_row[j] = row_tup[j]
            # empty cell
            # set the current cell as empty
            self.up_row[j] = 0
            # perform DFS starting from the next position
            empty_ret = dp(int_c, ext_c, next_i, next_j, tuple(self.up_row))
            # restore the original value of the current cell
            self.up_row[j] = row_tup[j]

            # return the highest happiness
            return max(i_delta_happy, e_delta_happy, empty_ret)

        # start dp
        return dp(introverts_count, extroverts_count, 0, 0, tuple(self.up_row))


if __name__ == "__main__":
    solution = Solution()
    assert solution.get_max_grid_happiness(2, 3, 1, 2) == 240
    assert solution.get_max_grid_happiness(3, 1, 2, 1) == 260
    assert solution.get_max_grid_happiness(2, 2, 4, 0) == 240
