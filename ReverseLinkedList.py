# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head is None or head.next is None:
    #         return head
    #     prev = head
    #     current = head
    #     while current is not None:
    #         temp = current.next
    #         current.next = prev
    #         prev = current
    #         current = temp
    #
    #         if prev is head:
    #             prev.next = None
    #
    #     return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = ListNode(head.val)
        prev.next = None
        return self.reverseListRecursive(head.next, prev)

    def reverseListRecursive(self, current: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
        if current is None:
            return prev
        temp = current.next
        current.next = prev
        prev = current
        current = temp

        return self.reverseListRecursive(current, prev)


def main():
    print("Hello World!")
    solution = Solution()
    list = [1, 2, 3, 4, 5]
    prev = ListNode(list[0])
    head = prev
    for i in range(1, len(list)):
        node = ListNode(list[i])
        prev.next = node
        prev = node
    prev.next = None

    result = solution.reverseList(head)
    print(result.val)


if __name__ == "__main__":
    main()
