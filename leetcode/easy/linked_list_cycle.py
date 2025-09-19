"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer. Internally, pos is used to denote the
index of the node that tail's next pointer is connected to. Note that pos is not passed
as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode | None = None


class Solution:
    def hasCycle_slow(self, head: Optional[ListNode]) -> bool:
        cur = head
        check_counter = counter = 0

        while cur:
            check = head
            check_counter = 0

            while check_counter < counter:
                if check is cur:
                    return True

                check_counter += 1
                check = check.next

            counter += 1
            cur = cur.next

        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast:
            fast = fast.next.next if fast.next else None

            if slow is fast is slow:
                return True

            slow = slow.next

        return False


def test_task():
    s = Solution()

    l0 = ListNode(0)
    l1 = ListNode(1)
    l2 = ListNode(2)
    l0.next = l1
    l1.next = l2

    assert not s.hasCycle(l0)

    l2.next = l1
    assert s.hasCycle(l0)


if __name__ == "__main__":
    test_task()
