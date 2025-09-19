"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from typing import Callable, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = head
        cur = head.next

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        head.next = None

        return prev

    def reverseList_recur(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        reversed_head = self.reverseList_recur(head.next)

        head.next.next = head

        head.next = None

        return reversed_head


def test_task(func: Callable):
    l0 = ListNode(0)
    l1 = ListNode(1)
    l2 = ListNode(2)
    l0.next = l1
    l1.next = l2

    assert func(l0) is l2
    assert l2.next is l1
    assert l1.next is l0
    assert l0.next is None

    assert func(None) is None


if __name__ == "__main__":
    s = Solution()
    test_task(s.reverseList)
    test_task(s.reverseList_recur)
