# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
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

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        strVal1 = ''
        headRef = head
        while head is not None:
            strVal1 += str(head.val)
            head = head.next

        reversedHead = self.reverseList(headRef)
        strVal2 = ''
        while reversedHead is not None:
            strVal2 += str(reversedHead.val)
            reversedHead = reversedHead.next
        if strVal1 == strVal2:
            return True

        return False


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

    tempList = [1, 2, 2, 1]
    prev = ListNode(tempList[0])
    head2 = prev
    for i in range(1, len(tempList)):
        node = ListNode(tempList[i])
        prev.next = node
        prev = node
    prev.next = None

    result = solution.isPalindrome(head2)
    print(result)


if __name__ == "__main__":
    main()
