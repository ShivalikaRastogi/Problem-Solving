# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        while l1 != None:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2 != None:
            num2 = str(l2.val) + num2
            l2 = l2.next
        num = int(num1) + int(num2)
        res = ListNode(0)
        head = res
        if num == 0:
            return res
        while num > 0:
            rem = num % 10
            temp = ListNode(rem)
            res.next = temp
            res = res.next
            num = num // 10
        return head.next