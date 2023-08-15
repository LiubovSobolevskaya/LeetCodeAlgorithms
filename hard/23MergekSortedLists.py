# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        elements = []
        
        for l in lists:
           while l:
               elements.append(l.val)
               l = l.next
        elements.sort()

        head = point = ListNode(0)
        for i in range(len(elements)):
            element = ListNode(elements[i])
            head.next = element
            head = element

        return point.next