# @l2g 2018 python3
# [2018] Check if Word Can Be Placed In Crossword
# Difficulty: Medium
# https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword
#
# You are given an m x n matrix board,representing the current state of a crossword puzzle.
# The crossword contains lowercase English letters (from solved words),
# ' ' to represent any empty cells,and '#' to represent any blocked cells.
# A word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top) in the board if:
#
# It does not occupy a cell containing the character '#'.
# The cell each letter is placed in must either be ' ' (empty) or match the letter already on the board.
# There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.
# There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.
#
# Given a string word, return true if word can be placed in board, or false otherwise.
#
# Example 1:
#
#
# Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"
# Output: true
# Explanation: The word "abc" can be placed as shown above (top to bottom).
#
# Example 2:
#
#
# Input: board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"
# Output: false
# Explanation: It is impossible to place the word because there will always be a space/letter above or below it.
# Example 3:
#
#
# Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"
# Output: true
# Explanation: The word "ca" can be placed as shown above (right to left).
#
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m * n <= 2 * 10^5
# board[i][j] will be ' ', '#', or a lowercase English letter.
# 1 <= word.length <= max(m, n)
# word will contain only lowercase English letters.
#
#

from typing import Dict, List, Tuple


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m: int = len(board)
        n: int = len(board[0])

        for i in range(m):
            valid1 = valid2 = True
            st: int = 0
            for j in range(n):
                if board[i][j] == "#":
                    if (valid1 or valid2) and len(word) == j - st:
                        return True
                    else:
                        st = j + 1
                        valid1 = valid2 = True
                elif j - st >= len(word):
                    valid1 = valid2 = False
                else:
                    if valid1 and board[i][j] != " " and board[i][j] != word[j - st]:
                        valid1 = False
                    if (
                        valid2
                        and board[i][j] != " "
                        and board[i][j] != word[len(word) - 1 - j + st]
                    ):
                        valid2 = False
            if (valid1 or valid2) and len(word) == n - st:
                return True

        for j in range(n):
            valid1 = valid2 = True
            st = 0
            for i in range(m):
                if board[i][j] == "#":
                    if (valid1 or valid2) and len(word) == i - st:
                        return True
                    else:
                        st = i + 1
                        valid1 = valid2 = True
                elif i - st >= len(word):
                    valid1 = valid2 = False
                else:
                    if valid1 and board[i][j] != " " and board[i][j] != word[i - st]:
                        valid1 = False
                    if (
                        valid2
                        and board[i][j] != " "
                        and board[i][j] != word[len(word) - 1 - i + st]
                    ):
                        valid2 = False
            if (valid1 or valid2) and len(word) == m - st:
                return True

        return False


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2018.py")])
