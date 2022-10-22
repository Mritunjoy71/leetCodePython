# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # tempSet = set()
        # while head is not None:
        #     if head in tempSet:
        #         print("true")
        #         return True
        #     tempSet.add(head)
        #     head = head.next
        #     print("hitting next")
        if head is None:
            return False
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


def main():
    print("Hello World!")
    solution = Solution()
    # tempList = [1, 2, 4]
    # prev = ListNode(tempList[0])
    # head1 = prev
    # for i in range(1, len(tempList)):
    #     node = ListNode(tempList[i])
    #     prev.next = node
    #     prev = node
    # prev.next = None

    tempList = [1, 2]
    prev = ListNode(tempList[0])
    head2 = prev
    for i in range(1, len(tempList)):
        node = ListNode(tempList[i])
        prev.next = node
        prev = node
    prev.next = None

    result = solution.hasCycle(head2)
    print("result: ", result)


if __name__ == "__main__":
    main()
