# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     if list1 is None:
    #         return list2
    #     elif list2 is None:
    #         return list1
    #
    #     if list1.val <= list2.val:
    #         mergedList = list1
    #         list1 = list1.next
    #     else:
    #         mergedList = list2
    #         list2 = list2.next
    #     mergedList.next = None
    #     mergedListHead = mergedList
    #     while list1 is not None and list2 is not None:
    #         if list1.val <= list2.val:
    #             mergedList.next = list1
    #             mergedList = mergedList.next
    #             list1 = list1.next
    #             mergedList.next = None
    #
    #         elif list2.val <= list1.val:
    #             mergedList.next = list2
    #             mergedList = mergedList.next
    #             list2 = list2.next
    #             mergedList.next = None
    #
    #     if list1 is not None:
    #         mergedList.next = list1
    #     elif list2 is not None:
    #         mergedList.next = list2
    #
    #     return mergedListHead

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


def main():
    print("Hello World!")
    solution = Solution()
    tempList = [1, 2, 4]
    prev = ListNode(tempList[0])
    head1 = prev
    for i in range(1, len(tempList)):
        node = ListNode(tempList[i])
        prev.next = node
        prev = node
    prev.next = None

    tempList = [1, 3, 4]
    prev = ListNode(tempList[0])
    head2 = prev
    for i in range(1, len(tempList)):
        node = ListNode(tempList[i])
        prev.next = node
        prev = node
    prev.next = None

    result = solution.mergeTwoLists(head1, head2)
    print(result.val)


if __name__ == "__main__":
    main()
