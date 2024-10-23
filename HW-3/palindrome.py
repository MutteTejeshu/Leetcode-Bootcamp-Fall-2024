# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        halfPtr = head
        lastPtr = head
        prevPtr = None
        if head.next == None:
            return True

        while lastPtr and lastPtr.next:
            lastPtr = lastPtr.next.next

            tmpPtr = halfPtr.next
            halfPtr.next = prevPtr
            prevPtr = halfPtr
            halfPtr = tmpPtr

        if lastPtr != None:
            halfPtr = halfPtr.next
        
        while halfPtr and prevPtr:
            if halfPtr.val != prevPtr.val:
                return False
            halfPtr = halfPtr.next
            prevPtr = prevPtr.next
        return True
        
