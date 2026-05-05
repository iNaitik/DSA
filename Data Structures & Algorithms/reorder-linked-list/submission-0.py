# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        #reverse second half
        second = slow.next
        slow.next = None  #1 → 2 → 3   and   4 → 5
        prev = None
        while second :
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #Merge
        first = head
        second = prev  #prev is Head of new list
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2 



