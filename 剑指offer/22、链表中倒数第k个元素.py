class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def getKthFromEnd(self, head:ListNode,k:int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter