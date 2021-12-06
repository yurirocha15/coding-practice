# @l2g 2081 python3
# [2081] Sum of k-Mirror Numbers
# Difficulty: Hard
# https://leetcode.com/problems/sum-of-k-mirror-numbers
#
# A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.
#
# For example,9 is a 2-mirror number.
# The representation of 9 in base-10 and base-2 are 9 and 1001 respectively,
# which read the same both forward and backward.
# On the contrary,4 is not a 2-mirror number.The representation of 4 in base-2 is 100,
# which does not read the same both forward and backward.
#
# Given the base k and the number n, return the sum of the n smallest k-mirror numbers.
#
# Example 1:
#
# Input: k = 2, n = 5
# Output: 25
# Explanation:
# The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
#   base-10    base-2
#     1          1
#     3          11
#     5          101
#     7          111
#     9          1001
# Their sum = 1 + 3 + 5 + 7 + 9 = 25.
#
# Example 2:
#
# Input: k = 3, n = 7
# Output: 499
# Explanation:
# The 7 smallest 3-mirror numbers are and their representations in base-3 are listed as follows:
#   base-10    base-3
#     1          1
#     2          2
#     4          11
#     8          22
#     121        11111
#     151        12121
#     212        21212
# Their sum = 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499.
#
# Example 3:
#
# Input: k = 7, n = 17
# Output: 20379000
# Explanation: The 17 smallest 7-mirror numbers are:
# 1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596
#
#
# Constraints:
#
# 2 <= k <= 9
# 1 <= n <= 30
#
#


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def generate_palindrome():
            nums_1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            nums_2 = ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99"]
            while True:
                for num in nums_1:
                    if num[0] == "0":
                        continue
                    yield int(num)
                for num in nums_2:
                    if num[0] == "0":
                        continue
                    yield int(num)

                nums_1 = [str(n) + num + str(n) for n in range(10) for num in nums_1]
                nums_2 = [str(n) + num + str(n) for n in range(10) for num in nums_2]

        def is_palindrome_on_base(num: int, base: int) -> bool:
            digits = []
            while num > 0:
                num, digit = divmod(num, base)
                digits.append(digit)
            for i in range(len(digits) // 2):
                if digits[i] != digits[-i - 1]:
                    return False
            return True

        g = generate_palindrome()

        cnt = res = 0
        while cnt < n:
            num = next(g)
            if is_palindrome_on_base(num, k):
                print(num)
                cnt += 1
                res += num

        return res


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2081.py")])
