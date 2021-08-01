# @l2g 1723 python3
# [1723] Find Minimum Time to Finish All Jobs
# Difficulty: Hard
# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs
#
# You are given an integer array jobs,
# where jobs[i] is the amount of time it takes to complete the ith job.
# There are k workers that you can assign jobs to.Each job should be assigned to exactly one worker.
# The working time of a worker is the sum of the time it takes to complete all jobs assigned to them.
# Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.
# Return the minimum possible maximum working time of any assignment.
#
# Example 1:
#
# Input: jobs = [3,2,3], k = 3
# Output: 3
# Explanation: By assigning each person one job, the maximum time is 3.
#
# Example 2:
#
# Input: jobs = [1,2,4,7,8], k = 2
# Output: 11
# Explanation: Assign the jobs the following way:
# Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
# Worker 2: 4, 7 (working time = 4 + 7 = 11)
# The maximum working time is 11.
#
# Constraints:
#
# 1 <= k <= jobs.length <= 12
# 1 <= jobs[i] <= 10^7
#
#

from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # each worker workload
        workload: List[int] = [0] * k

        # recursive dfs for each task
        def dfs(idx: int, cur_best: int = 10 ** 100) -> int:
            # if there is no more tasks, return the longest workload
            if idx == len(jobs):
                return max(workload)
            else:
                # loop through each worker
                for worker in range(k):
                    # if the workload is the same as the last worker
                    # no reason to expand the search
                    # as it will yield the same result
                    if not worker or workload[worker - 1] != workload[worker]:
                        # add the task to the worker
                        workload[worker] += jobs[idx]
                        # if this new workload is worse than the current best
                        # no reason to expand the search
                        if workload[worker] < cur_best:
                            # call dfs for the next task
                            cur_best = min(dfs(idx + 1, cur_best), cur_best)
                        # remove the task from the worker
                        # so it can be added to the next worker
                        workload[worker] -= jobs[idx]
                return cur_best

        return dfs(0)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1723.py")])
