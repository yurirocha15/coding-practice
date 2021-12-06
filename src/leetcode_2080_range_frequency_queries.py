# @l2g 2080 python3
# [2080] Range Frequency Queries
# Difficulty: Medium
# https://leetcode.com/problems/range-frequency-queries
#
# Design a data structure to find the frequency of a given value in a given subarray.
# The frequency of a value in a subarray is the number of occurrences of that value in the subarray.
# Implement the RangeFreqQuery class:
#
# RangeFreqQuery(int[] arr) Constructs an instance of the class with the given 0-indexed integer array arr.
# int query(int left,int right,int value) Returns the frequency of value in the subarray arr[left...
# right].
#
# A subarray is a contiguous sequence of elements within an array.arr[left...
# right] denotes the subarray that contains the elements of nums between indices left and right (inclusive).
#
# Example 1:
#
# Input
# ["RangeFreqQuery", "query", "query"]
# [[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
# Output
# [null, 1, 2]
#
# Explanation
# RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
# rangeFreqQuery.query(1, 2, 4); // return 1. The value 4 occurs 1 time in the subarray [33, 4]
# rangeFreqQuery.query(0, 11, 33); // return 2. The value 33 occurs 2 times in the whole array.
#
#
# Constraints:
#
# 1 <= arr.length <= 10^5
# 1 <= arr[i], value <= 10^4
# 0 <= left <= right < arr.length
# At most 10^5 calls will be made to query
#
#

import bisect
import collections
from typing import DefaultDict, List


class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.occurrences: DefaultDict[List[int]] = collections.defaultdict(list)
        for i, n in enumerate(arr):
            self.occurrences[n].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        return bisect.bisect_right(self.occurrences[value], right) - bisect.bisect_left(
            self.occurrences[value], left
        )


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2080.py")])
