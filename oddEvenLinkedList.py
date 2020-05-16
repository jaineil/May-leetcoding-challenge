# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head == None: return None
        
        odd = head
        even = head.next
        evenHead = even
        
        while(even != None and even.next != None): # think in pairs of 2, so even limit
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        # elegantly joining odd.head at last ele of odd to evenHead at first ele of even
        odd.next = evenHead 
        return head 
    
'''
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        curr = head
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next
            
        i = 0
        curr = head
        while i < len(values):
            curr.val = values[i]
            curr = curr.next
            i+=2
        i = 1
        while i < len(values):
            curr.val = values[i]
            curr = curr.next
            i+=2
        return head
'''