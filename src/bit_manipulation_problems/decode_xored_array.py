#!/usr/bin/env python
"""
Platform: LeetCode
1720. Decode XORed Array
URL: https://leetcode.com/problems/decode-xored-array/

Description:
There is a hidden integer array arr that consists of n non-negative integers.

It was encoded into another integer array encoded of length n - 1,
such that encoded[i] = arr[i] XOR arr[i + 1].
For example, if arr = [1,0,2,1], then encoded = [1,2,3].

You are given the encoded array.
You are also given an integer first,
that is the first element of arr, i.e. arr[0].

Return the original array arr.
It can be proved that the answer exists and is unique.


Example 1:
Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]
Explanation: If arr = [1,0,2,1], then first = 1
and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]

Example 2:
Input: encoded = [6,2,7,3], first = 4
Output: [4,2,0,7,4]

Constraints:
2 <= n <= 10^4
encoded.length == n - 1
0 <= encoded[i] <= 10^5
0 <= first <= 10^5
"""
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # the inverse of the XOR operation is the XOR operation
        # the walrus operator ':=' stores the value in the list while also
        # assigning it to the left side variable (requires Python 3.8)
        # mypy and flake8 seem to not like the walrus operator yet
        # return [first] + [first := first ^ n for n in encoded]
        ret = [first]
        for n in encoded:
            first = first ^ n
            ret.append(first)
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.decode([1, 2, 3], 1) == [1, 0, 2, 1]
    assert solution.decode([6, 2, 7, 3], 4) == [4, 2, 0, 7, 4]
