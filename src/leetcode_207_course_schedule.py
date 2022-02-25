# @l2g 207 python3
# [207] Course Schedule
# Difficulty: Medium
# https://leetcode.com/problems/course-schedule
#
# There are a total of numCourses courses you have to take,labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai,
# bi] indicates that you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
#
# Return true if you can finish all courses. Otherwise, return false.
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
# Example 2:
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0,
# and to take course 0 you should also have finished course 1.So it is impossible.
#
#
# Constraints:
#
# 1 <= numCourses <= 10^5
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
#
#

from collections import defaultdict, deque
from typing import DefaultDict, Deque, List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        outbound_graph: DefaultDict[int, List[int]] = defaultdict(list)
        inbound_cnt: List[int] = [0 for _ in range(numCourses)]

        for course, prereq in prerequisites:
            outbound_graph[prereq].append(course)
            inbound_cnt[course] += 1

        pq: Deque = deque(course for course, cnt in enumerate(inbound_cnt) if cnt == 0)

        visited_cnt = 0

        while pq:
            cur_course = pq.popleft()
            visited_cnt += 1
            for next_course in outbound_graph[cur_course]:
                inbound_cnt[next_course] -= 1
                if inbound_cnt[next_course] == 0:
                    pq.append(next_course)

        return visited_cnt == numCourses


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_207.py")])
