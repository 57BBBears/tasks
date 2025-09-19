from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers1(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    cur_node = ListNode()

    while l1 or l2:
        cur_node = ListNode()
        val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + cur_node.val
        if val < 10:
            cur_node.val = val
            next_node = ListNode()
        else:
            cur_node.val = val % 10
            next_node = ListNode(1)

        cur_node.next = next_node
        cur_node = next_node

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None


def addTwoNumbers2(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    prev_node = result = ListNode()
    extra = 0

    while l1 or l2:
        cur_node = ListNode()
        val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + extra

        if val < 10:
            cur_node.val = val
            extra = 0
        else:
            cur_node.val = val % 10
            extra = 1

        prev_node.next = cur_node
        prev_node = cur_node

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if extra:
        cur_node.next = ListNode(1)

    return result.next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if l1 and not l2:
        return l1
    elif l2 and not l1:
        return l2

    if not (l1 or l2):
        return None

    node = ListNode()
    val = l1.val + l2.val

    if val < 10:
        node.val = val
        node.next = addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None)
    else:
        node.val = val % 10
        node.next = addTwoNumbers(
            addTwoNumbers(ListNode(1), l1.next if l1 else None), l2.next if l2 else None
        )

    return node


if __name__ == "__main__":
    l1 = ListNode(9)
    l2 = ListNode(9, l1)
    l3 = ListNode(9, l2)

    res = addTwoNumbers(l1, l2)

    while True:
        if res:
            print(res.val)
            res = res.next
        else:
            break
