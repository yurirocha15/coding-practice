# @l2g 2049 python3
# [2049] Count Nodes With the Highest Score
# Difficulty: Medium
# https://leetcode.com/problems/count-nodes-with-the-highest-score
#
# There is a binary tree rooted at 0 consisting of n nodes.The nodes are labeled from 0 to n - 1.
# You are given a 0-indexed integer array parents representing the tree,
# where parents[i] is the parent of node i.Since node 0 is the root,parents[0] == -1.
# Each node has a score.To find the score of a node,
# consider if the node and the edges connected to it were removed.
# The tree would become one or more non-empty subtrees.
# The size of a subtree is the number of the nodes in it.
# The score of the node is the product of the sizes of all those subtrees.
# Return the number of nodes that have the highest score.
#
# Example 1:
#
#
# Input: parents = [-1,2,0,2,0]
# Output: 3
# Explanation:
# - The score of node 0 is: 3 * 1 = 3
# - The score of node 1 is: 4 = 4
# - The score of node 2 is: 1 * 1 * 2 = 2
# - The score of node 3 is: 4 = 4
# - The score of node 4 is: 4 = 4
# The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.
#
# Example 2:
#
#
# Input: parents = [-1,2,0]
# Output: 2
# Explanation:
# - The score of node 0 is: 2 = 2
# - The score of node 1 is: 2 = 2
# - The score of node 2 is: 1 * 1 = 1
# The highest score is 2, and two nodes (node 0 and node 1) have the highest score.
#
#
# Constraints:
#
# n == parents.length
# 2 <= n <= 10^5
# parents[0] == -1
# 0 <= parents[i] <= n - 1 for i != 0
# parents represents a valid binary tree.
#
#

from typing import Any, Dict, List, Tuple


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        tree: List[List[int]] = [[] for _ in parents]
        costs: List[int] = [1 for _ in parents]
        for i, p in enumerate(parents[1:], 1):
            tree[p].append(i)

        def fill_tree(cur: int) -> int:
            if not tree[cur]:
                return 1
            cost = 1
            for child in tree[cur]:
                cost += fill_tree(child)
            costs[cur] = cost
            return cost

        fill_tree(0)

        max_cost, cnt = 0, 0
        for i, node in enumerate(tree):
            cost = max(costs[0] - costs[i], 1)
            for child in node:
                cost *= max(costs[child], 1)
            if cost == max_cost:
                cnt += 1
            elif cost > max_cost:
                max_cost = cost
                cnt = 1
        return cnt


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2049.py")])
