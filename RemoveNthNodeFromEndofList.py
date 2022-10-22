from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     if head.next is None and n == 1:
    #         return None
    #     count = 1
    #     node = head
    #     while node.next is not None:
    #         node = node.next
    #         count += 1
    #     deleteNo = count - n + 1
    #     print('delete No: ', deleteNo)
    #     node = head
    #     count = 1
    #     preNode = head
    #     while True:
    #         if count == deleteNo:
    #             if node.next is not None:
    #                 node.val = node.next.val
    #                 node.next = node.next.next
    #                 break
    #             else:
    #                 preNode.next = None
    #                 preNode = None
    #                 break
    #
    #         else:
    #             count += 1
    #             preNode = node
    #             node = node.next
    #
    #     return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0)
        slow = start
        fast = start
        start.next = head
        # moving fast pointer n+1 forward to keep the slow pointer just before the delete node
        for i in range(0, n + 1):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return start.next
