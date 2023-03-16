# lc 2 
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNum(l1, l2):
        dummy = ListNode()
        carry = 0
        curr = dummy
        
        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            
            #new digit
            val = value1 + value2 + carry
            carry = val //10
            val = val%10
            curr.next = ListNode(val)
            
            curr = curr.next
        return dummy.next