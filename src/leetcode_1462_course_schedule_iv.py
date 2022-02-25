# @l2g 1462 python3
# [1462] Course Schedule IV
# Difficulty: Medium
# https://leetcode.com/problems/course-schedule-iv
#
# There are a total of numCourses courses you have to take,labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai,
# bi] indicates that you must take course ai first if you want to take course bi.
#
# For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
#
# Prerequisites can also be indirect.If course a is a prerequisite of course b,
# and course b is a prerequisite of course c,then course a is a prerequisite of course c.
# You are also given an array queries where queries[j] = [uj,vj].For the jth query,
# you should answer whether course uj is a prerequisite of course vj or not.
# Return a boolean array answer, where answer[j] is the answer to the jth query.
#
# Example 1:
#
#
# Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
# Output: [false,true]
# Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
# Course 0 is not a prerequisite of course 1, but the opposite is true.
#
# Example 2:
#
# Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
# Output: [false,false]
# Explanation: There are no prerequisites, and each course is independent.
#
# Example 3:
#
#
# Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
# Output: [true,true]
#
#
# Constraints:
#
# 2 <= numCourses <= 100
# 0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
# prerequisites[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
# All the pairs [ai, bi] are unique.
# The prerequisites graph has no cycles.
# 1 <= queries.length <= 10^4
# 0 <= ui, vi <= n - 1
# ui != vi
#
#

from collections import defaultdict, deque
from typing import DefaultDict, Deque, List, Set


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        inbound_graph: DefaultDict[int, Set[int]] = defaultdict(set)
        outbound_cnt: List[int] = [0 for _ in range(numCourses)]

        for prereq, course in prerequisites:
            inbound_graph[course].add(prereq)
            outbound_cnt[prereq] += 1

        unlocks: DefaultDict[int, Set[int]] = defaultdict(set)

        pq: Deque = deque(course for course, cnt in enumerate(outbound_cnt) if cnt == 0)

        while pq:
            cur_course = pq.popleft()
            for prereq in inbound_graph[cur_course]:
                unlocks[prereq] |= unlocks[cur_course]
                unlocks[prereq].add(cur_course)
                outbound_cnt[prereq] -= 1
                if outbound_cnt[prereq] == 0:
                    pq.append(prereq)

        res: List[bool] = []

        for prereq, course in queries:
            res.append(course in unlocks[prereq])

        return res


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1462.py")])
