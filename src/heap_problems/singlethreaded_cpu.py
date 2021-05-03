#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1834. Single-Threaded CPU
URL: https://leetcode.com/problems/single-threaded-cpu/description/
"""
import heapq
from typing import List, Tuple


# O(NlogN) / O(N)
class Solution:
    def get_order(self, tasks: List[List[int]]) -> List[int]:
        curr_time = 0
        pq: List[Tuple[int, int, int]] = []
        ret: List[int] = []
        # save original index before sorting
        task_list = sorted([(task[0], task[1], idx) for idx, task in enumerate(tasks)])
        for enqueue_t, proc_t, idx in task_list:
            # if we cannot perform the current task, do the next task in the queue until
            # it is empty or we can add the current task to the queue
            while pq and curr_time < enqueue_t:
                done_proc_t, done_idx, done_enqueue_t = heapq.heappop(pq)
                ret.append(done_idx)
                # if the task enqueue time is after current time, if should start from enqueue time
                curr_time = max(curr_time, done_enqueue_t) + done_proc_t
            # add current task to the queue
            heapq.heappush(pq, (proc_t, idx, enqueue_t))
        # empty the queue
        while pq:
            ret.append(heapq.heappop(pq)[1])
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.get_order(tasks=[[1, 2], [2, 4], [3, 2], [4, 1]]) == [0, 2, 3, 1]
    assert solution.get_order(tasks=[[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]) == [
        4,
        3,
        2,
        0,
        1,
    ]
