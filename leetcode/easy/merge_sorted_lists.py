class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    if list1 and list2:
        if list1.val < list2.val:
            cur = list1
            cur.next = merge(cur.next, list2)
        else:
            cur = list2
            cur.next = merge(list1, cur.next)

        return cur

    else:
        return list1 or list2


def test_task():
    l4 = ListNode(4)
    l2 = ListNode(2, l4)
    l1 = ListNode(1, l2)
    m4 = ListNode(4)
    m3 = ListNode(3, m4)
    m1 = ListNode(1, m3)

    cur = merge(l1, m1)
    expected = []
    while cur is not None:
        expected.append(cur)
        cur = cur.next

    assert expected == [m1, l1, l2, m3, m4, l4]

    assert merge(None, None) is None
    l0 = ListNode(0)
    assert merge(None, l0) == l0


if __name__ == "__main__":
    test_task()
