# @l2g 2074 python3
# [2074] Reverse Nodes in Even Length Groups
# Difficulty: Medium
# https://leetcode.com/problems/reverse-nodes-in-even-length-groups
#
# You are given the head of a linked list.
# The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1,
# 2,3,4,...).The length of a group is the number of nodes assigned to it.In other words,
#
# The 1st node is assigned to the first group.
# The 2nd and the 3rd nodes are assigned to the second group.
# The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
#
# Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.
# Reverse the nodes in each group with an even length,and return the head of the modified linked list.
#
# Example 1:
#
#
# Input: head = [5,2,6,3,9,1,7,3,8,4]
# Output: [5,6,2,3,9,1,4,8,3,7]
# Explanation:
# - The length of the first group is 1, which is odd, hence no reversal occurrs.
# - The length of the second group is 2, which is even, hence the nodes are reversed.
# - The length of the third group is 3, which is odd, hence no reversal occurrs.
# - The length of the last group is 4, which is even, hence the nodes are reversed.
#
# Example 2:
#
#
# Input: head = [1,1,0,6]
# Output: [1,0,1,6]
# Explanation:
# - The length of the first group is 1. No reversal occurrs.
# - The length of the second group is 2. The nodes are reversed.
# - The length of the last group is 1. No reversal occurrs.
#
# Example 3:
#
#
# Input: head = [1,1,0,6,5]
# Output: [1,0,1,5,6]
# Explanation:
# - The length of the first group is 1. No reversal occurrs.
# - The length of the second group is 2. The nodes are reversed.
# - The length of the last group is 2. The nodes are reversed.
#
# Example 4:
#
#
# Input: head = [2,1]
# Output: [2,1]
# Explanation:
# - The length of the first group is 1. No reversal occurrs.
# - The length of the last group is 1. No reversal occurrs.
#
# Example 5:
#
# Input: head = [8]
# Output: [8]
# Explanation: There is only one group whose length is 1. No reversal occurrs.
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 10^5
#
#

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: Optional["ListNode"] = next

    def __repr__(self) -> str:
        next_val = str(self.next.val) if self.next else "None"
        return str(self.val) + " -> " + next_val


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        max_size = 2
        i = 0
        final_node_parent = last_node = head
        final_node = current = last_node.next
        while current:
            cnt = 0
            while cnt < max_size and current:
                cnt += 1
                last_node = current
                current = current.next
            if cnt and not cnt % 2:
                current = final_node
                i = 0
                while i < max_size and current:
                    cnt += 1
                    next_node = current.next
                    current.next = last_node
                    last_node = current
                    current = next_node
                    i += 1
                final_node.next = current
                final_node_parent.next = last_node
                final_node_parent = final_node
            else:
                final_node_parent = last_node
            final_node = current

            max_size += 1
        return head


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2074.py")])
