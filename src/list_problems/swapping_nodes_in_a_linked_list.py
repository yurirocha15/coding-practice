#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1721. Swapping Nodes in a Linked List
URL: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

Description:
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping
the values of the kth node from the beginning
and the kth node from the end (the list is 1-indexed).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Example 3:
Input: head = [1], k = 1
Output: [1]

Example 4:
Input: head = [1,2], k = 1
Output: [2,1]

Example 5:
Input: head = [1,2,3], k = 2
Output: [1,2,3]

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 10^5
0 <= Node.val <= 100
"""
from __future__ import annotations

from attr import dataclass


@dataclass
class ListNode:
    val: int
    next: ListNode = None


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        first = last = current = head
        i = 1
        while current is not None:
            if i == k:
                first = current
            elif i > k:
                last = last.next
            i, current = i + 1, current.next
        first.val, last.val = last.val, first.val
        return head


if __name__ == "__main__":
    solution = Solution()
    head = None
    input = [1, 2, 3, 4, 5]
    for n in input[::-1]:
        head = ListNode(n, head)
    assert solution.swapNodes(head, 2).next.val == 4
