#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1743. Restore the Array From Adjacent Pairs
URL: https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/
"""
from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def restore_array(self, adjacentPairs: List[List[int]]) -> List[int]:
        d: DefaultDict[int, List[int]] = defaultdict(list)
        for ap in adjacentPairs:
            d[ap[0]].append(ap[1])
            d[ap[1]].append(ap[0])

        for _head, edges in d.items():
            if len(edges) < 2:
                break
        head = _head
        ret = [head]
        nxt = edges[0]
        while len(d[nxt]) == 2:
            head, nxt = nxt, d[nxt][0] if d[nxt][0] != head else d[nxt][1]
            ret.append(head)
        ret.append(nxt)
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.restore_array(adjacentPairs=[[2, 1], [3, 4], [3, 2]]) == [
        1,
        2,
        3,
        4,
    ]
    assert solution.restore_array(adjacentPairs=[[4, -2], [1, 4], [-3, 1]]) == [
        -2,
        4,
        1,
        -3,
    ]
    assert solution.restore_array(adjacentPairs=[[100000, -100000]]) == [
        100000,
        -100000,
    ]
