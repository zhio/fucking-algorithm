"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

"""

class ListNode:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

# 使用迭代的方式
def reverseList(head: ListNode) -> ListNode:
    cur, pre = head, None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

# 使用递归的方式
def reverseList2(head: ListNode) -> ListNode:
    def recur(cur,pre):
        if not cur: return pre
        res = recur(cur.next,cur)
        cur.next = pre
        return res
    return recur(head,None)
