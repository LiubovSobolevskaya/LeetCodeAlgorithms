# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseKelements(self, head: Optional[ListNode], k: int)-> Optional[ListNode]:
        ptr = head
        prev = None
        counter = 0
        while counter<k and ptr!=None:
            nextEl = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = nextEl
            counter+=1

        return prev


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        counter = 0
        oldHead = ptr = head
        while counter<k and ptr:
            counter+=1
            ptr = ptr.next
        if counter == k:
            newHead = self.reverseKelements(head, k)
            oldHead.next = self.reverseKGroup(ptr, k)
        else:
            newHead = oldHead

        return newHead

         


       
  
                




            

