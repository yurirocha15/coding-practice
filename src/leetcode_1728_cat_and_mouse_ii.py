# @l2g 1728 python3
# [1728] Cat and Mouse II
# Difficulty: Hard
# https://leetcode.com/problems/cat-and-mouse-ii
#
# A game is played by a cat and a mouse named Cat and Mouse.
# The environment is represented by a grid of size rows x cols,where each element is a wall,floor,
# player (Cat,Mouse),or food.
#
# Players are represented by the characters 'C'(Cat),'M'(Mouse).
# Floors are represented by the character '.' and can be walked on.
# Walls are represented by the character '#' and cannot be walked on.
# Food is represented by the character 'F' and can be walked on.
# There is only one of each character 'C', 'M', and 'F' in grid.
#
# Mouse and Cat play according to the following rules:
#
# Mouse moves first, then they take turns to move.
# During each turn,Cat and Mouse can jump in one of the four directions (left,right,up,down).
# They cannot jump over the wall nor outside of the grid.
# catJump,mouseJump are the maximum lengths Cat and Mouse can jump at a time,respectively.
# Cat and Mouse can jump less than the maximum length.
# Staying in the same position is allowed.
# Mouse can jump over Cat.
#
# The game can end in 4 ways:
#
# If Cat occupies the same position as Mouse, Cat wins.
# If Cat reaches the food first, Cat wins.
# If Mouse reaches the food first, Mouse wins.
# If Mouse cannot get to the food within 1000 turns, Cat wins.
#
# Given a rows x cols matrix grid and two integers catJump and mouseJump,
# return true if Mouse can win the game if both Cat and Mouse play optimally,otherwise return false.
#
# Example 1:
#
#
# Input: grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
# Output: true
# Explanation: Cat cannot catch Mouse on its turn nor can it get the food before Mouse.
#
# Example 2:
#
#
# Input: grid = ["M.C...F"], catJump = 1, mouseJump = 4
# Output: true
#
# Example 3:
#
# Input: grid = ["M.C...F"], catJump = 1, mouseJump = 3
# Output: false
#
# Example 4:
#
# Input: grid = ["C...#","...#F","....#","M...."], catJump = 2, mouseJump = 5
# Output: false
#
# Example 5:
#
# Input: grid = [".M...","..#..","#..#.","C#.#.","...#F"], catJump = 3, mouseJump = 1
# Output: true
#
#
# Constraints:
#
# rows == grid.length
# cols = grid[i].length
# 1 <= rows, cols <= 8
# grid[i][j] consist only of characters 'C', 'M', 'F', '.', and '#'.
# There is only one of each character 'C', 'M', and 'F' in grid.
# 1 <= catJump, mouseJump <= 8
#
#

from typing import List, Tuple


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m_pos: Tuple[int, int] = (0, 0)
        c_pos: Tuple[int, int] = (0, 0)
        f_pos: Tuple[int, int] = (0, 0)
        available_pos: int = 0
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == "M":
                    m_pos = (i, j)
                elif c == "C":
                    c_pos = (i, j)
                elif c == "F":
                    f_pos = (i, j)
                # count the available positions
                if c != "#":
                    available_pos += 1

        @lru_cache(None)
        def dp(turn: int, m_pos: Tuple[int, int], c_pos: Tuple[int, int]) -> bool:
            # ending conditions
            if turn == available_pos * 2:
                return False
            if m_pos == c_pos:
                return False
            if c_pos == f_pos:
                return False
            if m_pos == f_pos:
                return True

            # if it is the mouse's turn
            if turn % 2 == 0:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    for m in range(mouseJump + 1):
                        x, y = m_pos[0] + (dx * m), m_pos[1] + (dy * m)
                        # no need to check after obstacles or boundaries
                        if (
                            x < 0
                            or x >= len(grid)
                            or y < 0
                            or y >= len(grid[0])
                            or grid[x][y] == "#"
                        ):
                            break

                        # if the cat is not in the position
                        if (x, y) != c_pos:
                            if dp(turn + 1, (x, y), c_pos):
                                return True

                return False
            # if it is the cat's turn
            else:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    for c in range(catJump + 1):
                        x, y = c_pos[0] + (dx * c), c_pos[1] + (dy * c)
                        # no need to check after obstacles or boundaries
                        if (
                            x < 0
                            or x >= len(grid)
                            or y < 0
                            or y >= len(grid[0])
                            or grid[x][y] == "#"
                        ):
                            break

                        if not dp(turn + 1, m_pos, (x, y)):
                            return False

                return True

        return dp(0, m_pos, c_pos)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1728.py")])
